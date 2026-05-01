import time  # 时间模块
from selenium import webdriver  # 自动化模块
from selenium.webdriver.edge.options import Options  # 浏览器设置模块
import requests  # 网络请求库  HTTP服务库
import json  # JSON库
import re  # 正则
from selenium.webdriver.edge.service import Service  # edgedriver服务

# TODO 用网络空间搜索河南陕西的酒店源端口IP  用自动化工具selenium 爬虫 抓取正则匹配直播源地址并整理 写入TXT 文本

# TODO 创建 WebDriver 对象，指明使用edge浏览器驱动  环境变量已经配置好了pcharm不识别 所以指定浏览器驱动路径
#driver = webdriver.edge(service=Service(r'C:\python\Scripts\msedgedriver.exe'))

# 定义河南 陕西 空间搜索fofa 以获取 酒店源网络地址端口
henan = "https://fofa.info/result?qbase64=ImlwdHYvbGl2ZS96aF9jbi5qcyIgJiYgY291bnRyeT0iQ04iICYmIHJlZ2lvbj0i5rKz5Y2XIg%3D%3D"  # 河南


# 定义一个处理URL的函数
def process_url(url):
    # 设置edge浏览器的选项，包括无头模式和安全选项
    edge_options = Options()
    #设置Edge浏览器二进制路径
    edge_options.binary_location=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    # edge_options.add_argument('--headless')  # 无头模式，不显示浏览器界面
    edge_options.add_argument('--no-sandbox')  # 忽略沙箱环境
    edge_options.add_argument('--disable-dev-shm-usage')  # 禁用/dev/shm的使用
   # 添加以下参数禁用媒体组件，消除GetPackagesByPackageFamily错误
    edge_options.add_argument('--disable-media-source')
    edge_options.add_argument('--disable-software-rasterizer')
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # 添加伪装UA，绕过反爬检测
    edge_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')

    
    # 创建一个edge WebDriver实例
    driver = webdriver.Edge(
        service=Service(r'C:\python\Scripts\msedgedriver.exe'),  # 定义浏览器驱动路径
        options=edge_options,
    )
    # 使用WebDriver访问网页
    driver.get("https://fofa.info/")  # 将网址替换为你要访问的网页地址

    print(f"请在打开的浏览器中登录fofa账号，登录完成后程序会继续执行...")

    time.sleep(20)  # 等待页面加载
    driver.get(url)
    # 获取网页内容
    page_content = driver.page_source
    #print(page_content)

    # 关闭WebDriver
    #driver.quit()

    # 使用正则表达式查找所有符合条件的网址
    pattern = r"http://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+"  # 匹配IP地址和端口的格式 如http://8.8.8.8:8888
    urls_all = re.findall(pattern, page_content)  # 返回匹配项（pattern ip地址端口）的列表
    urls = list(set(urls_all))  # 去重得到唯一的URL列表  set（集合）具有去重功能
    print(urls)
    results = []  # 新建空列表，用于暂存直播源
    # 遍历网址列表，获取JSON文件并解析
    for url in urls:
        try:  # 可能出现的异常
            # 构造JSON文件的URL并发送GET请求获取数据
            # TODO 可修改直播源链接格式
            json_url = f"{url}/iptv/live/1000.json?key=txiptv"  # 拼接链接
            response = requests.get(json_url, timeout=10)  # 获取链接网址数据 等待3秒
            print(response)
            json_data = response.json()  # 解析网站返回的json 数据为python对象 （通常为字典或列表）

            # 解析JSON文件，获取name和url字段
            for item in json_data['data']:
                if isinstance(
                    item, dict
                ):  # 如果item 是一个字典，isinstance() 函数用于检查一个对象是否是一个已知的类型，或者来自一个继承自那种类型的子类
                    name = item.get('name')  # 获取字典键名‘name’ 对于的数据value 也就是节目名称
                    urlx = item.get('url')  # 获取节目地址
                    urld = f"{url}{urlx}"  # 酒店ip地址端口和节目源地址

                    # 清理名称中的特定文字
                    name = name.replace("中央", "CCTV")  # 替换‘中央’为‘CCTV'
                    name = name.replace("高清", "")  # 替换’高清’ 为空  去除高清
                    name = name.replace("HD", "")
                    name = name.replace("标清", "")
                    name = name.replace("频道", "")
                    name = name.replace("-", "")
                    name = name.replace(" ", "")
                    name = name.replace("PLUS", "+")
                    name = name.replace("(", "")
                    name = name.replace(")", "")
                    name = name.replace("CCTV1综合", "CCTV1")
                    name = name.replace("CCTV2财经", "CCTV2")
                    name = name.replace("CCTV3综艺", "CCTV3")
                    name = name.replace("CCTV4国际", "CCTV4")
                    name = name.replace("CCTV4中文国际", "CCTV4")
                    name = name.replace("CCTV5体育", "CCTV5")
                    name = name.replace("CCTV6电影", "CCTV6")
                    name = name.replace("CCTV7军事", "CCTV7")
                    name = name.replace("CCTV7军农", "CCTV7")
                    name = name.replace("CCTV7国防军事", "CCTV7")
                    name = name.replace("CCTV8电视剧", "CCTV8")
                    name = name.replace("CCTV9记录", "CCTV9")
                    name = name.replace("CCTV9纪录", "CCTV9")
                    name = name.replace("CCTV10科教", "CCTV10")
                    name = name.replace("CCTV11戏曲", "CCTV11")
                    name = name.replace("CCTV12社会与法", "CCTV12")
                    name = name.replace("CCTV13新闻", "CCTV13")
                    name = name.replace("CCTV新闻", "CCTV13")
                    name = name.replace("CCTV14少儿", "CCTV14")
                    name = name.replace("CCTV15音乐", "CCTV15")
                    name = name.replace("CCTV16奥林匹克", "CCTV16")
                    name = name.replace("CCTV17农业农村", "CCTV17")
                    name = name.replace("CCTV5+体育赛视", "CCTV5+")
                    name = name.replace("CCTV5+体育赛事", "CCTV5+")

                    # 如果名称和URL存在，则添加到结果列表
                    if name and urlx:
                        results.append(f"{name},{urld}")
        # 捕获异常该别名为e,当你捕获 requests.exceptions.RequestException 时，你可以处理所有与 requests 请求相关的异常(超时，返回错误等）
        except requests.exceptions.RequestException as e:
            # 打印请求异常信息
            print(
                f"Failed to process JSON for URL {json_url}. Error: {str(e)}"
            )  # e 是一个异常对象，str() 转换为字符串
            continue  # 跳出此次循环
        except json.JSONDecodeError as e:  # 捕获json.JSONDecodeError异常并改名为‘e’
            # 打印JSON解析异常信息
            print(
                f"Failed to parse JSON for URL {url}. Error: {str(e)}"
            )  # e 是一个异常对象，str() 转换为字符串
            continue  # 跳出此次循环

    # 返回处理结果
    return results


# 定义一个保存结果的函数
def save_results(results, filename):
    # 将结果文本文件保存到C盘下载目录

    with open(
        f"C:/C盘下载/{filename}", "w", encoding="utf-8"
    ) as file:
        for result in results:
            file.write(result + "\n")
            print(result)  # 打印直播源


# 处理各个URL并保存结果到文件
# 处理第henan个URL
results_henan = process_url(henan)
save_results(results_henan, "henan.txt")

# 合并文件内容
file_contents = []  # 新建列表 存放合并后的直播源
file_paths = [
   
    "C:/C盘下载/henan.txt",
]  # 替换为实际的文件路径列表
for file_path in file_paths:  # 遍历文件路径
    # with是一个上下文管理器语句，用于打开一个文件并确保文件在使用后会被正确关闭
    with open(file_path, 'r', encoding="utf-8") as file:  # 以只读的方式打开指定路径文件
        content = file.read()  # 逐行读取文件
        file_contents.append(content)  # 追加行到列表结尾
# 写入合并后的文件到桌面
with open("C:/C盘下载/IPTV.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))
