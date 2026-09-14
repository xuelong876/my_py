import requests
import json
import os
from typing import List, Dict

# 配置区 - 方便统一修改配置
CONFIG = {
    "xiaosa_json_url": "https://raw.githubusercontent.com/qist/tvbox/refs/heads/master/xiaosa/api.json",
    "wallpaper": "http://饭太硬.top/深色壁纸/api.php",
    "logo": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/pg.gif",
    "spider": "https://gitee.com/xuelong88/xiaosa_box/raw/master/spider.jar",
    "output_path": r"C:\C盘下载\Tvbox_json\xiaosa.json",
    "exclude_names": [
        "短剧", "123", "戏曲", "本地", "抖音", "推送", "预告", "动漫", 
        "看球", "DJ", "体育", "听书", "FM", "儿童", "童趣", "课堂", 
        "教育", "急救", "养生", "知识"
    ],
    "add_site":[
         {
            "key": "腾讯视频",
            "name": "🎬腾讯｜视频🍅",
            "type": 3,
            "api": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/drpy2.min.js",
            "ext": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/腾讯视频.js",
            "changeable": 0
        },
        {
            "key": "优酷视频",
            "name": "🎬优酷｜视频🍅",
            "type": 3,
            "api": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master//xiaosa/drpy2.min.js",
            "ext": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/优酷视频.js",
            "changeable": 0
        },
        {
            "key": "芒果视频",
            "name": "🎬芒果｜视频🍅",
            "type": 3,
            "api": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/drpy2.min.js",
            "ext": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/芒果视频.js",
            "changeable": 0
        },
        {
            "key": "爱奇艺",
            "name": "🎬爱奇艺｜视频🍅",
            "type": 3,
            "api": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/drpy2.min.js",
            "ext": "https://raw.giteeusercontent.com/xuelong88/xiaosa_box/raw/master/xiaosa/爱奇艺.js",
            "changeable": 0
        },
            {
            "key": "猎手影视",
            "name": "🏂猎手｜py🍅 ",
            "type": 3,
            "api": "./py/猎手影视.py",
            "searchable": 1,
            "changeable": 0,
            "quickSearch": 1,
            "filterable": 1
        }
    ],
    "lives": [
        {
            "name": "移动8m",
            "type": 0,
            "url": "https://gh-proxy.com/https://raw.githubusercontent.com/xuelong876/mybox_PG/refs/heads/main/live/YD8M.m3u",
            "playerType": 2,
            "ua": "okhttp/3.12.13",
            "logo": "https://cdn.jsdelivr.net/gh/xuelong876/channal_logo2@master/{name}.png",
            "epg": "http://cdn.1678520.xyz/epg/?ch={name}&date={date}"
        },
        {
            "name": "刺桐自营",
            "type": 0,
            "url": "https://www.cttv.vip/ys/json/ctzb.txt",
            "playerType": 2,
            "ua": "okhttp/3.12.13",
            "logo": "https://cdn.jsdelivr.net/gh/xuelong876/channal_logo2@master/{name}.png",
            "epg": "http://cdn.1678520.xyz/epg/?ch={name}&date={date}"
        }
    ]

}

# --- 名称美化（添加Emoji）---
def add_emoji_to_name(name: str) -> str:
    """添加Emoji到名称
    匹配规则：按列表顺序依次判断，命中第一条即返回
    """
    # 规则配置：(匹配类型, 匹配值, 结果模板/固定返回文本)
    # type: "startswith"前缀 / "endswith"后缀
    rules = [
        ("startswith", "豆瓣", "🏠豆瓣 • 潇洒👨"),
        ("startswith", "配置", "⚙️配置 • 中心🍅"),
        ("startswith", "哔哩", "🅱️{name}🍅"),
        ("endswith", "APP", "🐞{name}🍅"),
        ("endswith", "视频", "🎬{name}🍅"),
        ("endswith", "影视", "🎥{name}🍅"),
        ("endswith", ("4K", "网盘", "云盘"), "☁{name}🍅"),
        ("endswith", "磁力", "🧲{name}🍅"),
        ("endswith", "搜索", "🔍 {name}🍅"),
    ]

    # 入参校验
    if not isinstance(name, str):
        return ""

    for match_type, match_val, template in rules:
        if match_type == "startswith":
            if name.startswith(match_val):
                if "{name}" in template:
                    return template.format(name=name)
                return template
        elif match_type == "endswith":
            # 支持多个后缀匹配
            if isinstance(match_val, tuple):
                if any(name.endswith(val) for val in match_val):
                    return template.format(name=name)
            elif name.endswith(match_val):
                return template.format(name=name)

    # 默认规则
    return f"🍅{name}🍅"

# 主程序 修改json文件
def main():
    """
    1；读取指定接口地址JSON 文件，转换为py字典
    2；修改壁纸和logo，jar地址
    3；修改lives键的值为指定路径
    4；遍历字典中键“sites"的值，排除包含exclude_names中的站点名称的值，
    5；对各站点中的name添加emoji名称美化
    6；修改后的json文件，保存为指定路径
    """
    try:
        # 获取在线json内容，增加错误处理
        response = requests.get(CONFIG["xiaosa_json_url"], timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        
        # 修改壁纸和logo，jar地址
        data["wallpaper"] = CONFIG["wallpaper"]
        data["logo"] = CONFIG["logo"]
        data["spider"] = CONFIG["spider"]
        
        # 修改lives键的值为指定路径
        data["lives"] = CONFIG["lives"]
        
        # 遍历字典中键"sites"的值，排除包含exclude_names中的站点名称的值
        # any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
        # 元素除了是 0、空、FALSE 外都算 TRUE。
        if "sites" in data:
            data["sites"] = [
                site for site in data["sites"] 
                if not any(
                    exclude_name in site.get("name", "") 
                    for exclude_name in CONFIG["exclude_names"]
                )
            ]

            # 对各站点中的name添加emoji名称美化
            for site in data["sites"]:
                site["name"] = add_emoji_to_name(site["name"])
                # 关闭自动换源
                site["changeable"] = 0
        #添加站点
        data["sites"].extend(CONFIG["add_site"])


        
        # 确保输出目录存在
        output_dir = os.path.dirname(CONFIG["output_path"])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 保存修改后的json文件
        with open(CONFIG["output_path"], "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"处理完成，文件已保存到：{CONFIG['output_path']}")
    
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误：{str(e)}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误：{str(e)}")
    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")

if __name__ == "__main__":
    main()
