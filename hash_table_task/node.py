class Node:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __iter__(self):
        return iter((self.__key, self.__value))

    def __repr__(self):
        return f"\"{self.key}\":{self.value}"
