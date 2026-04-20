# TODO: 打印指定文件夹里面的文件名 并排列成N列
import os

# 假设这是包含多个文件夹的根目录路径
root_dir = 'C:/Users/Administrator/Desktop/jarfile/7.27'

# 创建一个字典来存储每个文件夹的文件名（不带后缀名）列表
folder_files_no_ext = {}

# 遍历根目录下的所有文件夹
for subdir, dirs, files in os.walk(root_dir):
    if subdir == root_dir:  # 跳过根目录本身
        continue
    last_name = os.path.basename(subdir)  # 使用os.path.basename()来获取最后的目录名
    files.insert(0, last_name)  # 目录名插入到列表首位

    while len(files) < 100:  # 如果每个文件夹里的文件名小于100 则用空格字符补齐
        files.append(' ')

    # 初始化或追加不带后缀名的文件名到对应文件夹的列表中  os.path.splitext(路径) 将路径拆分为文件名和扩展 并返回一个元组第一个元组为文件名，第二个为扩展名
    folder_files_no_ext[subdir] = [os.path.splitext(file)[0] for file in files]
separator = '  '  # 您可以根据需要调整分隔符的空格数
for i in range(100):
    # 初始化这一行将要打印的字符串
    line = ''
    first_file = True  # 第一文件标记，用于判断第一列文件 前不加空格
    row_print = []  # 每行文件列表
    # 遍历每个文件夹，获取对应位置的文件名（不带后缀名），并添加填充空格 items()方法返回字典键key 和数据value
    for subdir, files in folder_files_no_ext.items():
        if not first_file:  # 第一个文件跳过
            line += separator  # 在第一个文件名之后添加分隔符
        file = files[i]
        # 添加文件名和填充空格以达到最大宽度
        line += file + ' ' * (15 - len(file))
        row_print.append(line)  # 追加文件名到行列表
        first_file = False  # 不是第一行

    # 打印这一行
    print(line)
    row_print = []
