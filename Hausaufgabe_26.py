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

"""
2. Поиск и удаление файлов с указанным расширением

Напишите программу, которая:
• Принимает путь к директории и расширение файлов через аргумент командной строки.
• Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
• Спрашивает у пользователя, хочет ли он удалить найденные файлы.
• Если пользователь подтверждает, удаляет их.

Пример запуска:
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':

- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os, sys

if len(sys.argv) != 3:
    print("Correct usage: python/python3 script.py & dir path & .extension")
    sys.exit(1)

path_to_folder = sys.argv[1]
extension = sys.argv[2]
found_files = []

for root, _, files in os.walk(path_to_folder):
    for file in files:
        if file.endswith(extension):
            found_files.append(os.path.join(root, file))

if not found_files:
    print(f"Files with extension {extension} not founded")
    sys.exit(0)

print(f"Files with the extension {extension}")
for file in found_files:
    print("•", file)

confirm = input("\nDo you want to delete these files? (y/n): ")
if confirm.lower() == 'y':
    for file in found_files:
        os.remove(file)
        print("Deletion successfully completed")
else:
    print("Deletion canceled")
