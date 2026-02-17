"""
1. Генератор Фибоначчи

Создайте генератор, который генерирует последовательность Фибоначчи бесконечно,
возвращая по одному числу за раз.

Последовательность Фибоначчи — это ряд чисел, где каждое следующее число равно сумме двух предыдущих.
Начинается с 0 и 1.
"""


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()

for _ in range(10):
    print(next(gen))

"""
2. Генератор уникальных элементов

Создайте генератор, который принимает список элементов и выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке.
"""

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


def uniq_generate(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
            yield n


for _ in uniq_generate(data):
    print(_)


# второй вариант с dict.fromkeys()

def uniq_generate(nums):
    yield from dict.fromkeys(nums)


for _ in uniq_generate(data):
    print(_)
