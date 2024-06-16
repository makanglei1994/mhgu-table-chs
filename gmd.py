# 代码参考 https://github.com/mhvuze/gmdDump/blob/master/gmdDump/Program.cs
from io import BufferedReader
import struct
import os

def swapEndianness(x) :
    return ((x & 0x000000ff) << 24) + ((x & 0x0000ff00) << 8) + ((x & 0x00ff0000) >> 8) + ((x & 0xff000000) >> 24)

def read_null_terminated(binary_reader: BufferedReader, file_size):
    char_array = bytearray()
    while True:
        b = binary_reader.read(1)
        if b == b'\x00' or binary_reader.tell() == file_size:
            break
        char_array.extend(b)
    try:
        str_value = char_array.decode('utf-8')
    except:
        str_value = "<Decode Error>"
    return str_value

for root, dirs, files in os.walk("./chS/table"):
    for file in files:
        if not file.endswith(".gmd"):
            continue
        file_size = os.path.getsize(f"{root}/{file}")

        with open(f"{root}/{file}", "rb") as fs:
            header = struct.unpack('<I', fs.read(4))[0]
            version = struct.unpack('<I', fs.read(4))[0]

            if header != 0x00444D47:
                raise TypeError("文件类型不正确")
            
            if (version == 0x00010302):
                identifier_count_offset = 0x14
                identifier_size_offset = 0x1C
                s_count_offset = 0x18
                t_size_offset = 0x20
            
            fs.seek(identifier_count_offset)
            identifier_count = struct.unpack('<I', fs.read(4))[0]

            fs.seek(identifier_size_offset)
            i_table_size = struct.unpack('<I', fs.read(4))[0]

            fs.seek(s_count_offset)
            string_count = struct.unpack('<I', fs.read(4))[0]

            fs.seek(t_size_offset)
            table_size = struct.unpack('<I', fs.read(4))[0]

            if (string_count == 0):
                fs.seek(0x18)
                string_count = struct.unpack('<I', fs.read(4))[0]

                fs.seek(0x20)
                table_size = struct.unpack('<I', fs.read(4))[0]
            
            table_start = file_size - table_size - i_table_size
            fs.seek(table_start)

            print(f"{root} {file} {identifier_count}, {i_table_size}, {string_count}, {table_size}, {table_start}")

            base_name, ext = os.path.splitext(file)
            new_root_path = root.replace("chS", "target")
            new_file = f"{new_root_path}/{base_name}.txt"

            # 获取文件所在的目录路径
            dir_path = os.path.dirname(new_file)
            
            # 检查目录是否存在，如果不存在则创建
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            with open(new_file, "w", newline="", encoding='utf-8') as f:
  
                f.write("==========identifier start==========\n")
                for i in range(identifier_count):
                    hasHeader = True
                    str = read_null_terminated(fs, file_size).replace("\r\n", "<BR/>")
                    f.write(str + "\n")

                f.write("==========identifier end==========\n\n")

                f.write("==========string start==========\n")
                for i in range(string_count):
                    str = read_null_terminated(fs, file_size).replace("\r\n", "<BR/>")
                    
                    f.write(str + "\n")
                f.write("==========string end==========\n")