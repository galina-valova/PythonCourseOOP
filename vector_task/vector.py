from math import sqrt


class Vector:
    def __init__(self, *args):
        arguments_length = len(args)

        if arguments_length > 2 or arguments_length == 0:
            raise ValueError(f"Invalid number of arguments, your input is {arguments_length}")

        if arguments_length == 1 and isinstance(args[0], int):
            vector_size = args[0]

            if vector_size <= 0:
                raise ValueError(f"Vector size must be > 0. Your input is {vector_size}")

            self.__components = [0] * vector_size

        elif arguments_length == 1 and isinstance(args[0], Vector):
            vector = args[0]
            self.__components = list(vector.__components)

        elif arguments_length == 1 and isinstance(args[0], list):
            components_list = args[0]

            if len(components_list) == 0:
                raise ValueError(f"Vector size must be > 0. Your input is {components_list}")

            if not all(isinstance(item, (int, float)) for item in components_list):
                raise TypeError(f"Vector components must be numbers, not"
                                f"{[type(item).__name__ for item in components_list]}")

            self.__components = list(components_list)

        elif arguments_length == 2 and isinstance(args[0], int) and isinstance(args[1], list):
            vector_size = args[0]
            components_list = args[1]

            if vector_size <= 0:
                raise ValueError(f"Vector size must be > 0. Your input is {vector_size}")

            if not all(isinstance(item, (int, float)) for item in components_list):
                raise TypeError(f"Vector components must be numbers, not"
                                f"{[type(item).__name__ for item in components_list]}")

            if len(components_list) >= vector_size:
                self.__components = components_list[:vector_size]
            else:
                self.__components = components_list + [0] * (vector_size - len(components_list))

        else:
            raise TypeError("Unsupported arguments")

    @property
    def norm(self):
        return sqrt(sum(component ** 2 for component in self.__components))

    @property
    def size(self):
        return len(self.__components)

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"The second value must be Vector, not {type(other).__name__}")

        min_vector_size = min(self.size, other.size)

        for i in range(min_vector_size):
            self.__components[i] += other.__components[i]

        if self.size < other.size:
            size_delta = other.size - self.size

            for i in range(size_delta):
                self.__components.append(other.__components[min_vector_size + i])

        return self

    def __add__(self, other):
        result = Vector(self)
        result += other
        return result

    def __isub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"The second value must be Vector, not {type(other).__name__}")

        min_vector_size = min(self.size, other.size)

        for i in range(min_vector_size):
            self.__components[i] -= other.__components[i]

        if self.size < other.size:
            size_delta = other.size - self.size

            for i in range(size_delta):
                self.__components.append(-other.__components[min_vector_size + i])

        return self

    def __sub__(self, other):
        result = Vector(self)
        result -= other
        return result

    def __imul__(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError(f"The second value must be number, not {type(number).__name__}")

        for i in range(self.size):
            self.__components[i] *= number

        return self

    def __mul__(self, number):
        result = Vector(self)
        result *= number
        return result

    __rmul__ = __mul__

    def turn(self):
        for i in range(self.size):
            self[i] *= -1

    def get_dot_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Argument must be Vector, not {type(other).__name__}")

        return sum(item_1 * item_2 for item_1, item_2 in zip(self.__components, other.__components))

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if index >= len(self.__components) or index < -len(self.__components):
            raise IndexError(f"Vector index out of range. Index is {index}, "
                             f"index must be in [{-self.size}, {self.size})")

        return self.__components[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be number, not {type(value).__name__}")

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
