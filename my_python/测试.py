#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xue time:2024/7/30 8:45
# flle:测试.py.PY
import os

# 假设这是包含多个文件夹的根目录路径
root_dir = 'C:/Users/Administrator/Desktop/jarfile/7.27'

# 创建一个字典来存储每个文件夹的文件名（不带后缀名）列表
folder_files_no_ext = {}
filesname = True
# 遍历根目录下的所有文件夹
for subdir, dirs, files in os.walk(root_dir):
    # 跳过根目录本身

    if subdir == root_dir:
        continue
    while len(files) < 100:
        files.append(' ')

        # 初始化或追加不带后缀名的文件名到对应文件夹的列表中  os.path.splitext(路径) 将路径拆分为文件名和扩展 并返回一个元组第一个元组为文件名，第二个为扩展名
    folder_files_no_ext[subdir] = [os.path.splitext(file)[0] for file in files]

# # 确定所有文件夹中文件数量的最大值，以及每列需要的最大宽度
# # # 确定文件数量最多的
# #
# # filemame_max_column = []  # 文件名每列最长值列表
# # file_num = []  # 每列文件数目
# #
# # for files in folder_files_no_ext.values():
# #     maxfile = max(files, key=len)
# #
# #     filemame_max_column.append(len(maxfile))
# #
# #     print(filemame_max_column)
# # #
#     file_num[j] = len(files)
#     j += 1
# max_file_num = max(file_num)  # 最大文件数

# max_filenum = max(len(files) for files in folder_files_no_ext.values())
# # max_files_per_folder = max(len(files) for files in folder_files_no_ext.values())
# # 初始化一个列表，这个列表长度为max_files_per_folder 并且列表的每个元素都为0
# max_filename_widths = [0] * max_files_per_folder
#
# # 计算每列需要的最大宽度（不带后缀名的文件名）
# for files in folder_files_no_ext.values():
#     # enumerate() 函数返回 可迭代对象（列表，元组，字符串）的下标索引 和元素的元组
#     for i, file in enumerate(files):
#         max_filename_widths[i] = max(max_filename_widths[i], len(file))
#
#         # 打印文件名（不带后缀名），文件名之间用空格填充以实现列对齐
#         # for i in range(max_files_per_folder):
#         #     # 初始化这一行将要打印的字符串
#         #     line = ''
#         #
#         #     # 遍历每个文件夹，获取对应位置的文件名（不带后缀名），并添加填充空格
#         #     for subdir, files in folder_files_no_ext.items():
#         #         if i < len(files):
#         #             file = files[i]
#         #             # 添加文件名和填充空格以达到最大宽度
#         #             line += (
#         #                 file + ' ' * (max_filename_widths[i] - len(file)) + '\t'
#         #             )  # 或者使用额外的制表符作为分隔符
#         #         # 如果文件夹在该位置没有文件，则不添加任何内容（或者可以添加空格以保持对齐）
#         #
#         #     # ...（前面的代码保持不变，直到计算max_filename_widths）
#
# 打印文件名（不带后缀名），文件名之间用空格填充以实现列对齐，不使用制表符作为分隔符
separator = '  '  # 您可以根据需要调整分隔符的空格数
# 生成序列数 最大值为 文件名最多的97


for i in range(100):
    #         # 初始化这一行将要打印的字符串
    line = ''
    first_file = True
    row_print = []
    # 遍历每个文件夹，获取对应位置的文件名（不带后缀名），并添加填充空格
    for subdir, files in folder_files_no_ext.items():
        if not first_file:
            line += separator  # 在第一个文件名之后添加分隔符
        file = files[i]
        # 添加文件名和填充空格以达到最大宽度
        line += file + ' ' * (15 - len(file))
        row_print.append(line)
        first_file = False

    # 打印这一行
    print(line)
    row_print = []
# # #
#     # 打印这一行（注意：我们已经在每个文件名后添加了制表符作为分隔符，所以这里不需要额外的换行符）
#     # print(line.rstrip('\t'))  # 使用rstrip去除末尾可能的多余制表符
