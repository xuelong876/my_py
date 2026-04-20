import os  # 操作系统接口模块，用于文件路径操作
import re  # 正则表达式模块，用于字符串匹配和处理
import glob  # 文件通配符模块，用于查找匹配的文件
from typing import List, Tuple, Optional, Dict, Any  # 类型注解模块，用于指定函数参数和返回值的类型


def normalize_channel_name(channel_name: str) -> Optional[str]:
    """
    标准化频道名称
    将不同格式的频道名称统一为标准化格式
    """
    # 特殊频道排除列表 - 这些频道不需要处理
    EXCLUDED_CHANNELS = {"CCTV4美洲", "CCTV4欧洲","河南卫视4K", "CCTV世界地理"}
    if channel_name in EXCLUDED_CHANNELS:
        return None  # 如果是排除的频道，返回None

    # 特殊频道映射 - 定义特殊频道的别名映射关系
    SPECIAL_CHANNELS = {
        "CHC家庭影院": ["CHC家庭影院", "家庭影院"],
        "CHC动作电影": ["CHC动作电影", "动作电影"],
        "梨园频道": ["河南戏曲", "梨园频道", "移动戏曲", "河南梨园"],
        "河南都市": ["河南都市", "都市频道", "河南都市报道"]
    }
    
    # 检查特殊频道 - 遍历特殊频道映射
    for normalized, variants in SPECIAL_CHANNELS.items():
        if channel_name in variants:
            return normalized  # 如果找到匹配的特殊频道，返回标准化名称

    # CCTV频道处理 - 专门处理CCTV频道的命名
    if "cctv" in channel_name.lower():
        cctv_match = re.search(r'cctv-*(\d+\+*)-*\W*', channel_name.lower())
        if cctv_match:
            return f"CCTV{cctv_match.group(1).upper()}"  # 提取CCTV后面的数字并格式化

    # 通用处理 - 对普通频道进行清理
    cleaned_name = channel_name.replace("高清", "").replace("频道", "")  # 移除常见后缀
    cleaned_name = re.sub(r'[-_|:：\s]+', '', cleaned_name).strip()  # 移除特殊字符和空白
    
    return cleaned_name if cleaned_name else None  # 返回清理后的名称，如果为空则返回None


def read_keywords_file(file_path: str) -> List[str]:
    """
    从文件读取关键词列表，支持多种编码
    自动尝试不同的编码格式来读取文件
    """
    encodings = ['utf-8', 'gbk', 'gb2312']  # 尝试的编码列表
    keywords = []  # 存储读取的关键词
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                for line in f:
                    line = line.strip()  # 移除行首尾空白
                    if line and not line.startswith('#'):  # 跳过空行和注释行
                        keywords.append(line)
            print(f"✅ 成功从 {file_path} ({encoding}) 读取 {len(keywords)} 个关键词")
            return keywords  # 成功读取后返回关键词列表
        except (UnicodeDecodeError, FileNotFoundError):
            continue  # 编码失败，尝试下一个编码
    
    print(f"❌ 无法读取文件 {file_path}，尝试的编码: {encodings}")
    return []  # 所有编码都失败，返回空列表


def extract_channel_url_from_line(line: str) -> Tuple[Optional[str], Optional[str]]:
    """
    从单行文本中提取频道名称和URL
    解析包含频道和URL的文本行
    """
    url_pattern = r'https?://[^\s]+'  # URL正则表达式模式
    url_match = re.search(url_pattern, line)  # 在行中搜索URL
    
    if not url_match:
        return None, None  # 如果没有找到URL，返回None

    url = url_match.group()  # 提取匹配的URL
    raw_channel_name = re.sub(url_pattern, '', line).strip().rstrip(",")  # 移除URL部分，得到原始频道名
    
    # 过滤无效频道名 - 定义无效名称集合
    INVALID_NAMES = {'|', '-', '_', ':', '：', ''}
    if not raw_channel_name or raw_channel_name in INVALID_NAMES:
        return None, None  # 如果是无效名称，返回None

    normalized_name = normalize_channel_name(raw_channel_name)  # 标准化频道名称
    return (normalized_name, url) if normalized_name else (None, None)  # 返回标准化名称和URL


def read_files_from_dir(dir_path: str) -> List[Tuple[str, str]]:
    """
    从目录读取所有文本文件并提取频道URL
    遍历目录中的所有txt文件，提取频道和URL信息
    """
    file_paths = glob.glob(os.path.join(dir_path, "*.txt"))  # 获取所有txt文件路径
    if not file_paths:
        raise FileNotFoundError(f"在目录 {dir_path} 中未找到任何txt文件")  # 如果没有文件，抛出异常

    all_channel_url = []  # 存储所有频道URL对
    encodings = ['utf-8', 'gbk', 'gb2312']  # 尝试的编码列表

    for file_path in file_paths:
        print(f"正在读取文件：{file_path}")
        
        lines = []  # 存储文件内容行
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    lines = f.readlines()  # 读取所有行
                if encoding != 'utf-8':
                    print(f"⚠️ 文件 {file_path} 使用 {encoding} 编码读取")  # 非UTF-8编码提示
                break  # 成功读取，跳出编码循环
            except UnicodeDecodeError:
                continue  # 编码失败，尝试下一个
        
        if not lines:
            print(f"❌ 无法解码文件 {file_path}，跳过该文件")  # 所有编码都失败
            continue

        for line_num, line in enumerate(lines, 1):  # 遍历每一行，从1开始计数
            line = line.strip()  # 移除行首尾空白
            if not line:
                continue  # 跳过空行
            
            channel, url = extract_channel_url_from_line(line)  # 提取频道和URL
            if channel and url:
                all_channel_url.append((channel, url))  # 有效数据添加到列表
            elif re.search(r'https?://', line) and not channel:
                print(f"⚠️ 第{line_num}行有URL但频道名提取失败: {line[:50]}...")  # 提取失败警告

    return all_channel_url  # 返回所有提取的频道URL对


