"""
1. План по дням недели

Напишите программу, которая помогает планировать дела.
Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.


Пример ввода:

Нажмите 'Enter' для получения плана:

Monday: Gym, Work, Read book

Нажмите 'Enter' для получения плана:

Tuesday: Meeting, Work, Study Python

...

Нажмите 'Enter' для получения плана:

Sunday: Family time, Rest

Нажмите 'Enter' для получения плана:

Monday: Gym, Work, Read book

Нажмите 'Enter' для получения плана: q
"""
weekly_schedule = {"Monday": ["Gym", "Work", "Read book"], "Tuesday": ["Meeting", "Work", "Study Python"],
                   "Wednesday": ["Shopping", "Work", "Watch movie"],
                   "Thursday": ["Work", "Call parents", "Play guitar"], "Friday": ["Work", "Dinner with friends"],
                   "Saturday": ["Hiking", "Rest"], "Sunday": ["Family time", "Rest"]}

from itertools import cycle


def planing(schedule):
    schedule_cycle = cycle(schedule.items())
    while True:
        key = input("Нажмите 'Enter' для получения плана:")
        if key == '':
            day, tasks = next(schedule_cycle)
            print(f"{day}: {', '.join(tasks)}")
            yield day, tasks
        else:
            print("Вы вышли из программы")
            break


planner = planing(weekly_schedule)
for _ in planner:
    pass

"""
2. Объединение списков продуктов

Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор, содержащий все продукты в нижнем регистре.
Выведите содержимое генератора.


fruits = ["Apple", "Banana", "Orange"]

vegetables = ["Carrot", "Tomato", "Cucumber"]

dairy = ["Milk", "Cheese", "Yogurt"]

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def to_combination(*products):
    n = 0
    while n < len(products):
        for val in products:
            for item in val:
                print(item.lower())
                yield item
                n += 1


gen = to_combination(fruits, vegetables, dairy)
for _ in gen:
    pass


# Ещё вариант, по-проще как мне кажется


def to_combination(*products):
    for category in products:
        for product in category:
            print(product.lower())
            yield product


gen = to_combination(fruits, vegetables, dairy)
for _ in gen:
    pass

"""
3. Комбинации одежды

Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все возможные комбинации
в формате "Clothe - Color - Size".

Данные:

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

Пример вывода:

T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L
"""

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]


def cloth_options(*categories):
    clothes, colors, sizes = categories
    for cloth in clothes:
        for color in colors:
            for size in sizes:
                yield f"{cloth} - {color} - {size}"


gen = cloth_options(clothes, colors, sizes)
for _ in gen:
    print(_)

# Второй вариант решения с модулем itertools

from itertools import product


def cloth_options(*categories):
    for combination in product(*categories):
        yield " - ".join(combination)


gen = cloth_options(clothes, colors, sizes)
for _ in gen:
    print(_)
