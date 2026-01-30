# 1. Сумма цифр числа
#
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
#
# Данные:
#
# num = 43197
#
# Пример вывода:
#
# 24

num = 43197


def summ(numbers):
    result = [int(n) for n in str(numbers)]
    return sum(tuple(result))


print(summ(num))


def summ(numbers):
    if numbers < 10:
        return numbers
    return summ(numbers // 10) + (numbers % 10)


print(summ(num))


################################################################ 2 Option

def digit_sum(n):
    if n == 0:
        return 0
    number = n % 10
    another_nums = digit_sum(n // 10)
    result = number + another_nums
    return result


print(digit_sum(num))

# 2. Сумма вложенных чисел #
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.  #
# Данные:
#
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#
# Пример вывода:
#
# 28

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


def summ(arr):
    total = 0
    for n in arr:
        if isinstance(n, list):
            total += summ(n)
        else:
            total += n
    return total


print(summ(nested_numbers))


################################################################ 2 Option
def deep_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += deep_sum(item)
        else:
            total += item
    return total


print(deep_sum(nested_numbers))
