#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xue time:2024/5/16 7:34
# flle:打印文件目录树.PY
# TODO:在Python中，你可以使用os模块来遍历文件夹并打印文件树,排除图片文件（例如 .jpg、.png、.gif 等）。

import os


# def is_image_file(filename):
#     """检查文件是否是图片文件"""
#     image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
#     return os.path.splitext(filename)[1].lower() in image_extensions


"""
os.path.splitext(filename)[1] 用于分割文件名与其扩展名，并返回扩展名部分。[1] 是因为 os.path.splitext() 返回一个元组，
其中第一个元素是文件名（不包括扩展名），第二个元素是扩展名。

.lower() 是字符串方法，用于将字符串转换为小写 image_extensions 是一个集合，其中包含了要排除的图片文件的扩展名
"""


# def print_directory_tree(path, indent=0):
#     """
#     打印指定文件夹的文件树，排除图片文件
#     :param path: 文件夹路径
#     :param indent: 缩进量，用于表示层级关系
#     """
#
#     if os.path.isdir(path):  # 判断路径是不是路径
#         indix = 1
#         print(
#             ' ' * indent + +os.path.basename(path) + '/'
#         )  # 打印文件名缩进为0 os.path.basename(path为获取路径中的文件名
#         for item in os.listdir(path):  # 遍历当前目录下所有文件及文件夹名
#             item_path = os.path.join(path, item)  # os.path.join(path, item)连接路径和路径名
#             if os.path.isdir(item_path):  # 判断路径是不是路径 （是文件夹）
#                 print_directory_tree(item_path, indent + 4)  # 递归调用 文件路径为子目录 并缩进4个字符
#             elif not is_image_file(item):  # 如果不是图片文件，则打印
#                 print(' ' * (indent + 4) + +item)  # 打印文件夹及文件名，并缩进4个字符
#     else:
#         print("这不是一个文件夹")
"""
在这个代码中，is_image_file 函数用来检查一个文件是否是图片文件，它基于文件的扩展名来判断。
print_directory_tree 函数在遍历文件夹时，会忽略所有图片文件，只打印出非图片文件的名称。

你可以根据需要添加更多的图片文件扩展名到 image_extensions 集合中，以便排除更多类型的图片文件。同时，
请确保将 /path/to/your/directory 替换为你想要打印文件树的文件夹的实际路径。

"""


# TODO:给每个文件分配序号 以下是一个添加了序号的示例：


# def print_directory_tree(path, indent=0, file_num=1):
#     """
#     打印指定文件夹的文件树，并添加序号
#     :param path: 文件夹路径
#     :param indent: 缩进量，用于表示层级关系
#     :param file_num: 当前层级的文件序号
#     """
#     if os.path.isdir(path):
#         print(f'{" " * indent}{file_num}. {os.path.basename(path)}/')
#         total_files = len(
#             [
#                 name
#                 for name in os.listdir(path)
#                 if os.path.isfile(os.path.join(path, name))
#             ]
#         )
#         total_dirs = len(
#             [
#                 name
#                 for name in os.listdir(path)
#                 if os.path.isdir(os.path.join(path, name))
#             ]
#         )
#         next_file_num = file_num + total_dirs + 1
#         for item in os.listdir(path):
#             item_path = os.path.join(path, item)
#             if os.path.isdir(item_path):
#                 print_directory_tree(item_path, indent + 4, next_file_num)
#                 next_file_num += len(
#                     [
#                         name
#                         for name in os.listdir(item_path)
#                         if os.path.isdir(os.path.join(item_path, name))
#                     ]
#                 ) + len(
#                     [
#                         name
#                         for name in os.listdir(item_path)
#                         if os.path.isfile(os.path.join(item_path, name))
#                     ]
#                 )
#             else:
#                 print(f'{" " * (indent + 4)}{next_file_num}. {item}')
#                 next_file_num += 1
#     else:
#         print("这不是一个文件夹")


# """
# 在这个修改后的代码中，我们添加了一个参数来跟踪当前层级的文件序号。当遍历到一个文件夹时，我们会计算该文件夹下的子文件夹和文件数量，
# 以便为下一个层级的文件分配正确的序号。当遍历到一个文件时，我们直接打印出序号和文件名。file_num
#
# 注意：这个代码假设你想要为文件夹和文件都分配序号，并且序号是连续的。如果你只想为文件分配序号，或者你有其他的序号分配规则，
# 你可能需要进一步调整代码以满足你的需求。
# """
# TODO:排除图片文件，字幕（.srt .ass)不添加序号为其他文件添加序号


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
                if not item_path.lower().endswith(
                    ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
                ):
                    # 如果是字幕文件，则不添加序号
                    if not item_path.lower().endswith(('.srt', '.ass')):
                        print(' ' * (indent + 4) + f"{file_counter}. {item}")
                        file_counter += 1
    else:
        print("这不是一个文件夹")


"""

在这个代码中，我们检查每个文件是否以图片或字幕文件的扩展名结尾。如果不是图片文件，我们进一步检查它是否是字幕文件。如果既不是图片文件也不是字幕文件，我们则为其添加序号。

请注意，file_counter 只在递归调用中作为参数传递，因此它会在每个层级中重置。如果你想要在整个文件树中保持一个连续的序号，你需要将 file_counter 作为一个全局变量或者在函数外部以某种方式保持状态。在上面的示例中，序号会在每个目录层级内部连续。

将 /path/to/your/directory 替换为你要打印文件树的文件夹的实际路径，并根据需要添加或删除图片或字幕文件的扩展名。

"""

# 使用示例
print_directory_tree('//XIAOMI_EEF5/XiaoMi-usb3/data/TDDOWNLOAD/其他/.nomedia')
