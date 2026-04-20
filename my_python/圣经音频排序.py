# 导入操作系统相关功能模块，用于文件和文件夹操作
import os
# 导入高级文件操作模块，用于复制文件
import shutil
# 导入正则表达式模块，用于从文件名中提取数字
import re
"""
圣经音频排序,方便唱戏机顺序播放

功能：
1. 从txt文件中读取所有文件夹名称，按顺序排序
2. 从每个文件夹中读取所有音频文件，按章节号排序
3. 重命名每个音频文件，添加序号前缀
4. 复制排序后的音频文件到目标文件夹
"""
# ===================== 【配置区】 =====================
# 1. 定义存放文件夹列表的txt文件路径，这个txt里按顺序写好了各个书卷文件夹的名字
TXT_PATH = r"F:\汉语和合本_音乐版\圣经.txt"
# 2. 定义源文件根目录，所有音频文件夹都放在这个目录下面
SOURCE_ROOT = r"F:\汉语和合本_音乐版\汉语和合本_音乐版_旧约1"
# 3. 定义排序重命名后文件保存的目标文件夹
TARGET_DIR = r"F:\汉语和合本_音乐版\旧约_排序"
# 4. 定义唱戏机需要的编号位数，3位就是生成 001,002...这样格式的编号
NUMBER_LENGTH = 3
# ======================================================


# 定义函数：从文件名中提取章节数字，用于排序
def extract_chapter_number(filename):
    """
    从文件名中精准提取章节数字（适配格式：001_1马太福音第1章.mp3）
    :param filename: 文件名（如001_1马太福音第1章.mp3）
    :return: 章节数字（整数，如1/10/20）
    """
    # 使用正则表达式匹配 "第X章" 格式中的数字X，优先提取这个章节数
    chapter_match = re.search(r'第(\d+)章', filename)
    # 如果匹配到了结果
    if chapter_match:
        # 返回提取到的第一个分组（就是括号里的数字），转换为整数
        return int(chapter_match.group(1))
    
    # 如果没找到"第X章"格式，启用备用规则：匹配下划线后面的数字（如001_1xxx → 提取1）
    num_after_underline = re.search(r'_(\d+)', filename)
    # 如果匹配到了结果
    if num_after_underline:
        # 返回提取到的数字，转换为整数
        return int(num_after_underline.group(1))
    
    # 如果前两种规则都没匹配到，启用兜底规则：提取文件名中所有的数字，选最大的那个作为章节数
    # 这样可以避免前面的序号干扰，保证拿到的是章节号
    all_nums = re.findall(r'\d+', filename)
    # 如果提取到了至少一个数字
    if all_nums:
        # 把所有字符串数字转成整数，然后取最大值返回
        return max([int(num) for num in all_nums])
    
    # 如果上面所有规则都没找到数字，返回0，排序的时候会排在最前面
    return 0

# 主函数，程序入口
def main():
    # 创建目标文件夹，如果文件夹不存在的话
    if not os.path.exists(TARGET_DIR):
        # 递归创建目标文件夹
        os.makedirs(TARGET_DIR)

    # 创建空列表，保存从txt中读取的文件夹名称
    folder_names = []
    # 尝试先用UTF-8编码打开txt文件
    try:
        f = open(TXT_PATH, "r", encoding="utf-8")
    # 如果UTF-8打开失败（大概率是GBK编码的txt），改用GBK编码打开
    except:
        f = open(TXT_PATH, "r", encoding="gbk")
    
    # 使用with语句自动管理文件，处理完后自动关闭文件
    with f:
        # 逐行读取txt文件内容
        for line in f:
            # 去除每行首尾的空格、换行符等空白字符
            line = line.strip()
            # 如果去除后是空行，或者行以#开头（注释行），就跳过这一行
            if not line or line.startswith("#"):
                continue
            # 把有效的文件夹名称添加到列表中
            folder_names.append(line)

    # 打印信息，告诉用户读取到了多少个文件夹
    print(f"✅ 读取到 {len(folder_names)} 个文件夹")

    # 定义全局连续编号，从1开始，用来生成唱戏机需要的顺序编号
    global_index = 1

    # 遍历读取到的每个文件夹名称，按txt中的顺序处理
    for folder in folder_names:
        # 拼接得到当前文件夹的完整绝对路径
        folder_path = os.path.join(SOURCE_ROOT, folder)
        # 检查这个路径是否真的是一个文件夹，如果不是就跳过
        if not os.path.isdir(folder_path):
            # 打印警告信息告诉用户跳过了这个文件夹
            print(f"⚠️  跳过不存在的文件夹：{folder}")
            continue

        # 1. 获取文件夹内所有文件，过滤掉子文件夹，只保留文件
        all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        # 2. 使用我们定义的extract_chapter_number函数作为排序依据，对文件按章节数字排序
        sorted_files = sorted(all_files, key=extract_chapter_number)

        # 打印当前处理的文件夹信息，告诉用户这个文件夹有多少个文件
        print(f"\n📂 处理文件夹：{folder}（共{len(sorted_files)}个文件）")

        # 3. 遍历排序好的每个文件，进行重命名和复制
        for filename in sorted_files:
            # 生成新的文件名：用zfill补全编号位数，加上原文件名
            # 比如 global_index是1，NUMBER_LENGTH是3，就会变成"001_原文件名.mp3"
            new_filename = f"{str(global_index).zfill(NUMBER_LENGTH)}_{filename}"
            # 拼接源文件完整路径
            src_file = os.path.join(folder_path, filename)
            # 拼接目标文件完整路径
            dst_file = os.path.join(TARGET_DIR, new_filename)

            # 使用copy2复制文件，保留文件的元信息（修改时间等），不修改原文件
            shutil.copy2(src_file, dst_file)
            # 打印处理信息，告诉用户当前文件处理完成
            print(f"  ✅ {filename} → {new_filename}")

            # 全局编号加1，为下一个文件做准备
            global_index += 1

    # 所有处理完成后，打印结束信息
    print("\n🎉 排序+重命名完成！")
    # 告诉用户文件保存的位置
    print(f"📁 最终文件路径：{TARGET_DIR}")
    # 给用户的使用提示
    print("💡 直接把这个文件夹里的文件复制到内存卡，唱戏机100%按顺序播放！")

# 判断如果当前文件是主程序入口，就执行main函数
if __name__ == "__main__":
    main()
