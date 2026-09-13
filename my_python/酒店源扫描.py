#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
酒店IPTV直播源自动维护脚本
- 使用360 Quake API搜索特定地区的IPTV源
- 流量验真：必须拉取16KB有效数据流
- 本地缓存自检，有效则直接使用
- 找到首个有效IP及其所有频道后保存并退出
"""

import os
import re
import json
import requests
from typing import List, Dict, Tuple, Optional

# ==================== 配置区域（易于修改）====================
# Quake API 密钥（请设置环境变量 QUAKE_API_KEY 或直接填写）
QUAKE_API_KEY = os.environ.get("QUAKE_API_KEY", "your_api_key_here")

# 查询语句模板（可根据需要修改省份、城市、端口等）
QUERY_TEMPLATE = (
    'iptv/live/zh_cn.js AND province_cn: "广东" AND port: "9901" AND city_cn: "梅州市"'
)

# 本地输出文件名
OUTPUT_M3U = "梅州.m3u"
OUTPUT_TXT = "梅州.txt"

# 验真参数
STREAM_CHUNK_SIZE = 16 * 1024  # 16KB
STREAM_TIMEOUT = 10  # 秒

# Quake API 请求配置
QUAKE_API_URL = "https://quake.360.net/api/v3/search/quake_service"
QUAKE_PAGE_SIZE = 10  # 每次搜索返回的数量
# ===========================================================


def test_stream_url(url: str) -> bool:
    """
    验真URL：使用stream=True模式，读取前16KB数据，长度>0则有效
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        with requests.get(url, stream=True, timeout=STREAM_TIMEOUT, headers=headers) as resp:
            if resp.status_code != 200:
                return False
            # 读取前16KB数据
            data = b""
            for chunk in resp.iter_content(chunk_size=STREAM_CHUNK_SIZE):
                data += chunk
                if len(data) >= STREAM_CHUNK_SIZE:
                    break
            return len(data) > 0
    except Exception:
        return False


def parse_local_m3u(filepath: str) -> Optional[List[Tuple[str, str]]]:
    """
    解析本地m3u文件，返回频道列表 [(name, url), ...]
    若文件不存在或解析失败返回None
    """
    if not os.path.exists(filepath):
        return None
    channels = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("#EXTINF:"):
                # 提取频道名： -1,频道名
                match = re.search(r"#EXTINF:-?\d+,\s*(.+)", line)
                if match:
                    name = match.group(1).strip()
                    # 下一行应为URL
                    if i + 1 < len(lines):
                        url = lines[i + 1].strip()
                        if url and not url.startswith("#"):
                            channels.append((name, url))
                i += 2
            else:
                i += 1
        return channels if channels else None
    except Exception:
        return None


