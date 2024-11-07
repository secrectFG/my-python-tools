import os
import shutil
import random
import string

def get_random_string(length=8):
    """生成指定长度的随机字符串"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def flatten_directory(directory):
    """将指定目录中的所有文件扁平化"""
    if not os.path.isdir(directory):
        print(f"{directory} 不是一个有效的目录")
        return

    # 创建一个目标目录来存放所有的文件
    # flat_dir = os.path.join(directory, "flattened") 
    flat_dir = directory + "_flattened"
    os.makedirs(flat_dir, exist_ok=True)
    
    for root, _, files in os.walk(directory):
        for file in files:
            current_path = os.path.join(root, file)
            new_path = os.path.join(flat_dir, file)
            
            # 如果新路径已经存在文件，生成新的文件名
            while os.path.exists(new_path):
                name, ext = os.path.splitext(file)
                new_file_name = f"{name}_{get_random_string()}{ext}"
                new_path = os.path.join(flat_dir, new_file_name)
            
            # 将文件复制到新的路径
            shutil.copy2(current_path, new_path)
            print(f"文件 {current_path} 已被复制到 {new_path}")

if __name__ == "__main__":
    directory = input("请输入要扁平化处理的目录路径：")
    flatten_directory(directory)
