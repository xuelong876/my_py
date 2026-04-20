import os

# 提取指定文件夹的所有包含.png文件名字(不包含后缀.png)
def extract_png_names(folder_path):
    """从指定文件夹中提取所有PNG文件的文件名（不包含.png后缀）"""
    png_names = []
    for item in os.listdir(folder_path):
        if item.endswith('.png'):
            png_names.append(item.strip('.png'))
    return png_names


def read_channel_names(file_pach):
    """从文件中读取频道名称列表
    
    参数:
        file_pach: 包含频道信息的文件路径
        
    返回:
        list: 包含所有频道名称的列表
    """
    channel_names = []

    with open(file_pach, 'r', encoding='utf-8') as file:
        content = file.read()
        # 按行读取文件用逗号分割，去掉前后空格，将每个频道名添加到列表中
        for line in content.splitlines():
            # 按逗号分割，取第一个部分作为频道名
            if ',' in line:
                channel_name = line.split(',')[0].strip()
                channel_names.append(channel_name)

    return channel_names


# 如果channel_names中的元素在png_names中也存在，就删除channel_names中的元素
def delete_existing_channels(channel_names, png_names):
    """删除已经存在对应PNG文件的频道名称
    
    参数:
        channel_names: 包含频道名称的文件路径或列表
        png_names: 包含PNG文件名的文件夹路径或列表
        
    返回:
        list: 过滤后的频道名称列表（不包含已有PNG文件的频道）
    """
    # 如果传入的是文件路径，则读取文件内容
    if isinstance(channel_names, str):
        channel_names = read_channel_names(channel_names)
    # 如果传入的是文件夹路径，则提取PNG文件名
    if isinstance(png_names, str):
        png_names = extract_png_names(png_names)

    # 创建新列表来存储结果，避免在遍历时修改原列表
    result = []
    for channel in channel_names:
        if channel not in png_names:
            result.append(channel)
    return result


if __name__ == '__main__':
    # 定义联通直播文件路径
    live_path = r"C:\Users\xuelong88\Desktop\tvbox备份\pg.20260216-2329\live\LT8M.txt"
    # 定义TVLOGO图片文件夹路径
    tv_logo_pach = r"C:\Github\channal_logo2"

    # 直播频道名没有包含在台标文件夹的频道名
    channel_nanes = delete_existing_channels(live_path, tv_logo_pach)
   #打印过滤后的频道名
    print("直播频道名没有包含在台标文件夹的频道名:")
    
    for name in channel_nanes:
        print(name)



