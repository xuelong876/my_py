	=============================================
	Python 3 标准库速查表（完整版·每行带注释）
	=============================================
	【基础内置模块（无需import）】
    # 数据类型：int, float, str, list, tuple, dict, set, bool, None
    
	# 内置函数：
	  print(), input(), len(), type(), isinstance(), dir(), help()  urllib()
	  max(), min(), sum(), sorted(), reversed(), enumerate(), zip()
	  map(), filter(), any(), all(), open(), range(), round(), abs()
	  eval(), exec(), globals(), locals(), hash(), id(), ord(), chr()
	  
	====================
	一、内置函数（无需 import）
	====================
	# 输入输出
		print(*values, sep=' ', end='\n')  # 打印输出，可设置分隔符/结尾符
		input(prompt=None)                 # 读取控制台输入

	# 类型与判断
		len(obj)                           # 获取对象长度（元素个数）
		type(obj)                          # 返回对象的类型
		isinstance(obj, classinfo)         # 判断对象是否属于指定类型（推荐）
		issubclass(class, classinfo)       # 判断一个类是否是另一个类的子类
		dir(obj)                           # 查看对象的所有属性和方法
		help(obj)                          # 查看对象的帮助文档
		id(obj)                            # 返回对象的内存地址
		hash(obj)                          # 返回对象的哈希值
		bool(obj)                          # 转换为布尔值
		int(x, base=10)                    # 转换为整数，可指定进制
		float(x)                           # 转换为浮点数
		str(obj)                           # 转换为字符串
		list(iterable)                     # 转换为列表
		tuple(iterable)                    # 转换为元组
		dict(**kwargs)                     # 创建字典
		set(iterable)                      # 转换为集合
		frozenset(iterable)                # 转换为不可变集合

	# 数学计算
		abs(x)                             # 返回绝对值
		round(number, ndigits=None)         # 四舍五入，可指定小数位数
		max(*args)                         # 返回最大值
		min(*args)                         # 返回最小值
		sum(iterable, start=0)              # 求和，可设置初始值
		pow(base, exp, mod=None)            # 求幂运算，可带取模
		divmod(a, b)                       # 返回商和余数组成的元组

	# 序列与迭代
		range(start, stop, step)           # 生成整数序列
		enumerate(iterable, start=0)       # 返回索引+元素对
		zip(*iterables)                    # 打包多个可迭代对象
		sorted(iterable, key=None, reverse=False)  # 排序，返回新列表
		reversed(seq)                      # 反转序列，返回迭代器
		all(iterable)                      # 所有元素为True则返回True
		any(iterable)                      # 任一元素为True则返回True
		map(function, iterable)             # 对每个元素执行函数
		filter(function, iterable)          # 按条件过滤元素
		iter(iterable)                     # 获取迭代器
		next(iterator)                     # 获取迭代器下一个元素

	# 作用域
		globals()                          # 返回全局命名空间字典
		locals()                           # 返回局部命名空间字典
		vars(obj)                          # 返回对象的__dict__属性

	# 字符编码
		ord(c)                             # 字符→ASCII/Unicode编码
		chr(i)                             # 编码→对应字符
		repr(obj)                          # 返回对象的官方字符串表示
		ascii(obj)                         # 返回ASCII安全的表示

	# 文件操作
		open(file, mode='r', encoding=None) # 打开文件，返回文件对象

	====================
	二、文件与路径操作
	====================
	# os 模块：系统、路径、目录、文件
		import os
		os.getcwd()                 # 获取当前工作目录
		os.chdir(path)              # 切换工作目录
		os.listdir(path='.')        # 列出目录下所有文件/文件夹
		os.mkdir(path)              # 创建单层目录
		os.makedirs(path, exist_ok=True) # 递归创建目录，已存在不报错
		os.remove(path)             # 删除文件
		os.rmdir(path)              # 删除空目录
		os.rename(src, dst)         # 重命名/移动文件/目录
		os.path.exists(path)        # 判断路径是否存在
		os.path.isfile(path)        # 判断是否为文件
		os.path.isdir(path)         # 判断是否为目录
		os.path.abspath(path)       # 获取绝对路径
		os.path.basename(path)      # 获取文件名（含后缀）
		os.path.dirname(path)       # 获取目录部分
		os.path.join(a, *paths)     # 拼接路径（跨平台）
		os.path.splitext(path)      # 分割文件名与后缀
		os.path.getsize(path)       # 获取文件大小（字节）
		os.environ                  # 获取系统环境变量
		os.system(command)          # 执行系统命令

	# shutil 模块：高级文件操作
		import shutil
		shutil.copy(src, dst)        # 复制文件（不复制元数据）
		shutil.copy2(src, dst)       # 复制文件+保留元数据
		shutil.copytree(src, dst)   # 复制整个目录
		shutil.move(src, dst)        # 移动/重命名
		shutil.rmtree(path)          # 递归删除目录（非空也可删）
		shutil.make_archive()        # 打包压缩文件
		shutil.unpack_archive()      # 解压文件

	# pathlib 模块：面向对象路径（推荐）
		from pathlib import Path
		p = Path('.')                # 创建当前路径对象
		p / 'dir' / 'file.txt'       # 路径拼接（优雅）
		p.exists()                   # 路径是否存在
		p.is_file()                  # 是否是文件
		p.is_dir()                   # 是否是目录
		p.iterdir()                  # 遍历目录内容
		p.glob('*.py')               # 匹配当前目录py文件
		p.rglob('**/*.py')           # 递归匹配所有子目录py文件
		p.mkdir(exist_ok=True)       # 创建目录
		p.unlink()                   # 删除文件
		p.rmdir()                    # 删除空目录
		p.read_text(encoding='utf-8') # 读取文本文件
		p.write_text(s, encoding='utf-8') # 写入文本文件

	# 文件读写标准写法
		with open('a.txt', 'r', encoding='utf-8') as f:
		    f.read()                 # 读取全部内容
		    f.readline()             # 读取一行
		    f.readlines()            # 读取所有行（列表）

		with open('a.txt', 'w', encoding='utf-8') as f:
		    f.write(s)               # 写入字符串
		    f.writelines(lines)      # 写入多行（列表）

		# 文件打开模式说明
		# r 只读 w 覆盖写 a 追加
		# r+ 读写 w+ 读写清空 a+ 读写追加
		# b 二进制 t 文本模式

	====================
	三、字符串与正则表达式
	====================
	# 字符串常用方法
		s.strip()                    # 去除两端空白
		s.lstrip()                   # 去除左边空白 s.lstrip("x")表示去除左边的'x'
		s.rstrip()                   # 去除右边空白
		s.split(sep=None)            # 按分隔符分割成列表
		s.rsplit(sep=None,maxsplit=-1) #从右侧分割字符串， -1表示无限次
		s.splitlines()               # 按换行符分割
		s.join(iterable)             # 用字符串连接可迭代对象
		s.replace(old, new)          # 替换子串
		s.upper()                    # 转大写
		s.lower()                    # 转小写
		s.capitalize()               # 首字母大写
		s.title()                    # 每个单词首字母大写
		s.startswith(prefix)         # 是否以指定前缀开头
		s.endswith(suffix)           # 是否以指定后缀结尾
		s.find(sub)                  # 查找子串，返回索引（找不到-1）
		s.index(sub)                 # 查找子串，找不到抛异常
		s.count(sub)                 # 统计子串出现次数
		s.isdigit()                  # 是否全为数字
		s.isalpha()                  # 是否全为字母
		s.isalnum()                  # 是否字母/数字
		s.isspace()                  # 是否空白字符
		s.center(width)              # 居中显示
		s.ljust(width)               # 左对齐
		s.rjust(width)               # 右对齐
		s.zfill(width)               # 前面补0
		s.format()                   # 字符串格式化
		f"{x} {y}"                   # f-string格式化（推荐）

	# re 正则模块
		import re
		re.match(pattern, string)    # 从头开始匹配
		re.search(pattern, string)   # 任意位置匹配
		re.findall(pattern, string)  # 返回所有匹配结果（列表）
		re.finditer(pattern, string) # 返回匹配迭代器
		re.sub(pattern, repl, string) # 替换匹配内容
		re.split(pattern, string)    # 正则分割
		re.compile(pattern)          # 预编译正则（提速）

		# 常用正则符号
		# \d 数字 \D 非数字
		# \w 字母数字下划线 \W 相反
		# \s 空白 \S 非空白
		# . 任意字符 ^开头 $结尾
		# * 0次或多次 +1次或多次 ?0或1次
		# {n} 精确n次 {n,}至少n次 {n,m}n-m次
		# [] 字符集 [^] 排除字符集
		# | 或 () 分组

	====================
	四、日期与时间
	====================
	# datetime 模块
		from datetime import datetime, date, time, timedelta
		datetime.now()               # 获取当前日期时间
		datetime.utcnow()            # 获取UTC时间
		datetime(2026,4,6,12,0,0)    # 手动创建日期时间
		dt.year, dt.month, dt.day    # 获取年、月、日
		dt.hour, dt.minute, dt.second # 获取时、分、秒
		dt.timestamp()               # 转时间戳
		dt.strftime("%Y-%m-%d %H:%M:%S") # 日期→字符串
		datetime.strptime(s, "%Y-%m-%d") # 字符串→日期
		date.today()                 # 获取当前日期
		time(10,30,0)                # 创建时间对象
		timedelta(days=1, hours=2)    # 时间差对象
		dt1 - dt2                    # 计算两个时间差

	# time 模块
		import time
		time.time()                  # 获取当前时间戳（秒）
		time.ctime()                 # 获取可读时间字符串
		time.localtime()             # 本地时间结构体
		time.gmtime()                # UTC时间结构体
		time.sleep(secs)             # 程序休眠指定秒数
		time.strftime()               # 时间格式化
		time.strptime()               # 字符串转时间

	# calendar 模块
		import calendar
		calendar.month(2026,4)       # 打印指定月份日历
		calendar.isleap(2026)        # 判断是否闰年
		calendar.weekday(2026,4,6)   # 返回星期几（0=周一）

	====================
	五、数据结构增强
	====================
	# collections 模块
		from collections import defaultdict, OrderedDict, Counter, deque, namedtuple
		defaultdict(lambda:0)        # 带默认值的字典，键不存在不报错
		Counter(iterable).most_common(n) # 计数统计，取前n个
		deque(maxlen=None)           # 双端队列，头尾操作极快
		deque.append()               # 右侧添加
		deque.appendleft()           # 左侧添加
		deque.pop()                  # 右侧弹出
		deque.popleft()              # 左侧弹出
		namedtuple('Point',['x','y']) # 命名元组，可读性更强
		OrderedDict()                # 有序字典（3.7后普通dict也有序）

	# itertools 迭代器工具
		import itertools
		itertools.count()            # 无限计数
		itertools.cycle()            # 无限循环
		itertools.repeat(obj)        # 重复元素
		itertools.chain()            # 合并多个迭代器
		itertools.islice()           # 迭代器切片
		itertools.product()           # 笛卡尔积
		itertools.permutations()      # 排列
		itertools.combinations()      # 组合

	====================
	六、数学与随机数
	====================
	# math 数学函数
		import math
		math.pi                      # 圆周率常量
		math.e                       # 自然常数
		math.sqrt(x)                 # 平方根
		math.pow(x,y)                # x的y次方
		math.exp(x)                  # e的x次方
		math.log(x)                  # 自然对数
		math.log10(x)                # 以10为底对数
		math.sin(x)                  # 正弦（弧度）
		math.cos(x)                  # 余弦
		math.tan(x)                  # 正切
		math.floor(x)                # 向下取整
		math.ceil(x)                 # 向上取整
		math.fabs(x)                 # 浮点数绝对值
		math.factorial(n)            # 阶乘
		math.gcd(a,b)                # 最大公约数

	# random 随机数
		import random
		random.random()              # 0~1随机浮点数
		random.uniform(a,b)           # a~b随机浮点数
		random.randint(a,b)           # a~b随机整数（包含）
		random.randrange(start,stop)  # 指定范围随机整数
		random.choice(seq)            # 随机选一个元素
		random.choices(pop,k=1)       # 随机选k个（可重复）
		random.sample(pop,k)          # 随机选k个（不重复）
		random.shuffle(lst)           # 打乱列表顺序
		random.seed(n)                # 设置随机种子（可复现）

	# statistics 统计
		import statistics
		statistics.mean(data)         # 平均值
		statistics.median(data)       # 中位数
		statistics.mode(data)         # 众数
		statistics.stdev(data)        # 标准差
		statistics.variance(data)     # 方差

	# decimal 高精度小数
		from decimal import Decimal, getcontext
		getcontext().prec = 50        # 设置精度
		Decimal('0.1')+Decimal('0.2') # 精确计算，无浮点误差

	====================
	七、系统与进程
	====================
	# sys 系统参数
		import sys
		sys.argv                     # 命令行参数列表
		sys.version                  # Python版本
		sys.platform                 # 系统平台
		sys.path                     # 模块搜索路径
		sys.exit([arg])               # 退出程序
		sys.stdin                    # 标准输入
		sys.stdout                   # 标准输出
		sys.stderr                   # 标准错误
		sys.getsizeof(obj)            # 对象占用内存（字节）

	# platform 系统信息
		import platform
		platform.system()             # 系统名称（Windows/Linux）
		platform.node()               # 主机名
		platform.release()            # 系统版本
		platform.machine()            # 架构（x86/x64）
		platform.processor()          # 处理器
		platform.python_version()     # Python版本

	# subprocess 执行外部命令
		import subprocess
		subprocess.run(args)          # 执行命令，等待完成
		subprocess.call(args)         # 执行命令，返回状态码
		subprocess.check_output(args) # 执行命令，返回输出

	====================
	八、序列化与配置
	====================
	# json 序列化
		import json
		json.dumps(obj)               # 对象→JSON字符串
		json.loads(s)                 # JSON字符串→对象
		json.dump(obj, fp)            # 对象写入JSON文件
		json.load(fp)                 # 从JSON文件读取对象

	# pickle Python对象序列化
		import pickle
		pickle.dump(obj, file)        # 对象序列化到文件
		pickle.load(file)             # 从文件反序列化

	# configparser INI配置文件
		import configparser
		config = configparser.ConfigParser() # 创建配置对象
		config.read('config.ini')     # 读取配置文件
		config['section']['key']      # 获取配置值
		config.set('sec','key','val')  # 设置配置值

	# argparse 命令行参数
		import argparse
		parser = argparse.ArgumentParser() # 创建解析器
		parser.add_argument('--name')   # 添加参数
		args = parser.parse_args()     # 解析参数

	====================
	九、编码与加密
	====================
	# hashlib 哈希
		import hashlib
		hashlib.md5(b'data').hexdigest()    # MD5哈希
		hashlib.sha256(b'data').hexdigest() # SHA256哈希

	# base64 编码
		import base64
		base64.b64encode(b'data')      # Base64编码
		base64.b64decode(s)           # Base64解码

	# hmac 带密钥哈希
		import hmac
		h = hmac.new(key, msg, hashlib.sha256) # 生成HMAC
		h.hexdigest()                 # 转十六进制

	====================
	十、压缩与表格
	====================
	# zipfile ZIP压缩
		import zipfile
		with zipfile.ZipFile('a.zip','w') as zf:
		    zf.write('file.txt')       # 添加文件到压缩包
		with zipfile.ZipFile('a.zip','r') as zf:
		    zf.extractall()            # 解压全部

	# csv 表格文件
		import csv
		with open('a.csv','w') as f:
		    w = csv.writer(f)
		    w.writerow([1,2,3])       # 写入一行
		with open('a.csv','r') as f:
		    r = csv.reader(f)
		    for row in r: print(row)  # 读取每行

	====================
	十一、并发与日志
	====================
	# logging 日志
		import logging
		logging.basicConfig()         # 基础配置
		logging.debug('msg')          # 调试日志
		logging.info('msg')           # 信息日志
		logging.warning('msg')        # 警告日志
		logging.error('msg')          # 错误日志
		logging.critical('msg')       # 严重错误

	# threading 多线程
		import threading
		t = threading.Thread(target=func) # 创建线程
		t.start()                     # 启动线程
		t.join()                      # 等待线程结束

	# multiprocessing 多进程
		from multiprocessing import Process
		p = Process(target=func)      # 创建进程
		p.start()                     # 启动进程
		p.join()                      # 等待进程结束
	======================================================
	十二、urllib 网络请求
	======================================================
	# 模块总览
		urllib.request      发送 HTTP/HTTPS 请求
		urllib.parse        URL 解析、编码、拼接
		urllib.error        异常处理
		urllib.robotparser  解析 robots.txt 

	# urllib.request 所有方法 + 参数

		# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, cafile=None, capath=None, cadefault=False, context=None)
		   作用：打开 URL，发送请求
		   参数：
		     url        str/Request 对象  请求地址
		     data       bytes  提交数据，有则为 POST
		     timeout    int    超时秒数
		     context    ssl.SSLContext  SSL 配置

		   返回：HTTPResponse 对象

		# HTTPResponse 常用方法
			   resp.read()                  读取全部内容（bytes）
			   resp.read(n)                 读取 n 字节
			   resp.getcode() / status      状态码（200/404/500）
			   resp.getheaders()            所有响应头（列表）
			   resp.getheader(name)         获取指定响应头
			   resp.url                     实际 URL
			   resp.close()                 关闭连接

		# Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
		   作用：构造自定义请求
		   参数：
		     url        str    请求地址
		     data       bytes  POST 数据
		     headers    dict   请求头（User-Agent、Cookie 等）
		     method     str    GET/POST/PUT/DELETE

		   方法：
		   req.add_header(key, value)    添加请求头
		   req.get_method()              获取请求方法

		# build_opener(*handlers)
		   作用：创建自定义 opener
		   常用 Handler：
		   ProxyHandler          代理
		   HTTPCookieProcessor   Cookie
		   HTTPHandler           HTTP
		   HTTPSHandler          HTTPS

		# urlretrieve(url, filename=None, reporthook=None, data=None)
		   作用：下载文件
		   参数：
		     url         下载地址
		     filename    保存路径
		     reporthook  进度回调函数
		     data        POST 数据

	# urllib.parse 所有方法 + 参数

		# urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
		   作用：字典 → URL 查询字符串
		   参数：
		     query      dict  参数字典
		     encoding   str   编码（utf-8）

		# quote(string, safe='/', encoding=None, errors=None)
		   作用：字符串 URL 编码（中文/特殊字符）

		# unquote(string, encoding='utf-8', errors='replace')
		   作用：URL 解码

		# parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
		   作用：查询字符串 → 字典

		# urlparse(url, scheme='', allow_fragments=True)
		   作用：解析 URL
		   返回：scheme, netloc, path, params, query, fragment

		# urljoin(base, url, allow_fragments=True)
		   作用：基地址 + 相对地址 → 绝对地址

	# urllib.error 异常类

		# HTTPError（URLError 子类）
		   属性：code 状态码、reason 原因、headers 响应头

		# URLError
		   属性：reason 错误原因（网络失败、DNS 错误）

		捕获顺序：先 HTTPError → 再 URLError

	# 高频用法模板（带参数）

		# GET 请求
		with urlopen(url, timeout=10) as resp:
		    data = resp.read().decode('utf-8')

		# POST 请求
		data = urlencode({'key':'val'}).encode('utf-8')
		with urlopen(url, data=data, timeout=10) as resp:
		    ...

		# 带请求头
		req = Request(url, headers={'User-Agent':'...'}, method='GET')

		# 代理
		opener = build_opener(ProxyHandler({'http':'ip:port'}))

		# Cookie
		cj = CookieJar()
		opener = build_opener(HTTPCookieProcessor(cj))

		# SSL 无验证
		context = ssl._create_unverified_context()
		urlopen(url, context=context)

	# 核心参数速记
		urlopen：url, data, timeout, context
		Request：url, data, headers, method
		urlencode：query, encoding
		quote：string, encoding
		parse_qs：qs, encoding

	====================
	十三、其他常用工具
	====================
	# copy 拷贝
		import copy
		copy.copy(obj)                # 浅拷贝
		copy.deepcopy(obj)             # 深拷贝

	# glob 文件匹配
		import glob
		glob.glob('*.py')             # 匹配py文件
		glob.iglob('**/*.py',recursive=True) # 递归匹配

	# tempfile 临时文件
		import tempfile
		tempfile.NamedTemporaryFile() # 创建临时文件
		tempfile.TemporaryDirectory() # 创建临时目录

	# functools 工具
		import functools
		functools.lru_cache()         # 缓存装饰器
		functools.partial()           # 偏函数（固定参数）
		functools.reduce()            # 归约计算
	#bytes() 方法 把 字符串、数字、数组 转为 字节类型(bytes)
	   bytes([source], [encoding], [errors])
		参数：
		   source     数据源（字符串/列表/int/空）
		   encoding   编码（必填！如果 source 是字符串）
		   errors     错误处理（默认 strict）
	# decode()方法：字节 bytes  转 字符串 str
	   .decode(encoding="utf-8", errors="strict")
		参数：
		   encoding  编码格式
		      最常用：utf-8  其他：gbk、gb2312、ascii、iso-8859-1
	     errors    错误处理
		   strict      默认，报错
		   ignore      忽略无法解码的字符
		   replace     用�代替无法解码字符

	=============================================