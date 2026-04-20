import requests
import os
import json
#本脚本用于下载并处理Tvbox_json站点的JSON文件，先下载API 接口JSON文件，在提取站点(txt文件），
#  筛选站点后保存到sites_filter(txt文件），过滤后的JSON文件在此目录

# ==================== 配置区域 ====================
# 接口列表
api_urls = [
    "https://qist.ugigc.dpdns.org/xiaosa/api.json",
    "https://9280.kstore.space/wex.json",
    "https://www.252035.xyz/p/jsm.json"
]

# 基础保存路径
BASE_SAVE_PATH = r"C:\C盘下载\Tvbox_json"
# 过滤后文件输出目录
FILTER_DIR_NAME = "sites_filter"
# ==================================================

# 初始化路径
FILTER_PATH = os.path.join(BASE_SAVE_PATH, FILTER_DIR_NAME)
os.makedirs(BASE_SAVE_PATH, exist_ok=True)
os.makedirs(FILTER_PATH, exist_ok=True)

def download_json_files():

    """下载所有远程JSON文件到本地"""
    #如果 存在api.json,wex.jaon,jsm.json 则跳过下载，返回文件已存在
      # 检查所有文件是否都已下载完成
    all_exists = True
    for url in api_urls:
        file_name = url.split("/")[-1]
        if not os.path.exists(os.path.join(BASE_SAVE_PATH, file_name)):
            all_exists = False
            break
    if all_exists:
        print("所有文件已存在，跳过下载")
        return

    print("=" * 40)
    print("第一步：正在下载 JSON 文件...")
    print("=" * 40)
    
    success_count = 0
    fail_count = 0
    
    for url in api_urls:
        try:
            file_name = url.split("/")[-1]
            file_path = os.path.join(BASE_SAVE_PATH, file_name)

            resp = requests.get(url, timeout=15)
            resp.raise_for_status()

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(resp.text)

            print(f"✅ 已保存：{file_name}")
            success_count += 1

        except Exception as e:
            print(f"❌ 下载失败 {url}：{str(e)}")
            fail_count += 1
    
    print(f"\n📊 下载完成：成功 {success_count} 个，失败 {fail_count} 个\n")

def extract_names_to_txt():
    """从下载的JSON中提取站点名称生成TXT文件"""
    print("=" * 40)
    print("第二步：正在提取 name 并生成 txt...")
    print("=" * 40)
    
    success_count = 0
    total_names = 0
    
    for file_name in os.listdir(BASE_SAVE_PATH):
        if not file_name.endswith(".json"):
            continue
            
        try:
            file_path = os.path.join(BASE_SAVE_PATH, file_name)
            txt_file = file_name.replace(".json", ".txt")
            txt_path = os.path.join(BASE_SAVE_PATH, txt_file)

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            names = []
            if "sites" in data and isinstance(data["sites"], list):
                for item in data["sites"]:
                    if "name" in item and item["name"]:
                        names.append(item["name"])

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(names))

            print(f"📄 已生成：{txt_file} （共{len(names)}条）")
            success_count += 1
            total_names += len(names)

        except Exception as e:
            print(f"❌ 处理失败 {file_name}：{str(e)}")
    
    print(f"\n📊 提取完成：处理 {success_count} 个文件，共提取 {total_names} 个站点名称\n")

def generate_filtered_json():
    """根据过滤后的TXT生成精简JSON"""
    print("=" * 40)
    print("第三步：正在根据过滤列表生成精简JSON...")
    print("=" * 40)
    
    success_count = 0
    total_original = 0
    total_kept = 0
    
    # 自动扫描所有JSON文件，不需要硬编码
    for file_name in os.listdir(BASE_SAVE_PATH):
        if not file_name.endswith(".json"):
            continue
            
        json_name = file_name
        txt_name = file_name.replace(".json", ".txt")
        
        try:
            # 路径定义
            json_path = os.path.join(BASE_SAVE_PATH, json_name)
            txt_path = os.path.join(FILTER_PATH, txt_name)
            out_json_path = os.path.join(FILTER_PATH, json_name)
            
            # 检查过滤txt是否存在
            if not os.path.exists(txt_path):
                print(f"⚠️ 跳过 {json_name}：过滤文件 {txt_name} 不存在于 {FILTER_PATH}")
                continue

            # 读取保留名称列表
            with open(txt_path, "r", encoding="utf-8") as f:
                keep_names = {line.strip() for line in f if line.strip()}

            # 读取原始JSON
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # 过滤站点
            original_count = 0
            if "sites" in data and isinstance(data["sites"], list):
                original_count = len(data["sites"])
                new_sites = [site for site in data["sites"] if site.get("name") in keep_names]
                data["sites"] = new_sites
                kept_count = len(new_sites)
            else:
                original_count = 0
                kept_count = 0
                new_sites = []
             # 修改lives键的值为指定路径
            if "lives" in data:
                with open(r"C:\C盘下载\Tvbox_json\sites_filter\lives.json", "r", encoding="utf-8") as f:
                    lives_data = json.load(f)
                    data["lives"] = lives_data["lives"]
            #修改壁纸和logo地址
            data["wallpaper"]="http://饭太硬.top/深色壁纸/api.php"
            data["logo"]= "https://cdn.jsdelivr.net/gh/xuelong876/mybox_PG@main/pg.gif"
            # 写入新JSON
            with open(out_json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            print(f"✅ 成功生成：{out_json_path}")
            print(f"   原始站点：{original_count} 个 | 保留：{kept_count} 个\n")
            
            success_count += 1
            total_original += original_count
            total_kept += kept_count

        except Exception as e:
            print(f"❌ 处理失败 {json_name}：{str(e)}\n")
    
    print(f"\n📊 过滤完成：处理 {success_count} 个文件，原始共 {total_original} 个站点，保留 {total_kept} 个\n")

if __name__ == "__main__":
    # 按步骤执行
    download_json_files()#下载JSON文件

    extract_names_to_txt()#提取站点名称生成TXT文件
    #程序暂停，提示键盘输入2
    key_name=input("过滤站点请输入 2 继续...")
    if key_name=="2":
        generate_filtered_json()#根据过滤后的TXT生成精简JSON


    

    print("🎉 全部流程执行完成！")
