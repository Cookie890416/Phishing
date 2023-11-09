import os
import shutil

def find_and_copy_all_shot_png(root_folder, result_folder):
    # 确保 result_folder 存在，如果不存在则创建
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # 使用 os.walk() 遍历 A、B、C、D 四个文件夹
    for folder_path, _, files in os.walk(root_folder):
        # 检查当前文件夹是否包含 shot.png 文件
        if 'shot.png' in files:
            # 构建 shot.png 文件的完整路径
            shot_png_path = os.path.join(folder_path, 'shot.png')

            # 构建目标文件路径（在 result 文件夹下）
            target_path = os.path.join(result_folder, os.path.basename(folder_path) + '_shot.png')
            
            # 复制 shot.png 文件到 result 文件夹
            shutil.copy(shot_png_path, target_path)

# 替换 'your/root/folder/path' 为实际根文件夹路径
root_folder_path = 'Benign'
# 替换 'result' 为实际结果文件夹路径
result_folder_path = 'BenignData'

find_and_copy_all_shot_png(root_folder_path, result_folder_path)