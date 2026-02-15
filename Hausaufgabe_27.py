"""
1. Фильтрация по ключевому слову.
Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.
Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt

Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в error_system_log.txt.
"""

import os

input_filename = input("Enter the path to file for search: ")
keyword = input("Enter keyword: ").lower()

dir_name, base_name = os.path.split(input_filename)
output_filename = os.path.join(dir_name, f"{keyword}_{base_name}")

try:
    with open(input_filename, 'r', encoding='utf-8') as infile:
        matches_lines = [line for line in infile if keyword in line.lower()]

        if matches_lines:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                outfile.writelines(matches_lines)

            print(f"Lines containing the {keyword}, saved in {output_filename}")
        else:
            print(f"Matches with the {keyword} not founded. The File is not created")

except FileNotFoundError:
    print(f"Error: The file {input_filename} not founded")

"""
2. Поиск и удаление дубликатов
Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
Имя нового файла формируется как unique_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.
Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.
"""

import os

input_filename = input("Enter file name: ")
dir_name, base_name = os.path.split(input_filename)
output_filename = os.path.join(dir_name, f"unique_{base_name}")

try:
    with (open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w',
                                                                      encoding='utf-8') as outfile):
        seen = set()
        for line in infile:
            if line not in seen:
                output_filename.write(line)
        print(f"Duplicates removed, unique strings saved in {output_filename}")
except FileNotFoundError as e:
    print(f"Error: The File {input_filename} not found")
