from shapes_task.shape import Shape


class Square(Shape):
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError(f"Side length must be number, not {type(side_length).__name__}")

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

        return self.__side_length == other.__side_length
