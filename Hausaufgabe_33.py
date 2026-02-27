""" 1. Среднее время выполнения

Создайте декоратор measure_time, который измеряет и 
выводит среднее время выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или расчёты. 
"""

import time

def measure_time(func):
    def wrapper():
        times = []
        for _ in range(5):
            start = time.time()
            result = func()
            end = time.time()
            times.append(end - start)
        average = sum(times) / len(times)
        print(f"Среднее время выполнения для 5 раз: {round(average, 2)} секунд")
        print(f"Результат: {func()}")
        return result
    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10000000):
        total += i
    return total

compute()



""" 2. Среднее время выполнения c количеством вызовов

Доработайте декоратор measure_time, чтобы он принимал параметр repeats — количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее время выполнения. 
"""

import time

def measure_time(repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeats):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                times.append(end - start)
            average = sum(times) / len(times)
            print(f"Среднее время выполнения для {repeats} вызовов: {round(average, 2)} секунд")
            print(f"Результат: {result}")
            return average
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10000000):
        total += i
    return total

compute()