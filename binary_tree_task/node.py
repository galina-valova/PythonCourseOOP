class Node:
    def __init__(self, data):
        if not isinstance(data, int | float):
            raise TypeError("Node data must be numeric, not", type(data).__name__)

        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    def __repr__(self):
        return f"{self.data}"
