""" 
1. Извлечение дат

Реализуйте программу, которая должна:
- Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.
"""

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022"

import re


def get_date(data):
    return re.findall(r"\d{2}[\/\-.]\d{2}[\/\-.]\d{4}", data)


print(get_date(text))

""" 
2. Разделение списка тегов

Реализуйте программу, которая должна:
- Прочитать строку с тегами, введёнными пользователем.
- Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с запятой, слэши или пробелы).
- Удалить лишние пробелы и пустые значения. 
"""

tag_input = "python, data-science / machine-learning; AI neural-networks"

import re


def get_tag(data):
    return [tag for tag in re.split(r"[,\s;/]+", data)]


print(get_tag(tag_input))
