"""
JSON站点配置处理脚本

功能：
1. 为不同源站点的JSON配置文件添加对应的Emoji前缀/后缀标识。
2. 修正站点API及外部资源路径为正确的相对路径格式。
3. 为特定源添加自定义站点配置。
"""

import os
import json

# ---------------------------- 文件映射与路径配置 ----------------------------
# 输入文件名到输出文件名的映射关系
INPUT_TO_OUTPUT_MAPPING = {
    "api.json": "xiaosa.json",   # 潇洒源
    "wex.json": "erxiao.json",   # 二小源
    "jsm.json": "pg.json"        # PG源
}

# 输入文件所在基础目录
INPUT_BASE_DIR = r"C:\C盘下载\Tvbox_json\sites_filter"
# 输出文件存放目录
OUTPUT_BASE_DIR = r"C:\C盘下载\Tvbox_json\out_json"

# ---------------------------- 站点处理函数 ----------------------------
def process_xiaosa_site(site: dict) -> dict:
    """
    处理潇洒源（原api.json）的单条站点记录。
    
    操作包括：
    - 修正api字段的相对路径
    - 修正ext字段的相对路径
    - 特殊处理哔哩合集的ext.json路径
    - 根据站点名称添加对应的Emoji标识
    """
    # --- 路径修正 ---
    # 处理api字段的相对路径
    api_value = site.get('api', '')
    if isinstance(api_value, str) and api_value.startswith('./'):
        api_filename = api_value.split("/")[-1]
        site["api"] = f"./xiaosa/{api_filename}"

    # 处理ext字段的相对路径
    ext_value = site.get('ext', '')
    if isinstance(ext_value, str) and ext_value.startswith('./'):
        print(f"潇洒源 - 修正外部文件路径：{ext_value}")
        ext_filename = ext_value.split("/")[-1]
        site["ext"] = f"./xiaosa/{ext_filename}"

    # 特殊处理哔哩合集的ext内嵌json路径
    if site.get("key") == "哔哩合集" and isinstance(site.get("ext"), dict):
        site["ext"]["json"] = "./xiaosa/哔哩合集.json"

    # --- 名称美化（添加Emoji）---
    original_name = site.get("name", "")
    if original_name == "豆瓣｜首页":
        site["name"] = "🏠豆瓣🚥潇洒👨"
    elif original_name == "配置｜中心":
        site["name"] = "⚙️配置中心🍅"
    elif original_name.startswith("哔哩"):
        site["name"] = f"🅱️{original_name}🍅"
    elif original_name.endswith("APP"):
        site["name"] = f"🐞{original_name}🍅"
    elif original_name.endswith("视频"):
        site["name"] = f"🎬{original_name}🍅"
    elif original_name.endswith("影视"):
        site["name"] = f"🎥{original_name}🍅"
    elif original_name.endswith(("4K", "网盘", "云盘")):
        site["name"] = f"☁{original_name}🍅"
    elif original_name.endswith("磁力"):
        site["name"] = f"🧲{original_name}🍅"
    elif original_name.endswith("搜索"):
        site["name"] = f"🔍 {original_name}🍅"
    else:
        site["name"] = f"🍅{original_name}🍅"

    return site


def process_erxiao_site(site: dict) -> dict:
    """
    处理二小源（原wex.json）的单条站点记录。
    """
    if site.get("key") == "Douban":
        site["name"] = "🏠豆瓣-王二小👨"
    return site


def process_pg_site(site: dict) -> dict:
    """
    处理PG源（原jsm.json）的单条站点记录。
    """
    original_name = site.get("name", "")
    if original_name == "豆瓣":
        site["name"] = "🏠豆瓣🚥PG👨"
    elif original_name == "网盘及彈幕配置":
        site["name"] = "⚙️网盘及彈幕配置👌"
    elif original_name.startswith("B站"):
        site["name"] = f"🅱️{original_name}👌"
    elif original_name.endswith(("磁力", "磁")):
        site["name"] = f"🧲{original_name}👌"
    elif original_name.startswith("分享") or original_name.endswith(("分享", "网盘", "搜索", "云搜")):
        site["name"] = f"☁{original_name}👌"
    else:
        site["name"] = f"👌{original_name}👌"
    return site


# ---------------------------- 主处理流程 ----------------------------
def process_all_files():
    """遍历所有文件对，执行读取、处理、写入操作。"""
    # 确保输出目录存在
    os.makedirs(OUTPUT_BASE_DIR, exist_ok=True)

    for input_filename, output_filename in INPUT_TO_OUTPUT_MAPPING.items():
        input_path = os.path.join(INPUT_BASE_DIR, input_filename)
        output_path = os.path.join(OUTPUT_BASE_DIR, output_filename)

        # 读取原始JSON数据
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        processed_sites = []
        for site in data.get("sites", []):
            # 统一关闭自动换源
            site["changeable"] = 0

            # 根据输入文件选择对应的处理函数
            if input_filename == "api.json":
                processed = process_xiaosa_site(site)
            elif input_filename == "wex.json":
                processed = process_erxiao_site(site)
            elif input_filename == "jsm.json":
                processed = process_pg_site(site)
            else:
                processed = site  # 理论上不会进入此分支

            processed_sites.append(processed)

        # 为潇洒源追加额外的自定义站点
        if input_filename == "api.json":
            custom_site = {
                "key": "猎手影视",
                "name": "🏂猎手｜py🍅 ",
                "type": 3,
                "api": "./py/猎手影视.py",
                "searchable": 1,
                "changeable": 0,
                "quickSearch": 1,
                "filterable": 1
            }
            processed_sites.append(custom_site)
            #修改spider 为网络
            data["spider"]="https://qist.ugigc.dpdns.org/xiaosa/spider.jar"
        #为PG源更改网络爬虫包
        if input_filename == "jsm.json":
            data["spider"]="https://www.252035.xyz/p/pg.jar"


        # 更新数据并写入文件
        data["sites"] = processed_sites
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"✅ 处理完成：{input_filename} → {output_filename}")


if __name__ == "__main__":
    process_all_files()