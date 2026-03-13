from abc import ABC, abstractmethod
import math


class InvalidSizeError(ValueError):
    """Incorrect figure size"""
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("Radius must be positive.")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, height, width):
        if width <= 0 or height <= 0:
            raise IndentationError("Width and height must be positive")
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width


shapes = [Circle(12), Rectangle(68, 33)]

for shape in shapes:
    print(f"Area {shape.__class__.__name__}: {shape.area:.2f}")


