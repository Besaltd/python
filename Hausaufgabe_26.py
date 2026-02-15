""" 1. Список файлов и папок

Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
- Отдельно список папок
- Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':

Папки:
- folder1
- folder2

Файлы:
- file1.txt
- file2.txt
- notes.docx """

import os, sys

if len(sys.argv) != 2:
    print("Correct usage: python/python3 script.py & dir path")
    sys.exit(1)

dir_path = sys.argv[1]

if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
    print(f"Error: Directory {dir_path} not found")
    sys.exit(1)

folders = []
files = []

for item in os.listdir(dir_path):
    full_path = os.path.join(dir_path, item)
    if os.path.isdir(full_path):
        folders.append(item)
    elif os.path.isfile(full_path):
        files.append(item)

print(f"\nDirectory contents '{dir_path}': ")

if folders:
    print("\n Folders: ")
    for folder in sorted(folders):
        print("•", folder)
if files:
    print("\n Files: ")
    for file in sorted(files):
        print("•", file)
