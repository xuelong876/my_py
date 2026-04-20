#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xue time:2024/7/27 12:27
# flle:打印指定后缀目录树 .py.PY

import os


def print_directory_tree(path, indent=0, file_counter=1):
    """
    打印指定文件夹的文件树，排除图片文件，字幕文件不添加序号
    :param path: 文件夹路径
    :param indent: 缩进量，用于表示层级关系
    :param file_counter: 当前层级的文件序号
    """
    if os.path.isdir(path):
        print(' ' * indent + os.path.basename(path) + '/')
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent + 4, file_counter)
            elif os.path.isfile(item_path):
                # 检查是否为图片文件或字幕文件 endswith() 是一个字符串方法，用于检查字符串是否以指定的后缀或后缀之一结束
                if item_path.lower().endswith(('.java')):
                    # strip(".java")去除后缀.java
                    print(' ' * (indent + 4) + f"{file_counter}. {item.strip('.java')}")
                    file_counter += 1
    else:
        print("这不是一个文件夹")


# 使用示例
print_directory_tree(r"C:\工具\HZ(DIY)工具箱合集v1.0.7z")
