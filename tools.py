# -*- coding: utf-8 -*-
import requests
import os
import zipfile
import gdown

import os
import requests

import os
import requests

def download_file(file_url, fold='.'):
    """
    从GitHub下载单个文件并保存到本地。

    参数:
    file_url (str): 要下载的文件URL
    fold (str): 保存文件的文件夹路径
    """
    response = requests.get(file_url)
    file_name = os.path.basename(file_url)
    file_path = os.path.join(fold, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)

import os
import requests

def download_fold(repo_url, local_dir):
    """
    从GitHub上的目录下载文件到本地，并保持目录结构。

    :param repo_url: GitHub API URL，指向仓库目录。
    :param local_dir: 本地存储目录的路径。
    """
    # 获取GitHub API目录内容
    response = requests.get(repo_url)
    if response.status_code != 200:
        print(f"无法访问目录: {repo_url}")
        return

    # 确保本地目标目录存在
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # 获取目录中的内容列表
    files = response.json()

    for file in files:
        file_name = file['name']
        file_path = os.path.join(local_dir, file_name)

        # 如果是文件，则下载
        if file['type'] == 'file':
            down(file['download_url'], file_path)

        # 如果是目录，则递归调用下载
        elif file['type'] == 'dir':
            download_fold(file['url'], file_path)

def down(file_url, local_path):
    """
    下载单个文件到本地指定路径。

    :param file_url: 文件的GitHub下载链接
    :param local_path: 文件的本地保存路径
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"已下载文件: {local_path}")
    else:
        print(f"下载失败: {file_url}")

# 示例：下载GitHub仓库的指定目录
repo_url = "https://api.github.com/repos/xyt556/Data/contents/S-data/"
local_dir = "S-data"  # 本地存储目录
download_fold(repo_url, local_dir)



# 示例用法
local_dir = "S-data"
url = 'https://api.github.com/repos/xyt556/Data/contents/S-data/'
download_fold(url, local_dir)





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