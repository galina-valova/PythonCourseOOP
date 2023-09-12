from shapes_task.shape import Shape


class Rectangle(Shape):
    def __init__(self, width_length, height_length):
        self.__width_length = width_length
        self.__height_length = height_length

    def get_width(self):
        return self.__width_length

    def get_height(self):
        return self.__height_length

    def get_area(self):
        return self.__width_length * self.__height_length

    def get_perimeter(self):
        return 2 * (self.__width_length + self.__height_length)

    def __repr__(self):
        return f"Rectangle with sides: width length = {self.__width_length}, height length = {self.__height_length}"

    def __hash__(self):
        return hash((self.__width_length, self.__height_length))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__width_length == other.__width_length and \
            self.__height_length == other.__height_length
