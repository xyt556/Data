import os
import requests
import zipfile
import gdown
import re
# 通过链接下载文件
def download_file(file_url, save_path='.'):
    """
    通过链接下载单个文件并保存到本地。

    参数:
    file_url (str): 要下载的文件URL
    save_path (str): 保存文件的文件夹路径，默认为当前目录
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        # 获取文件名
        file_name = os.path.basename(file_url)
        file_path = os.path.join(save_path, file_name)

        # 确保文件夹存在
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # 保存文件
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"文件 {file_name} 已下载并保存到 {save_path}")
    else:
        print(f"无法下载文件，状态码: {response.status_code}")

# 文件 URLs
urls = [
    "https://github.com/xyt556/Data/raw/main/font_colab.ipynb",
    "https://github.com/xyt556/Data/raw/main/set_font.ipynb",
    # "https://github.com/xyt556/Data/raw/main/download_file.ipynb"
]

# 打印 URLs
print("文件 URLs:")
for url in urls:
    print(url)
    download_file(url)

# 下载目录，如github上的目录
def download_fold(url, local_dir = "./"):
    """
    从给定的GitHub仓库URL下载所有文件和目录。

    参数:
    url (str): GitHub API目录URL
    local_dir (str): 本地保存目录
    """
    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()  # 获取目录下的文件信息

        # 如果本地保存目录不存在，则创建该目录
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)

        # 遍历目录中的每个文件或子目录
        for file in files:
            if file['type'] == 'file':  # 如果是文件，下载文件
                file_url = file['download_url']
                download_file(file_url, local_dir)  # 调用合并后的下载函数
            elif file['type'] == 'dir':  # 如果是目录，递归下载该目录
                new_dir = os.path.join(local_dir, file['name'])
                download_fold(file['url'], new_dir)  # 递归下载子目录
    else:
        print(f"无法获取目录内容。状态码: {response.status_code}")

# 下载目录示例
# repo_url = "https://api.github.com/repos/xyt556/Data/contents/S_data/"
# local_dir = "xyt111"  # 本地存储目录
# download_fold(repo_url, local_dir)

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

# gdown下载Google网盘共享的文件
def extract_file_id(url):
    """
    从Google Drive共享链接中提取文件ID。

    参数:
    url (str): Google Drive共享链接

    返回:
    str: 文件ID
    """
    pattern = r'(?:/d/|id=)([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("无法从链接中提取文件ID")

def download_file_from_google_drive(url, output_folder='.'):
    """
    从Google Drive下载文件并保留原始文件名。

    参数:
    url (str): Google Drive文件的共享链接
    output_folder (str): 保存文件的文件夹路径
    """
    file_id = extract_file_id(url)
    download_url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(download_url, quiet=False, fuzzy=True)

# 示例用法
# download_file_from_google_drive('https://drive.google.com/file/d/1JY11SMlhCoHFvWSwevi_eya2eURtdWO5/view?usp=sharing')

# -------------------

# 下载Google共享文件夹
def download_folder_from_google_drive(url, output_folder='.'):
    """
    从Google Drive下载文件夹中的所有文件。

    参数:
    url (str): Google Drive文件夹的共享链接
    output_folder (str): 保存文件的文件夹路径
    """
    # 如果文件夹不存在，则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 使用 gdown 下载文件夹
    gdown.download_folder(url, quiet=False)


# 示例用法
# download_folder_from_google_drive('https://drive.google.com/drive/folders/1PlP6iqsXJeR4Atp5erf96DKvkWDRMTp_?usp=sharing')
# --------------------------

# 下载文件示例
# print("下载文件使用说明：")

# print("执行函数：")
# print("download_file(url, directory='.')")




# # 下载Google网盘共享文件夹及文件
# print("Goolgle网盘共享文件夹下载方法（不能超过50个文件）：")
# print("# 文件夹共享链接\n", "url = 'https://drive.google.com/drive/folders/1KPgKuxmW9nJ0dos4mXWAMFX2mnp5mTP-?usp=drive_link'\n", "gdown.download_folder(url, quiet=True, use_cookies=False)")
#
# print("Goolgle网盘共享文件下载方法：")
# print("# 文件共享链接\n", "url = 'https://drive.google.com/uc?id=1nfJVpHjRmsi9VFoQH8r5vDw7JW-_26QC'\n", "gdown.download(url, quiet=False, fuzzy=True)")

# 解压缩文件
# print("解压缩文件\n","unzip_file(zip_file_path, extract_to_dir='.')")