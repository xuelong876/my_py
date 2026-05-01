#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
文件目录树打印工具
支持三种模式：
1. 打印全部文件
2. 只打印视频文件
3. 排除指定后缀名打印
"""

import os
import sys

# 定义常见视频文件后缀
VIDEO_EXTENSIONS = {
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v',
    '.mpg', '.mpeg', '.3gp', '.3g2', '.ogv', '.ts', '.mts', '.m2ts',
    '.vob', '.rm', '.rmvb', '.asf', '.divx'
}

# 定义常见图片文件后缀（用于排除）
IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico', '.svg'
}

# 定义常见字幕文件后缀
SUBTITLE_EXTENSIONS = {
    '.srt', '.ass', '.ssa', '.sub', '.idx', '.vtt'
}


def get_extension(filename):
    """获取文件扩展名（小写）"""
    return os.path.splitext(filename)[1].lower()


def is_video_file(filename):
    """检查是否为视频文件"""
    return get_extension(filename) in VIDEO_EXTENSIONS


def is_excluded_file(filename, exclude_extensions):
    """检查文件是否在排除列表中"""
    return get_extension(filename) in exclude_extensions


def format_size(size_bytes):
    """格式化文件大小显示"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}TB"


def sort_items(items, path):
    """
    排序目录内容：文件夹优先，然后按名称排序
    """
    dirs = []
    files = []
    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            dirs.append(item)
        else:
            files.append(item)
    return sorted(dirs) + sorted(files)


def should_include_file(filename, mode, exclude_extensions=None):
    """判断文件是否应该被显示"""
    if mode == 1:
        return True
    elif mode == 2:
        return is_video_file(filename)
    elif mode == 3:
        return not is_excluded_file(filename, exclude_extensions)
    return True


def print_directory_tree(
    path, 
    mode, 
    exclude_extensions=None, 
    show_excluded=False, 
    show_size=False, 
    indent=0, 
    file_counter=1,
    is_last=True,
    prefix=""
):
    """
    通用目录树打印函数（统一处理三种模式）
    :param path: 文件夹路径
    :param mode: 打印模式 1-全部 2-仅视频 3-排除指定
    :param exclude_extensions: 要排除的后缀名集合
    :param show_excluded: 是否显示被排除的文件
    :param show_size: 是否显示文件大小
    :param indent: 缩进量
    :param file_counter: 文件序号计数器
    :param is_last: 是否是当前目录最后一个项目
    :param prefix: 前缀（用于绘制树形结构）
    """
    if not os.path.isdir(path):
        print(f"{prefix}错误：这不是一个有效的文件夹路径")
        return file_counter
    
    # 打印根目录名称
    if indent == 0:
        print(os.path.basename(path) + "/")
    
    try:
        items = sort_items(os.listdir(path), path)
    except PermissionError:
        print(f"{prefix}    [权限不足，无法读取]")
        return file_counter
    
    # 过滤需要显示的项目
    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        is_last_item = index == len(items) - 1
        if os.path.isdir(item_path):
            # 打印文件夹名称
            connector = "└─ " if is_last_item else "├─ "
            print(f"{prefix}{connector}{item}/")
            
            # 计算新前缀
            new_prefix = prefix + ("    " if is_last_item else "│   ")
            
            # 递归处理子文件夹
            file_counter = print_directory_tree(
                item_path, mode, exclude_extensions, 
                show_excluded, show_size, indent + 4, 
                file_counter, is_last_item, new_prefix
            )
        
        elif os.path.isfile(item_path):
            include = should_include_file(item, mode, exclude_extensions)
            
            if not include:
                if show_excluded:
                    connector = "└─ " if is_last_item else "├─ "
                    print(f"{prefix}{connector}[已排除] {item}")
                continue
            
            # 构建显示名称
            size_info = ""
            if show_size:
                file_size = os.path.getsize(item_path)
                size_info = f" [{format_size(file_size)}]"
            
            connector = "└─ " if is_last_item else "├─ "
            print(f"{prefix}{connector}{file_counter}. {item}{size_info}")
            file_counter += 1
    
    return file_counter


