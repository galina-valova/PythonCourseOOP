from math import sqrt


class Vector:
    def __init__(self, *args):
        if len(args) > 2 or len(args) == 0:
            raise ValueError("Invalid number of arguments")

        if len(args) == 1 and isinstance(args[0], int):
            n = args[0]

            if n <= 0:
                raise ValueError(f"Vector size must be > 0. Your input is {n}")

            self.__components = [0] * n

        elif len(args) == 1 and isinstance(args[0], Vector):
            vector = args[0]
            self.__components = list(vector.__components)

        elif len(args) == 1 and isinstance(args[0], list):
            components_list = args[0]

            if len(components_list) == 0:
                raise ValueError(f"Vector size must be > 0. Your input is {components_list}")

            if not all(isinstance(item, (int, float)) for item in components_list):
                raise TypeError("Vector components must be numbers")

            self.__components = list(components_list)

        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], list):
            n = args[0]
            components_list = args[1]

            if n <= 0:
                raise ValueError(f"Vector size must be > 0. Your input is {n}")

            if not all(isinstance(item, (int, float)) for item in components_list):
                raise TypeError("Vector components must be numbers")

            if len(components_list) >= n:
                self.__components = components_list[:n]
            else:
                self.__components = components_list + [0] * (n - len(components_list))

        else:
            raise TypeError("Unsupported arguments type")

    @property
    def norm(self):
        return sqrt(sum(component ** 2 for component in self.__components))

    @property
    def size(self):
        return len(self.__components)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The second value must be Vector")

        max_vector = self if self.size >= other.size else other
        min_vector = self if self.size < other.size else other
        result = Vector(max_vector.__components)

        for i, item in enumerate(min_vector):
            result[i] += item

        return result

    def __add__(self, other):
        return Vector(self).__iadd__(other)

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The second value must be Vector")

        result = Vector(other.size, self.__components) if self.size <= other.size else self
        subtrahend = other if self.size <= other.size else Vector(self.size, other.__components)

        for i, item in enumerate(subtrahend):
            result[i] -= item

        return result

    def __sub__(self, other):
        return Vector(self).__isub__(other)

    def __mul__(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError("The second value must be number")

        self_copy = Vector(self)
        self_copy.__components = [x * number for x in self_copy.__components]
        return Vector(self_copy)

    __rmul__ = __mul__

    def turn(self):
        for i in range(self.size):
            self[i] *= -1

    def get_dot_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The second value must be Vector")

        return sum(item_1 * item_2 for item_1, item_2 in zip(self.__components, other.__components))

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index >= len(self.__components) or index < -len(self.__components):
            raise IndexError(f"Vector index out of range. Index is {index}, "
                             f"index must be in [{-self.size}, {self.size})")

        return self.__components[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index >= len(self.__components) or index < -len(self.__components):
            raise IndexError(f"Vector index out of range. Index is {index}, "
                             f"index must be in [{-self.size}, {self.size})")

        self.__components[index] = value

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    def __repr__(self):
        return f'{{{", ".join(repr(component) for component in self.__components)}}}'
