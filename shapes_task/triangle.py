from shapes_task.shape import Shape
from math import sqrt


class Triangle(Shape):
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        coordinates_list = [x_1, y_1, x_2, y_2, x_3, y_3]

        if not all(isinstance(i, (int, float)) for i in coordinates_list):
            raise TypeError(f"Points must be numbers, not {[type(i).__name__ for i in coordinates_list]}")

        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    def get_width(self):
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self):
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    @staticmethod
    def get_length_side(x_1, x_2, y_1, y_2):
        return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

    def get_area(self):
        return abs((self.__x_1 - self.__x_3) * (self.__y_2 - self.__y_3) -
                   (self.__y_1 - self.__y_3) * (self.__x_2 - self.__x_3)) / 2

    def get_perimeter(self):
        side_1_length = self.get_length_side(self.__x_1, self.__x_2, self.__y_1, self.__y_2)
        side_2_length = self.get_length_side(self.__x_2, self.__x_3, self.__y_2, self.__y_3)
        side_3_length = self.get_length_side(self.__x_1, self.__x_3, self.__y_1, self.__y_3)
        return side_1_length + side_2_length + side_3_length

    def __repr__(self):
        return f"Triangle with vertices ({self.__x_1}, {self.__y_1}), ({self.__x_2}, " \
               f"{self.__y_2}), ({self.__x_3}, {self.__y_3})"

    def __hash__(self):
        return hash((self.__x_1, self.__x_2, self.__x_3, self.__y_1, self.__y_2, self.__y_3))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and \
            self.__x_2 == other.__x_2 and self.__y_2 == other.__y_2 and \
            self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3
