""" 
1. Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.
у каждого объекта должны быть два поля: width и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.

Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь. 
"""

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

figure = Rectangle(5, 6)
print(f"Площадь: {figure.get_area()}")
figure.width = 7
figure.height = 9
print(f"Новая площадь: {figure.get_area()}")


""" 
2. Класс Counter

Реализуйте класс Counter, который представляет собой простой счётчик.
Счётчик должен начинаться с нуля.
Предусмотрите методы для увеличения и уменьшения значения на единицу, 
при этом при каждой операции должно отображаться новое значение счётчика.
Добавьте метод, возвращающий текущий результат.
Проверьте работу счётчика, выполнив несколько операций.
"""

class Counter:
    def __init__(self, count=0):
        self.count = count

    def increase(self):
        self.count += 1
        return f"Значение увеличено, текущее: {self.count}"

    def decrease(self):
        self.count -= 1
        return f"Значение уменьшено, текущее: {self.count}"
    
    def get_info(self):
        return f"Текущее значение: {self.count}"

counter = Counter()
print(counter.increase())
print(counter.increase())
print(counter.increase())
print(counter.decrease())
print(counter.get_info())