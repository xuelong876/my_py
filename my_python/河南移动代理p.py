# -*- coding: utf-8 -*-
# socks5.py (Parser 版 v5) —— 逐行代理 + 可选前置链 + https 代理
# v5: ip/pre 支持 https:// 代理 (TLS 连代理, 不校验其证书); 其余同 v4
# 加载通道: base.parser.Parser; 名单写法: 频道名,脚本地址?ip=代理&u=流地址
# ip 写法: 裸 IP:端口 = socks5; 带协议头按协议走 (http:// / https:// / socks5://)
# 前置: 多加一个 pre 参数即可, 写法与 ip 相同, 例:
#   ...?ip=218.201.248.177:7302&pre=http://139.9.215.192:10088&u=流地址
#   链路: 播放器 -> 脚本本地中继 -> 前置 -> ip 代理 -> 源站
# 不带 pre 时与 v3 行为完全一致 (requests 直挂 ip 代理).
import requests
import urllib.parse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import socket
import ssl
import struct
import threading

try:
    import urllib3
    urllib3.disable_warnings()
except Exception:
    pass

try:
    from base.parser import Parser as BaseParser
except Exception:
    class BaseParser(object):
        pass

_original_getaddrinfo = socket.getaddrinfo


def _getaddrinfo_ipv4_only(*args, **kwargs):
    res = _original_getaddrinfo(*args, **kwargs)
    v4 = [r for r in res if r[0] == socket.AF_INET]
    return v4 if v4 else res


RESERVED = ('ip', 'u', 'url', 'pre')


def _split_proxy(spec):
    """ 'http://h:p' / 'socks5://h:p' / 裸 'h:p'(=socks5) -> (scheme, host, port) """
    s = str(spec or '').strip()
    scheme = 'socks5'
    if '://' in s:
        scheme, s = s.split('://', 1)
        scheme = scheme.lower()
    s = s.rstrip('/')
    if '@' in s:
        s = s.rsplit('@', 1)[1]
    if ':' in s:
        h, p = s.rsplit(':', 1)
        try:
            return scheme, h, int(p)
        except Exception:
            return scheme, h, 1080
    return scheme, s, 1080


def _socks5_client(sock, dst_host, dst_port):
    """在已连接的 socket 上完成 socks5 客户端握手 (目标域名原样发给对方解析)"""
    sock.sendall(b'\x05\x01\x00')
    r = sock.recv(2)
    if len(r) != 2 or r[0] != 5 or r[1] != 0:
        raise IOError('socks5 handshake failed')
    hb = dst_host.encode('utf-8')
    sock.sendall(b'\x05\x01\x00\x03' + bytes([len(hb)]) + hb +
                 struct.pack('>H', dst_port))
    r = sock.recv(4)
    if len(r) != 4 or r[1] != 0:
        raise IOError('socks5 connect failed')
    atyp = r[3]
    if atyp == 1:
        sock.recv(4)
    elif atyp == 3:
        sock.recv(sock.recv(1)[0])
    elif atyp == 4:
        sock.recv(16)
    sock.recv(2)
    return sock


def _http_connect(sock, dst_host, dst_port):
    sock.sendall(('CONNECT %s:%d HTTP/1.1\r\nHost: %s:%d\r\n\r\n'
                  % (dst_host, dst_port, dst_host, dst_port)).encode())
    buf = b''
    while b'\r\n\r\n' not in buf:
        d = sock.recv(4096)
        if not d:
            raise IOError('http connect closed')
        buf += d
    if b' 200' not in buf.split(b'\r\n')[0]:
        raise IOError('http connect refused')
    return sock


def _pump(a, b):
    try:
        while True:
            d = a.recv(65536)
            if not d:
                break
            b.sendall(d)
    except Exception:
        pass
    try:
        b.shutdown(socket.SHUT_WR)
    except Exception:
        pass


def _tls_wrap(sock, server_hostname):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx.wrap_socket(sock, server_hostname=server_hostname)


