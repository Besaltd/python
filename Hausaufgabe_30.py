"""
1. Анализ курсов студентов.
Реализовать программу, которая должна:
Прочитать файл student_courses.json, содержащий:
имя, дату рождения (birth_date) в формате дд.мм.гггг,
дату поступления (enrollment_date) в том же формате,
список курсов.

Вычислить:
Общее количество студентов.
Средний возраст на момент поступления.
Количество студентов на каждом курсе.
Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from datetime import datetime
from collections import Counter

# Путь к файлу со студентами
path = ("/Users/ernie/Documents/Studium/Python/Hausaufgaben/student_courses.json")


def total_reduce():
    total = dict()

    # Чтение JSON файла
    with open(path, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        print(loaded_data)

        # находим количество студентов
        total['total_student'] = len(loaded_data)

    # определяем средний возраст студента

    age_sum = 0

    for student in loaded_data:
        birth_date = datetime.strptime(student['birth_date'], "%d.%m.%Y").date()
        enrollment_date = datetime.strptime(student['enrollment_date'], "%d.%m.%Y").date()

        age = enrollment_date.year - birth_date.year

    # корректировка если день рождения ещё не наступил к моменту поступления
        if (enrollment_date.month, enrollment_date.day) < (birth_date.month, birth_date.day):
            age -= 1

        age_sum += age

    average_age = round(age_sum / len(loaded_data), 1)
    total['average_enrollment_age'] = average_age

    # работа с курсами
    courses = [course['courses'] for course in loaded_data]
    all_courses = [course for sublist in courses for course in sublist]
    course_count = Counter(all_courses)
    total["students_per_course"] = dict(course_count)

    # Создание и запись в JSON в файл
    with open("student_courses_report.json", "w") as report:
        json.dump(total, report)


total_reduce()