def get_user_input():
    """获取用户输入的模式和参数"""
    print("=" * 50)
    print("文件目录树打印工具")
    print("=" * 50)
    print("请选择打印模式：")
    print("  1 - 打印全部文件（所有文件带序号）")
    print("  2 - 只打印视频文件（只显示视频文件）")
    print("  3 - 排除指定后缀名打印")
    print("  0 - 退出程序")
    print("-" * 50)
    
    while True:
        try:
            mode = input("请输入模式编号 (0-3): ").strip()
            if mode in ['0', '1', '2', '3']:
                return int(mode)
            else:
                print("输入无效，请输入 0、1、2 或 3")
        except KeyboardInterrupt:
            print("\n已取消")
            return 0


def get_exclude_extensions():
    """获取用户要排除的后缀名"""
    print("\n请输入要排除的后缀名（多个后缀用逗号分隔，如：.txt,.log,.tmp）")
    print("直接回车使用默认排除项（图片+字幕）")
    
    user_input = input("排除后缀: ").strip()
    
    if not user_input:
        # 默认排除图片和字幕文件
        default_exclude = IMAGE_EXTENSIONS | SUBTITLE_EXTENSIONS
        print(f"使用默认排除项: {', '.join(sorted(default_exclude))}")
        return default_exclude
    
    # 解析用户输入的后缀名
    extensions = set()
    for ext in user_input.split(','):
        ext = ext.strip().lower()
        if not ext.startswith('.'):
            ext = '.' + ext
        extensions.add(ext)
    
    return extensions


def main():
    """主函数"""
    # 获取文件夹路径
    print("\n请输入要打印的文件夹路径：")
    print("（可以直接拖拽文件夹到此窗口，或手动输入路径）")
    
    while True:
        path = input("路径: ").strip().strip('"').strip("'")
        if path:
            break
        print("路径不能为空，请重新输入")
    
    # 检查路径是否存在
    if not os.path.exists(path):
        print(f"错误：路径 '{path}' 不存在")
        return
    
    # 获取打印模式
    mode = get_user_input()
    
    if mode == 0:
        print("已退出程序")
        return
    
    # 询问是否显示文件大小
    show_size_input = input("\n是否显示文件大小？(y/N): ").strip().lower()
    show_size = show_size_input == 'y'
    
    print("\n" + "=" * 50)
    print(f"正在扫描: {path}")
    print("=" * 50 + "\n")
    
    # 根据模式执行相应的打印函数
    if mode == 1:
        print_directory_tree(path, mode=1, show_size=show_size)
    elif mode == 2:
        print_directory_tree(path, mode=2, show_size=show_size)
    elif mode == 3:
        exclude_extensions = get_exclude_extensions()
        show_excluded = input("\n是否显示被排除的文件？(y/N): ").strip().lower() == 'y'
        print()
        print_directory_tree(
            path, mode=3, exclude_extensions=exclude_extensions,
            show_excluded=show_excluded, show_size=show_size
        )
    
    print("\n" + "=" * 50)
    total_files = print_directory_tree.__closure__[0].cell_contents if False else file_counter
    # 这里直接使用最终计数器的值，因为函数会返回它
    final_counter = 0
    if mode == 1:
        final_counter = print_directory_tree(path, mode=1, show_size=False) - 1
    elif mode == 2:
        final_counter = print_directory_tree(path, mode=2, show_size=False) - 1
    elif mode == 3:
        final_counter = print_directory_tree(
            path, mode=3, exclude_extensions=exclude_extensions,
            show_excluded=show_excluded, show_size=False
        ) - 1
    
    print(f"\n总计显示 {final_counter} 个文件")
    print("打印完成！")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {e}")
