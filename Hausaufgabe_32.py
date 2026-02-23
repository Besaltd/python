
""" 1. Фабрика функций округления

Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.

Пример вызова: 

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода: 

3.14
2.72
10.0 
"""


def make_rounder(char_qty):
    def rounded(number):
        return round(number, char_qty)
    return rounded

round2 = make_rounder(2)
print(round2(3.14159))
print(round2(2.71828))

round0 = make_rounder(0)
print(round0(9.999))


""" 2. Расширяемый логгер событий

Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие c текущим временем (если оно передано) 
и возвращать весь список событий.

Пример вызова: 

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)

Пример вывода: 

Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
"""

import time

def create_logger():
    events = list()
    def logger(event=None):
        if event is not None:
            events.append(f"{event}: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}")
        return events
    return logger


log = create_logger()

log("Загрузка данных")
log("Сохранение файла")
log("Обработка завершена")

for event in log():
    print(event)


""" 
3. Рамка вокруг вывода
Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -,
выводя по строке до и после вызова функции.
Пример декорируемой функции: 

def say_hello():
    print("Привет, игрок!")

Пример вывода: 

--------------------------------------------------
Привет, игрок!
--------------------------------------------------
 """


def say_hello(func):
    def wrapper(*args):
        print('-' * 50)
        result = func()
        print('-' * 50)
        return result
    return wrapper

@say_hello
def framed():
    print("Привет, игрок!")

if __name__ == "__main__":
    framed()