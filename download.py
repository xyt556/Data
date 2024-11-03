# -*- coding: utf-8 -*-
import requests
import os
import zipfile
import gdown

def download_file(url, directory='.'):
    response = requests.get(url, allow_redirects=True)
    filename = os.path.basename(url)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as file:
        file.write(response.content)
    print(f"{filepath} 下载完成")

# 解压缩
def unzip_file(zip_file_path, extract_to_dir='.'):
    """
    解压指定的 ZIP 文件到指定目录。如果没有提供目标目录，则解压到ZIP文件所在的目录。

    参数:
    zip_file_path (str): ZIP 文件的路径
    extract_to_dir (str): 解压后的目标目录（可选）。如果未指定，默认为 ZIP 文件所在目录
    """
    if extract_to_dir is None:
        # 如果没有提供目标解压目录，使用ZIP文件的所在目录
        extract_to_dir = os.path.dirname(zip_file_path)

    # 确保目标目录存在
    if not os.path.exists(extract_to_dir):
        os.makedirs(extract_to_dir)

    # 解压 ZIP 文件
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)  # 解压所有文件
        print(f"已解压 '{zip_file_path}' 到 '{extract_to_dir}'")

print("下载文件使用说明：")
# 文件 URLs
urls = [
    "https://github.com/xyt556/Data/raw/main/font_colab.ipynb",
    "https://github.com/xyt556/Data/raw/main/set_font.ipynb",
    "https://github.com/xyt556/Data/raw/main/download_file.ipynb"
]
# 打印 URLs
print("文件 URLs:")
for url in urls:
    print(url)
    download_file(url)
print("执行函数：")
print("download_file(url, directory='.')")

# 下载Google网盘共享文件夹及文件
print("Goolgle网盘共享文件夹下载方法（不能超过50个文件）：")
print("# 文件夹共享链接\n", "url = 'https://drive.google.com/drive/folders/1KPgKuxmW9nJ0dos4mXWAMFX2mnp5mTP-?usp=drive_link\n", "gdown.download_folder(url, quiet=True, use_cookies=False)")

print("Goolgle网盘共享文件下载方法：")
print("# 文件共享链接\n", "url = 'https://drive.google.com/uc?id=1nfJVpHjRmsi9VFoQH8r5vDw7JW-_26QC\n", "gdown.download(url, quiet=False, fuzzy=True)")

# 解压缩文件
print("解压缩文件\n","unzip_file(zip_file_path, extract_to_dir='.')")