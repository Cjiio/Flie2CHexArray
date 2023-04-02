import os
import binascii

# 获取当前Python文件所在目录的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 定义输入和输出文件夹路径
input_folder = os.path.join(current_dir, "Input")
output_folder = os.path.join(current_dir, "Output")

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 拼接输入和输出文件的完整路径
    input_path = os.path.join(input_folder, filename)
    output_filename = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, output_filename + ".c")

    # 读取输入文件中的数据
    with open(input_path, "rb") as f:
        data = f.read()

    # 将数据转换为hex字符串，并在每个字节前添加"0x"前缀和","后缀
    hex_str = ", ".join(["0x{:02x}".format(b) for b in data])

    # 将hex字符串按照每16个字节一行的格式进行换行
    hex_lines = [hex_str[i:i+48].rstrip() for i in range(0, len(hex_str), 48)]

    # 生成C语言数组的定义，包括文件类型注释
    array_def = "// File type: {}\nconst unsigned char {}[] = {{\n  {}\n}};".format(os.path.splitext(filename)[1], output_filename, "\n  ".join(hex_lines))

    # 将C语言数组定义写入输出文件中
    with open(output_path, "w") as f:
        f.write(array_def)
