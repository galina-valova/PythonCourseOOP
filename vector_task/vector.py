from math import sqrt


class Vector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            if args[0] <= 0:
                raise ValueError(f"Vector size n must be > 0. Your input is n = {args[0]}")

            self.__components = [0] * args[0]

        elif len(args) == 1 and isinstance(args[0], Vector):
            self.__components = list(args[0].__components)

        elif len(args) == 1 and isinstance(args[0], list):
            if len(args[0]) == 0:
                raise ValueError(f"Vector size n must be > 0. Your input is n = {args[0]}")

            self.__components = list(args[0])

        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], list):

            if args[0] <= 0:
                raise ValueError(f"Vector size n must be > 0. Your input is n = {args[0]}")

            if len(args[1]) < args[0]:
                self.__components = args[1] + [0] * (args[0] - len(args[1]))
            else:
                self.__components = list(args[1])
        else:
            raise TypeError("Unsupported arguments type")

    @property
    def norm(self):
        return sqrt(sum(component ** 2 for component in self.__components))

    @property
    def size(self):
        return len(self.__components)

    def __add__(self, other):
        max_vector = self if self.size >= other.size else other
        min_vector = self if self.size < other.size else other
        result = list(max_vector.__components)

        for i, item in enumerate(min_vector.__components):
            result[i] += item

        return Vector(result)

    def __sub__(self, other):
        other_copy = Vector(other)
        other_copy.turn()
        return self + other_copy

    def __mul__(self, number):
        self_copy = Vector(self)
        self_copy.__components = [x * number for x in self_copy.__components]

        return Vector(self_copy)

    __rmul__ = __mul__

    def turn(self):
        self.__components = [-x for x in self.__components]

    def dot_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError("The second value must be Vector")

        return sum(item_1 * item_2 for item_1, item_2 in zip(self.__components, other.__components))

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Item must be int")

        if len(self.__components) <= item:
            raise IndexError("Vector index out of range")

        return self.__components[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Key must be int")

        if len(self.__components) <= key:
            raise IndexError("Vector index out of range")

        self.__components[key] = value

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__components == other.__components

    def __hash__(self):
        return hash(tuple(self.__components))

    def __repr__(self):
        return f'{{{", ".join(repr(component) for component in self.__components)}}}'
