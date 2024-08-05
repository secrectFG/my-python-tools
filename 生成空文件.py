import os
from PIL import Image
import numpy as np

def create_empty_files(directory, num_files):
    # 如果目录不存在，创建它
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, num_files + 1):
        file_path = os.path.join(directory, f'file_{i}.txt')
        file = open(file_path, 'w')
        file.write('1'*1000)
        file.close()
        print(f"已创建文件: {file_path}")
        generate_random_image(file_path.replace('.txt','.png'))
        
def generate_random_image(filename,size=(32, 32)):
    # 生成随机像素数据
    random_data = np.random.randint(0, 256, (size[0], size[1], 3), dtype=np.uint8)
    
    # 创建图像对象
    image = Image.fromarray(random_data, 'RGB')

    # 保存图像
    image.save(filename)

if __name__ == "__main__":
    directory = r'E:\UnityProjects\BigResoures\Assets\Resources'
    num_files = 10000
    
    create_empty_files(directory, num_files)
    
    print(f"已在目录 {directory} 中创建了 {num_files} 个空的文本文件。")
