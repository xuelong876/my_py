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


def print_directory_tree_all(path, indent=0, file_counter=1, prefix=""):
    """
    模式1：打印全部文件（带序号）
    :param path: 文件夹路径
    :param indent: 缩进量
    :param file_counter: 文件序号计数器
    :param prefix: 前缀（用于递归时传递序号状态）
    """
    if not os.path.isdir(path):
        print("错误：这不是一个有效的文件夹路径")
        return file_counter
    
    # 打印当前文件夹名称
    print(' ' * indent + os.path.basename(path) + '/')
    
    # 获取并排序目录内容
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(' ' * (indent + 4) + '[权限不足，无法读取]')
        return file_counter
    
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            # 递归处理子文件夹
            file_counter = print_directory_tree_all(item_path, indent + 4, file_counter, prefix)
        elif os.path.isfile(item_path):
            # 打印文件（全部文件都带序号）
            print(' ' * (indent + 4) + f"{file_counter}. {item}")
            file_counter += 1
    
    return file_counter


def print_directory_tree_video(path, indent=0, file_counter=1, prefix=""):
    """
    模式2：只打印视频文件（只对视频文件编号，非视频文件不显示）
    :param path: 文件夹路径
    :param indent: 缩进量
    :param file_counter: 文件序号计数器
    :param prefix: 前缀
    """
    if not os.path.isdir(path):
        print("错误：这不是一个有效的文件夹路径")
        return file_counter
    
    # 打印当前文件夹名称
    print(' ' * indent + os.path.basename(path) + '/')
    
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(' ' * (indent + 4) + '[权限不足，无法读取]')
        return file_counter
    
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            # 递归处理子文件夹
            file_counter = print_directory_tree_video(item_path, indent + 4, file_counter, prefix)
        elif os.path.isfile(item_path):
            # 只打印视频文件
            if is_video_file(item):
                # 显示文件信息（可选的额外信息）
                file_size = os.path.getsize(item_path)
                size_str = format_size(file_size)
                print(' ' * (indent + 4) + f"{file_counter}. {item} [{size_str}]")
                file_counter += 1
            # 非视频文件不显示，也不占用序号
    
    return file_counter


def print_directory_tree_exclude(path, exclude_extensions, indent=0, file_counter=1, show_excluded=False):
    """
    模式3：排除指定后缀名打印目录树
    :param path: 文件夹路径
    :param exclude_extensions: 要排除的后缀名集合（如 {'.txt', '.log'}）
    :param indent: 缩进量
    :param file_counter: 文件序号计数器
    :param show_excluded: 是否显示被排除的文件（标记为[已排除]）
    """
    if not os.path.isdir(path):
        print("错误：这不是一个有效的文件夹路径")
        return file_counter
    
    # 打印当前文件夹名称
    print(' ' * indent + os.path.basename(path) + '/')
    
    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        print(' ' * (indent + 4) + '[权限不足，无法读取]')
        return file_counter
    
    for item in items:
        item_path = os.path.join(path, item)
        
        if os.path.isdir(item_path):
            # 递归处理子文件夹
            file_counter = print_directory_tree_exclude(
                item_path, exclude_extensions, indent + 4, file_counter, show_excluded
            )
        elif os.path.isfile(item_path):
            # 检查是否被排除
            if is_excluded_file(item, exclude_extensions):
                if show_excluded:
                    print(' ' * (indent + 4) + f"[已排除] {item}")
                # 被排除的文件不占用序号
            else:
                print(' ' * (indent + 4) + f"{file_counter}. {item}")
                file_counter += 1
    
    return file_counter


def format_size(size_bytes):
    """格式化文件大小显示"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}TB"


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
    
    print("\n" + "=" * 50)
    print(f"正在扫描: {path}")
    print("=" * 50 + "\n")
    
    # 根据模式执行相应的打印函数
    if mode == 1:
        print_directory_tree_all(path)
    elif mode == 2:
        print_directory_tree_video(path)
    elif mode == 3:
        exclude_extensions = get_exclude_extensions()
        show_excluded = input("\n是否显示被排除的文件？(y/N): ").strip().lower() == 'y'
        print()
        print_directory_tree_exclude(path, exclude_extensions, show_excluded=show_excluded)
    
    print("\n" + "=" * 50)
    print("打印完成！")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已被用户中断")
    except Exception as e:
        print(f"\n程序运行出错: {e}")