def process_channel_data(channel_url_list: List[Tuple[str, str]], 
                        favorite_channels_path: Optional[str] = None) -> List[Tuple[str, str]]:
    """
    合并、去重、排序频道数据
    处理频道数据，包括去重和排序
    """
    # 去重 - 基于频道名和URL组合作为唯一键
    unique_channels = {}
    for channel, url in channel_url_list:
        key = f"{channel}_{url}"  # 创建唯一标识符
        if key not in unique_channels:
            unique_channels[key] = (channel, url)  # 只保留唯一的频道URL对

    unique_list = list(unique_channels.values())  # 转换为列表
    
    # 排序 - 根据收藏列表或自然排序
    favorite_channels = read_keywords_file(favorite_channels_path) if favorite_channels_path else []
    
    if favorite_channels:
        # 创建频道到优先级的映射 - 收藏频道优先
        channel_priority = {}
        for priority, fav_channel in enumerate(favorite_channels):  # 枚举收藏频道
            for channel, url in unique_list:
                if fav_channel in channel:  # 如果频道包含收藏关键词
                    channel_priority[channel] = priority  # 记录优先级
        
        def sort_key(item):
            channel, url = item
            # 优先按收藏列表排序，然后按频道名称自然排序
            return (0, channel_priority.get(channel, float('inf')), channel.lower(), url)
        
        sorted_list = sorted(unique_list, key=sort_key)  # 使用自定义排序键排序
    else:
        def natural_sort_key(item):
            channel = item[0].lower()  # 转换为小写
            return [int(part) if part.isdigit() else part  # 数字部分转换为整数
                   for part in re.split(r'(\d+)', channel)]  # 按数字分割
        
        sorted_list = sorted(unique_list, key=natural_sort_key)  # 自然排序

    return sorted_list  # 返回排序后的列表


def save_results(sorted_list: List[Tuple[str, str]], 
                txt_file: str, 
                m3u_file: Optional[str] = None) -> None:
    """
    保存结果到文件
    将处理后的数据保存为TXT和M3U格式
    """
    # 保存TXT文件 - 简单格式：频道名,URL
    with open(txt_file, 'w', encoding='utf-8') as f:
        for channel, url in sorted_list:
            f.write(f"{channel},{url}\n")  # 写入频道和URL
    
    print(f"✅ TXT文件已保存: {txt_file}")
    print(f"📊 共 {len(sorted_list)} 条有效记录")

    # 保存M3U文件（如果指定） - 播放列表格式
    if m3u_file:
        with open(m3u_file, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")  # M3U文件头
            for channel, url in sorted_list:
                channel_clean = channel.rstrip(",")  # 清理频道名
                # 写入M3U条目，包含频道信息和URL
                f.write(f'#EXTINF:-1 tvg-name="{channel_clean}" tvg-logo="https://cdn.jsdelivr.net/gh/xuelong876/channal_logo2@master/{channel_clean}.png" group-title="联通酒店", {channel_clean}\n{url}\n')
        
        print(f"✅ M3U文件已保存: {m3u_file}")


def main():
    """
    主函数
    程序的主要执行流程
    """
    # 配置项 - 定义文件路径和目录
    CONFIG = {
        'target_dir': r"C:\C盘下载\河南联通直播源",  # 源文件目录
        'favorite_file': r"C:\Users\xuelong88\Desktop\tvbox备份\收藏频道.txt", 
        # 'favorite_file': r"C:\Users\xuelong88\Desktop\tvbox备份\增加频道.txt",  # 给移动8M增加的频道

        'output_txt': r"C:\Users\xuelong88\Desktop\tvbox备份\联通酒店合并.txt",  # 输出TXT文件
        'output_m3u': r"C:\Users\xuelong88\Desktop\tvbox备份\联通酒店合并.m3u"  # 输出M3U文件
    }

    try:
        print("🚀 开始处理频道数据...")
        
        # 1. 读取数据 - 从目录读取所有文件
        raw_data = read_files_from_dir(CONFIG['target_dir'])
        print(f"📥 原始数据: {len(raw_data)} 条记录")
        
        # 2. 处理数据 - 去重和排序
        processed_data = process_channel_data(raw_data, CONFIG['favorite_file'])
        print(f"🔧 处理后数据: {len(processed_data)} 条记录")
        
        # 3. 过滤收藏频道 - 根据收藏列表筛选
        favorite_keywords = read_keywords_file(CONFIG['favorite_file'])
        if favorite_keywords:
            filtered_data = [
                (channel, url) for channel, url in processed_data
                if any(fav in channel for fav in favorite_keywords)  # 检查频道是否包含收藏关键词
            ]
            print(f"⭐ 收藏频道: {len(filtered_data)} 条记录")
        else:
            filtered_data = processed_data  # 没有收藏列表，使用全部数据
            print("⚠️ 无收藏列表，使用全部频道")
        
        # 4. 保存结果 - 保存为TXT和M3U文件
        save_results(filtered_data, CONFIG['output_txt'], CONFIG['output_m3u'])
        
        print("🎉 处理完成！")

    except Exception as e:
        print(f"❌ 程序执行出错: {e}")  # 异常处理
        raise  # 重新抛出异常


if __name__ == "__main__":
    main()  # 程序入口点
