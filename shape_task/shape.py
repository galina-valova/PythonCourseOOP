from abc import ABC, abstractmethod
from math import sqrt, pi


class Shape(ABC):
    @abstractmethod
    def get_width(self): pass

    @abstractmethod
    def get_height(self): pass

    @abstractmethod
    def get_area(self): pass

    @abstractmethod
    def get_perimeter(self): pass


class Square(Shape):
    def __init__(self, side_length):
        self.__side_length = side_length

    def get_width(self):
        return self.__side_length

    def get_height(self):
        return self.__side_length

    def get_area(self):
        return self.__side_length ** 2

    def get_perimeter(self):
        return 4 * self.__side_length

    def __repr__(self):
        return f"Square with side length {self.__side_length}"

    def __hash__(self):
        return self.__side_length

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return self.__side_length == other.__side_length


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.__x_1, self.__y_1 = x_1, y_1
        self.__x_2, self.__y_2 = x_2, y_2
        self.__x_3, self.__y_3 = x_3, y_3

    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    def get_area(self):
        return ((self.__x_1 - self.__x_3) * (self.__y_2 - self.__y_3) -
                (self.__y_1 - self.__y_3) * (self.__x_2 - self.__x_3)) / 2

    def get_perimeter(self):
        side_1 = sqrt((self.__x_2 - self.__x_1) ** 2 + (self.__y_2 - self.__y_1) ** 2)
        side_2 = sqrt((self.__x_3 - self.__x_2) ** 2 + (self.__y_3 - self.__y_2) ** 2)
        side_3 = sqrt((self.__x_3 - self.__x_1) ** 2 + (self.__y_3 - self.__y_1) ** 2)
        return side_1 + side_2 + side_3

    def __repr__(self):
        return f"Triangle with vertices ({self.__x_1}, {self.__y_1}), ({self.__x_2}, " \
               f"{self.__y_2}), ({self.__x_3}, {self.__y_3})"

    def __hash__(self):
        return hash((self.__x_1, self.__x_2, self.__x_3, self.__y_1, self.__y_2, self.__y_3))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return (self.__x_1, self.__y_1) == (other.__x_1, other.__y_1) \
                   and (self.__x_2, self.__y_2) == (other.__x_2, other.__y_2) \
                   and (self.__x_3, self.__y_3) == (other.__x_3, other.__y_3)


class Rectangle(Shape):
    def __init__(self, side_1_length, side_2_length):
        self.__side_1_length = side_1_length
        self.__side_2_length = side_2_length

    def get_width(self):
        return self.__side_1_length

    def get_height(self):
        return self.__side_2_length

    def get_area(self):
        return self.__side_1_length * self.__side_2_length

    def get_perimeter(self):
        return 2 * (self.__side_1_length + self.__side_2_length)

    def __repr__(self):
        return f"Rectangle with side lengths {self.__side_1_length}, {self.__side_2_length}"

    def __hash__(self):
        return hash((self.__side_1_length, self.__side_2_length))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        else:
            return (self.__side_1_length, self.__side_2_length) == (other.__side_1_length, other.__side_2_length)


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
        else:
            return self.__radius == other.__radius