class _Chain(object):
    """本地中继: 入口按第二跳协议收话, 经前置隧道到第二跳代理, 再由它到源站"""

    def __init__(self, front_spec, second_spec):
        self.front = _split_proxy(front_spec)
        self.second = _split_proxy(second_spec)
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(('127.0.0.1', 0))
        self.srv.listen(16)
        self.port = self.srv.getsockname()[1]
        self.alive = True
        threading.Thread(target=self._accept_loop, daemon=True).start()

    def entry_url(self):
        scheme = 'socks5' if self.second[0] == 'socks5' else 'http'
        return '%s://127.0.0.1:%d' % (scheme, self.port)

    def close(self):
        self.alive = False
        try:
            self.srv.close()
        except Exception:
            pass

    def _accept_loop(self):
        while self.alive:
            try:
                c, _ = self.srv.accept()
            except Exception:
                return
            threading.Thread(target=self._handle, args=(c,), daemon=True).start()

    def _to_second(self):
        fs, fh, fp = self.front
        _, sh, sp = self.second
        raw = socket.create_connection((fh, fp), timeout=20)
        if fs == 'https':
            raw = _tls_wrap(raw, fh)
        if fs == 'socks5':
            _socks5_client(raw, sh, sp)
        else:
            _http_connect(raw, sh, sp)
        raw.settimeout(60)
        return raw

    def _to_origin(self, dst_host, dst_port):
        up = self._to_second()
        if self.second[0] == 'https':
            up = _tls_wrap(up, self.second[1])
        if self.second[0] == 'socks5':
            _socks5_client(up, dst_host, dst_port)
        else:
            _http_connect(up, dst_host, dst_port)
        return up

    def _handle(self, client):
        try:
            client.settimeout(60)
            first = client.recv(1, socket.MSG_PEEK)
            if first == b'\x05':
                self._handle_socks(client)
            else:
                self._handle_http(client)
        except Exception:
            try:
                client.close()
            except Exception:
                pass

    def _handle_socks(self, client):
        n = client.recv(2)
        if len(n) < 2:
            return
        client.recv(n[1])
        client.sendall(b'\x05\x00')
        h = client.recv(4)
        if len(h) < 4 or h[1] != 1:
            return
        atyp = h[3]
        if atyp == 1:
            host = socket.inet_ntoa(client.recv(4))
        elif atyp == 3:
            host = client.recv(client.recv(1)[0]).decode()
        else:
            client.recv(16)
            host = ''
        port = struct.unpack('>H', client.recv(2))[0]
        up = self._to_origin(host, port)
        client.sendall(b'\x05\x00\x00\x01\x00\x00\x00\x00\x00\x00')
        threading.Thread(target=_pump, args=(client, up), daemon=True).start()
        _pump(up, client)

    def _handle_http(self, client):
        buf = b''
        while b'\r\n\r\n' not in buf:
            d = client.recv(65536)
            if not d:
                return
            buf += d
        head, _, rest = buf.partition(b'\r\n\r\n')
        lines = head.split(b'\r\n')
        method, target, ver = lines[0].decode('latin1').split(' ', 2)
        if method.upper() == 'CONNECT':
            hp = target if ':' in target else target + ':443'
            host, port = hp.rsplit(':', 1)
            up = self._to_origin(host, int(port))
            client.sendall(b'HTTP/1.1 200 Connection Established\r\n\r\n')
            if rest:
                up.sendall(rest)
            threading.Thread(target=_pump, args=(client, up), daemon=True).start()
            _pump(up, client)
            return
        # 绝对地址形式的普通请求 (http 目标经 http 第二跳)
        u = urllib.parse.urlsplit(target)
        if self.second[0] == 'socks5':
            up = self._to_origin(u.hostname, u.port or 80)
            path = u.path or '/'
            if u.query:
                path += '?' + u.query
            keep = [ln for ln in lines[1:]
                    if not ln.lower().startswith(b'proxy-')]
            new_head = ('%s %s %s' % (method, path, ver)).encode() + \
                b'\r\n' + b'\r\n'.join(keep) + b'\r\n\r\n'
            up.sendall(new_head + rest)
        else:
            up = self._to_second()
            if self.second[0] == 'https':
                up = _tls_wrap(up, self.second[1])
            up.sendall(buf)
        threading.Thread(target=_pump, args=(client, up), daemon=True).start()
        _pump(up, client)


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except Exception:
            pass
        if not getattr(self, 'address', None):
            self.address = 'http://127.0.0.1:9978/proxy'
        self.session = self._create_session()
        self._chain = None
        self._chain_key = None

    def _create_session(self):
        s = requests.Session()
        s.verify = False
        retry = Retry(total=2, backoff_factor=0.1,
                      status_forcelist=[408, 500, 502, 503, 504, 599])
        adapter = HTTPAdapter(pool_connections=20, pool_maxsize=50,
                              max_retries=retry)
        s.mount('http://', adapter)
        s.mount('https://', adapter)
        s.headers.update({
            'Accept': '*/*',
            'Accept-Encoding': 'identity',
            'Connection': 'keep-alive',
            'User-Agent': 'okhttp/3.15',
        })
        return s

    def _proxies(self, ip, pre=''):
        if not ip:
            return {}
        if pre:
            key = (pre, ip)
            if self._chain is None or self._chain_key != key:
                if self._chain is not None:
                    self._chain.close()
                self._chain = _Chain(pre, ip)
                self._chain_key = key
            entry = self._chain.entry_url()
            return {'http': entry, 'https': entry}
        if '://' in ip:
            return {'http': ip, 'https': ip}
        return {'http': 'socks5://' + ip, 'https': 'socks5://' + ip}

    # ---------- 打包 ----------
    def parse(self, params, raw_query_string=None):
        ip = str(params.get('ip', '') or '').strip()
        pre = str(params.get('pre', '') or '').strip()
        base_url = str(params.get('u', '') or '').strip()
        if not ip:
            return {'error': '缺少代理IP参数: ip'}
        if not base_url:
            return {'error': '缺少播放URL参数: u'}
        try:
            base_decoded = urllib.parse.unquote(base_url)
        except Exception:
            base_decoded = base_url
        others = {}
        for k, v in params.items():
            if k and k not in RESERVED:
                others[k] = v
        target_url = base_decoded
        if others:
            qp = ['%s=%s' % (k, urllib.parse.quote_plus(str(v), safe=':/,'))
                  for k, v in others.items()]
            target_url += ('&' if '?' in target_url else '?') + '&'.join(qp)
        enc = ['ip=' + urllib.parse.quote(ip, safe='')]
        if pre:
            enc.append('pre=' + urllib.parse.quote(pre, safe=''))
        enc.append('u=' + urllib.parse.quote(base_url, safe=''))
        for k, v in others.items():
            enc.append('%s=%s' % (k, urllib.parse.quote_plus(str(v), safe='')))
        return {'url': '%s?%s' % (self.address, '&'.join(enc)),
                'socks5': ip, 'm3u8_url': target_url}

    # ---------- 取流 ----------
    def proxy(self, url, headers):
        socket.getaddrinfo = _getaddrinfo_ipv4_only
        try:
            qs = urllib.parse.parse_qs(urllib.parse.urlparse(url).query,
                                        keep_blank_values=True)
            ip = qs.get('ip', [''])[0]
            pre = qs.get('pre', [''])[0]
            base_url = qs.get('u', [''])[0]
            if not ip or not base_url:
                return self._err('缺少必要参数', 400)
            target = urllib.parse.unquote(base_url)
            others = {}
            for k, values in qs.items():
                if k and k not in RESERVED and values:
                    others[k] = urllib.parse.unquote(values[0])
            if others:
                qp = ['%s=%s' % (k, urllib.parse.quote_plus(v, safe=':/,'))
                      for k, v in others.items()]
                target += ('&' if '?' in target else '?') + '&'.join(qp)
            is_m3u8 = '.m3u8' in target.lower()
            req_headers = {k: v for k, v in (headers or {}).items()
                           if k.lower() in ('range', 'user-agent')}
            r = self.session.get(target, proxies=self._proxies(ip, pre),
                                 headers=req_headers,
                                 timeout=(3 if is_m3u8 else 8),
                                 verify=False, stream=not is_m3u8)
            if r.status_code >= 400:
                return self._err('目标请求失败: %d' % r.status_code,
                                 r.status_code)
            if is_m3u8:
                all_params = {k: v[0] for k, v in qs.items() if k != 'url'}
                b = self._rewrite(r.text, target, ip, all_params).encode('utf-8')
                h = {'Content-Type': 'application/vnd.apple.mpegurl',
                     'Content-Length': str(len(b))}
                return b, self._common(h, r.status_code)
            h = {'Content-Type': r.headers.get('Content-Type', 'video/mp2t')}
            for k, v in r.headers.items():
                if k.lower() in ('content-length', 'content-range',
                                 'transfer-encoding'):
                    h[k] = v
            return r.iter_content(chunk_size=8192), self._common(h, r.status_code)
        except Exception as e:
            return self._err(str(e), 500)
        finally:
            socket.getaddrinfo = _original_getaddrinfo

    def _rewrite(self, content, base_url, ip, original_params):
        if not content.strip():
            return content
        parts_url = urllib.parse.urlparse(base_url)
        base_dir = base_url.rsplit('/', 1)[0] + '/'
        base_root = '%s://%s' % (parts_url.scheme, parts_url.netloc)
        lines = []
        for raw in content.splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith('#'):
                if line.upper().startswith('#EXT-X-KEY') and 'URI="' in line:
                    segs = line.split(',')
                    new_segs = []
                    for seg in segs:
                        if seg.upper().startswith('URI='):
                            uri = seg[4:].strip().strip('"')
                            absu = (base_root + uri if uri.startswith('/')
                                    else urllib.parse.urljoin(base_dir, uri)
                                    if not uri.startswith('http') else uri)
                            new_segs.append('URI="%s"' % self._purl(
                                ip, absu, original_params))
                        else:
                            new_segs.append(seg)
                    lines.append(','.join(new_segs))
                else:
                    lines.append(line)
                continue
            full = (base_root + line if line.startswith('/')
                    else urllib.parse.urljoin(base_dir, line)
                    if not line.startswith('http') else line)
            lines.append(self._purl(ip, full, original_params))
        return '\n'.join(lines)

    def _purl(self, ip, abs_url, original_params):
        parts = ['ip=' + urllib.parse.quote(ip)]
        if original_params.get('pre'):
            parts.append('pre=' + urllib.parse.quote(
                str(original_params['pre']), safe=''))
        parts.append('u=' + urllib.parse.quote_plus(abs_url, safe=''))
        for k, v in original_params.items():
            if k not in RESERVED:
                parts.append('%s=%s' % (k, urllib.parse.quote_plus(str(v), safe='')))
        return '%s?%s' % (self.address, '&'.join(parts))

    @staticmethod
    def _common(headers, status_code):
        headers.update({'Access-Control-Allow-Origin': '*',
                        'X-Proxy-Status-Code': str(status_code)})
        return headers

    def _err(self, msg, status_code=500):
        b = ('[Error %d] %s' % (status_code, msg)).encode('utf-8')
        return b, self._common({'Content-Type': 'text/plain',
                                'Content-Length': str(len(b))}, status_code)

    def stop(self):
        try:
            self.session.close()
        except Exception:
            pass
        if self._chain is not None:
            self._chain.close()
            self._chain = None
            self._chain_key = None
