from shapes_task.shape import Shape
from math import pi


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def get_width(self):
        return 2 * self.__radius

    def get_height(self):
        return 2 * self.__radius

    def get_area(self):
        return pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.__radius

    def __repr__(self):
        return f"Circle with radius {self.__radius}"

    def __hash__(self):
        return self.__radius

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__radius == other.__radius
