#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xue time:2023/9/23 12:40
# flle:百年盒子live.PY
import json
M3U_file_w = "txt" # 文件写入类型 可选项 m3u或其他 txt
name_path = "蜜桃"  #平台名称

#定义一个函数：作用：读取文件 输入地址 返回 列表：address(播放地址） name(主播名称)
def File_read(name_path):                            #读取文件方法 形参为文件地址 相对地址只填文件名 返回 主播名称 和地址
    f = open(f"D:/live/{name_path}.txt","r",encoding="utf-8-sig")  #打开直播平台JSON文件
    data_json =f.read()                              #读取JSON文件
    f.close()                                       # 关闭文件
    data_dict = json.loads(data_json) ["zhubo"]       #json转python 并取出主播数据
    live_list = []                              #新建直播列表
    for line in data_dict:                              #遍历字典 ，取出每个主播数据
        title = line["title"]                       # 主播名称
        address = line["address"]                 #直播地址
        live_list.append([title,address])         #以列表形式写入列表
    return live_list                    #f返回直播名称和地址 [[主播，地址]，[直播，地址]...]
data = File_read(name_path)             #接收指定文件列表数据

#定义一个函数：传入数据为列表data 写入文件为 txt 的文件存入 百年盒子txt 文件夹，m3u文件存入 百年盒子m3u文件夹
def File_write(data):
    if M3U_file_w == "m3u":   #判断 文件格式 是否为 “m3u"
        fw = open(f"D:/live/百年盒子m3u/{name_path}.m3u", "w", encoding="utf-8")  # 新建 m3u格式文件
        fw.write("#EXTM3U\n")          #x写入M3U 文件表头
        for line in data:              #遍历列表 取出 主播 和地址
            fw.write(f"#EXTINF:-1,{line[0]}\n{line[1]}\n")   #写入m3u 格式文件
        fw.close()                                           #关闭文件
    else:
        fw = open(f"D:/live/百年盒子txt/{name_path}.txt", "w", encoding="utf-8")  # 新建 txt 格式文件
        for line in data:                               #遍历列表 取出直播和地址
            fw.write(f"{line[0]},{line[1]}\n")           #写入txt格式文件
        fw.close()                                       #关闭列表

File_write(data)                                        #运行写入文件







