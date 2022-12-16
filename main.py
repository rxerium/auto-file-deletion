import os
import shutil

downloads_folder = '/Users/rishi/Downloads'

files = os.listdir(downloads_folder)

for file in files:
    file_path = os.path.join(downloads_folder, file)
    if os.path.isdir(file_path):
        shutil.rmtree(file_path)
    else:
        os.remove(file_path)