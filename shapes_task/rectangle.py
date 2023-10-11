from shapes_task.shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        sides_list = [width, height]

        if not all(isinstance(i, (int, float)) for i in sides_list):
            raise TypeError(f"Rectangle width and height must be numbers, not {[type(i).__name__ for i in sides_list]}")

        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        return f"Rectangle with sides: width length = {self.__width}, height length = {self.__height}"

    def __hash__(self):
        return hash((self.__width, self.__height))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__width == other.__width and self.__height == other.__height