def save_channels(channels: List[Tuple[str, str]], m3u_path: str, txt_path: str):
    """保存频道列表到m3u和txt文件"""
    # 保存M3U
    with open(m3u_path, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for name, url in channels:
            f.write(f'#EXTINF:-1,{name}\n{url}\n')
    # 保存TXT（格式：频道名,URL）
    with open(txt_path, "w", encoding="utf-8") as f:
        for name, url in channels:
            f.write(f"{name},{url}\n")
    print(f"✅ 已保存 {len(channels)} 个频道至 {m3u_path} 和 {txt_path}")


def search_quake(query: str, api_key: str) -> List[str]:
    """
    调用360 Quake API，返回IP:port列表（端口固定9901）
    """
    if not api_key or api_key == "your_api_key_here":
        print("❌ 请先设置 Quake API Key（环境变量 QUAKE_API_KEY 或直接修改脚本）")
        return []

    headers = {
        "Content-Type": "application/json",
        "X-QuakeToken": api_key
    }
    payload = {
        "query": query,
        "start": 0,
        "size": QUAKE_PAGE_SIZE,
        "latest": True
    }

    try:
        resp = requests.post(QUAKE_API_URL, json=payload, headers=headers, timeout=15)
        if resp.status_code != 200:
            print(f"❌ Quake API 错误: {resp.status_code} - {resp.text}")
            return []
        data = resp.json()
        if data.get("code") != 0:
            print(f"❌ Quake API 返回错误: {data.get('message')}")
            return []
        assets = data.get("data", [])
        ips = []
        for asset in assets:
            ip = asset.get("ip")
            port = asset.get("port")
            if ip and port == 9901:  # 确保端口匹配
                ips.append(f"{ip}:{port}")
        return ips
    except Exception as e:
        print(f"❌ Quake API 请求异常: {e}")
        return []


def parse_channel_js(js_content: str, base_url: str) -> List[Tuple[str, str]]:
    """
    从 zh_cn.js 内容中解析出频道名称和流URL。
    支持常见格式：
      - JSON对象 {"频道名": "http://..."}
      - 数组 [{"name":"CCTV1","url":"..."}, ...]
      - var channels = [...]; 包裹的JS对象
    返回 [(name, url), ...]
    """
    channels = []
    # 尝试直接解析JSON
    try:
        data = json.loads(js_content)
        if isinstance(data, dict):
            for name, url in data.items():
                if isinstance(url, str) and (url.startswith("http") or url.startswith("rtsp")):
                    channels.append((name, url))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    name = item.get("name") or item.get("channel") or item.get("title")
                    url = item.get("url") or item.get("stream") or item.get("path")
                    if name and url and (url.startswith("http") or url.startswith("rtsp")):
                        channels.append((name, url))
        if channels:
            return channels
    except json.JSONDecodeError:
        pass

    # 尝试提取 var xxx = {...} 或直接 {...}
    # 匹配大括号包围的JSON对象
    json_pattern = r'(\{.*\})'
    match = re.search(json_pattern, js_content, re.DOTALL)
    if match:
        try:
            obj = json.loads(match.group(1))
            if isinstance(obj, dict):
                for name, url in obj.items():
                    if isinstance(url, str) and (url.startswith("http") or url.startswith("rtsp")):
                        channels.append((name, url))
                if channels:
                    return channels
        except:
            pass

    # 通用正则：提取 "name":"xxx" 和 "url":"http://..." 配对
    # 查找类似 "channel_name":"http://..." 或 "name":"xxx","url":"..."
    pattern = r'(?:name|channel|title)[\s:]*["\']([^"\']+)[\'"][^}]*?(?:url|stream|path)[\s:]*["\'](https?://[^\s"\']+)[\'"]'
    matches = re.findall(pattern, js_content, re.IGNORECASE)
    for name, url in matches:
        channels.append((name.strip(), url))
    if channels:
        return channels

    # 最后降级：提取所有http/rtsp链接，用序号命名
    urls = re.findall(r'(https?://[^\s"\']+|rtsp://[^\s"\']+)', js_content)
    for idx, url in enumerate(urls, 1):
        channels.append((f"频道{idx}", url))

    return channels


def fetch_and_parse_channels(ip_port: str) -> Optional[List[Tuple[str, str]]]:
    """
    访问 http://IP:9901/iptv/live/zh_cn.js，解析频道列表
    成功返回列表，失败返回None
    """
    url = f"http://{ip_port}/iptv/live/zh_cn.js"
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return None
        js_content = resp.text
        base_url = f"http://{ip_port}"
        channels = parse_channel_js(js_content, base_url)
        if not channels:
            # 尝试补全相对路径URL
            full_channels = []
            for name, stream_url in channels:
                if stream_url.startswith("/"):
                    stream_url = base_url + stream_url
                full_channels.append((name, stream_url))
            return full_channels if full_channels else None
        return channels
    except Exception:
        return None


def main():
    print("=== 酒店IPTV直播源自动维护脚本 ===")

    # 1. 本地自检
    local_channels = parse_local_m3u(OUTPUT_M3U)
    if local_channels:
        print("📁 发现本地缓存文件，正在验真首个频道...")
        first_url = local_channels[0][1]
        if test_stream_url(first_url):
            print("✅ 本地缓存有效，直接使用现有文件")
            # 确保文件存在（可能只有m3u无txt，重新生成txt）
            save_channels(local_channels, OUTPUT_M3U, OUTPUT_TXT)
            return
        else:
            print("⚠️ 本地缓存失效，将搜索新源")

    # 2. 搜索Quake
    print(f"🔍 使用查询语句: {QUERY_TEMPLATE}")
    ip_list = search_quake(QUERY_TEMPLATE, QUAKE_API_KEY)
    if not ip_list:
        print("❌ 未从Quake获取到任何IP，请检查API Key或查询条件")
        return

    print(f"📡 获取到 {len(ip_list)} 个候选IP，开始验证...")

    for ip_port in ip_list:
        print(f"⚙️ 测试 {ip_port} ...")
        channels = fetch_and_parse_channels(ip_port)
        if not channels:
            print(f"   ⚠️ 无法解析频道列表")
            continue

        # 对第一个频道进行流量验真
        first_name, first_url = channels[0]
        print(f"   🧪 验真首个频道: {first_name} - {first_url[:60]}...")
        if test_stream_url(first_url):
            print(f"✅ 找到有效IP: {ip_port}，共 {len(channels)} 个频道")
            save_channels(channels, OUTPUT_M3U, OUTPUT_TXT)
            return
        else:
            print(f"   ❌ 流量验真失败（未能读取16KB数据）")

    print("❌ 所有候选IP均未通过流量验真，请尝试修改查询条件或稍后再试")


if __name__ == "__main__":
    main()