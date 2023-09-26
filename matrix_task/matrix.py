from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            n_rows = args[0]
            n_cols = args[1]

            if n_rows > 0 and n_cols > 0:
                self.__rows = [Vector(n_cols)] * n_rows
            else:
                raise ValueError("Matrix dimensions must be positive integer")

        elif len(args) == 1 and isinstance(args[0], Matrix):
            self.__rows = list(args[0].__rows)

        elif len(args) == 1 and isinstance(args[0], list):
            components_list = args[0]

            if all(isinstance(item, list) for item in components_list) \
                    and sum([len(item) for item in components_list]) > 0:
                n_cols = len(max(components_list, key=len))
                self.__rows = [Vector(n_cols, item) for item in components_list]

            elif all(isinstance(item, Vector) for item in components_list) \
                    and sum([item.size for item in components_list]) > 0:
                n_cols = max(components_list, key=lambda x: x.size).size
                self.__rows = [Vector(n_cols, list(item)) for item in components_list]
            else:
                raise ValueError("Lists or vectors must be not empty")

        else:
            raise TypeError("Unsupported arguments type")

    @property
    def size(self):
        n_rows = len(self.__rows)
        n_cols = max(self.__rows, key=lambda x: x.size).size
        return n_rows, n_cols

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self_copy = Matrix(self)
            self_copy.__rows = [row * other for row in self_copy.__rows]
            return Matrix(self_copy)

        if isinstance(other, Vector):
            if self.size[1] != other.size:
                raise ValueError("Incompatible matrix and vector sizes for multiplication")

            return Vector([row.get_dot_product(other) for row in self.__rows])

        raise TypeError("The second value must be number")

    __rmul__ = __mul__

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix")

        if self.size != other.size:
            raise ValueError("Incompatible matrix sizes for addition")

        self.__rows = [row_1 + row_2 for row_1, row_2 in zip(self.__rows, other.__rows)]
        return self

    def __add__(self, other):
        return Matrix(self).__iadd__(other)

    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix")

        if self.size != other.size:
            raise ValueError("Incompatible matrix sizes for subtraction")

        self.__rows = [row_1 - row_2 for row_1, row_2 in zip(self.__rows, other.__rows)]
        return self

    def __sub__(self, other):
        return Matrix(self).__isub__(other)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix")

        if self.size[1] != other.size[0]:
            raise ValueError("Incompatible matrix sizes for multiplication")

        return Matrix([[row.get_dot_product(Vector(list(col))) for col in zip(*other.__rows)] for row in self.__rows])

    def get_transpose(self):
        self.__rows = [Vector(list(item)) for item in (zip(*self.__rows))]
        return self

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Key must be int")

        if index >= self.size[0] or index < -self.size[0]:
            raise IndexError(f"Row index out of range. Index is {index}, "
                             f"index must be in [{-self.size[0]}, {self.size[0]})")

        if isinstance(value, list) and self.size[1] != len(value):
            raise ValueError("Incompatible row length")

        elif isinstance(value, Vector) and self.size[1] != value.size:
            raise ValueError("Incompatible row length")

        self.__rows[index] = Vector(value)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Item must be int")

        if index >= self.size[0] or index < -self.size[0]:
            raise IndexError(f"Row index out of range. Index is {index}, "
                             f"index must be in [{-self.size[0]}, {self.size[0]})")

        return self.__rows[index]

    def get_col(self, index):
        if not isinstance(index, int):
            raise TypeError("Item must be int")

        if index >= self.size[1] or index < -self.size[1]:
            raise IndexError(f"Column index out of range. Index is {index}, "
                             f"index must be in [{-self.size[1]}, {self.size[1]})")

        return Vector([row[index] for row in self.__rows])

    def get_algebraic_complement(self, row_item_index, col_item_index):
        if row_item_index >= self.size[0] or col_item_index >= self.size[1]:
            raise IndexError("Indexes out of range")

        if self.size[0] < 2 or self.size[1] < 2:
            raise TypeError("Requires a matrix, not a vector")

        matrix_elements = []

        for i in range(self.size[0]):
            for j in range(self.size[1]):

                if i != row_item_index:
                    if j != col_item_index:
                        matrix_elements.append(self.__rows[i][j])

        return Matrix([Vector(matrix_elements[i:i + (self.size[0] - 1)]) for i in range(0, len(matrix_elements),
                                                                                        (self.size[0] - 1))])

    def get_determinant(self):
        if self.size[0] != self.size[1]:
            raise TypeError("Incompatible matrix for calculate determinant")

        if self.size == (1, 1):
            return self[0][0]

        if self.size == (2, 2):
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        else:
            determinant = 0

            for j in range(self.size[0]):
                determinant += (-1) ** j * self.__rows[0][j] * self.get_algebraic_complement(0, j).get_determinant()

            return determinant

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__rows == other.__rows

    def __hash__(self):
        return hash(tuple(self.__rows))

    def __repr__(self):
        return f'{{{", ".join(repr(row) for row in self.__rows)}}}'
