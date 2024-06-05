from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        arguments_count = len(args)

        if arguments_count == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            rows_count = args[0]
            columns_count = args[1]

            if rows_count < 0 or columns_count < 0:
                raise ValueError("Matrix dimensions must be positive integer, not", rows_count, columns_count)

            self.__rows = [Vector(columns_count) for _ in range(rows_count)]
            return

        if arguments_count == 1 and isinstance(args[0], Matrix):
            self.__rows = [Vector(vector) for vector in args[0].__rows]
            return

        if arguments_count == 1 and isinstance(args[0], list):
            rows_list = args[0]

            if all(isinstance(row, list) for row in rows_list):
                if sum([len(row) for row in rows_list]) <= 0:
                    raise ValueError("List must contains at least one non-empty list")

                columns_count = len(max(rows_list, key=len))
                self.__rows = [Vector(columns_count, row) for row in rows_list]

            elif all(isinstance(row, Vector) for row in rows_list):
                if len(rows_list) <= 0:
                    raise ValueError("List of vectors must be non-empty")

                columns_count = max(rows_list, key=lambda x: x.size).size
                self.__rows = [Vector(columns_count, list(row)) for row in rows_list]

            else:
                raise ValueError("Unsupported type of list elements")
            return

        else:
            raise TypeError("Unsupported arguments type")

    @property
    def rows_count(self):
        return len(self.__rows)

    @property
    def columns_count(self):
        return self.__rows[0].size

    def __check_dimensions(self, other):
        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            raise ValueError("Incompatible matrix sizes for operation: matrix sizes should be equal"
                             f"{self.rows_count} x {self.columns_count} and "
                             f"{other.rows_count} x {other.columns_count}")

    def __check_index(self, index):
        if index < -self.rows_count or index >= self.rows_count:
            raise IndexError(f"Row index out of range. Index is {index}, "
                             f"index must be in [{-self.rows_count}, {self.rows_count}]")

    def __imul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("The second value must be number, not ", type(other))

        for item in self.__rows:
            item *= other

        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Matrix(self)
            result *= other
            return result

        if isinstance(other, Vector):
            if self.columns_count != other.size:
                raise ValueError("Incompatible matrix and vector sizes for multiplication. "
                                 f" Matrix row length {self.columns_count} is not equal to vector length {other.size}")

            return Vector([row.get_dot_product(other) for row in self.__rows])

        raise TypeError("The second value must be number or Vector, not ", type(other))

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        self.__check_dimensions(other)

        for i in range(self.rows_count):
            self.__rows[i] += other.__rows[i]

        return self

    def __add__(self, other):
        self.__check_dimensions(other)
        result = Matrix(self)
        result += other
        return result

    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        self.__check_dimensions(other)

        for i in range(self.rows_count):
            self.__rows[i] -= other.__rows[i]

        return self

    def __sub__(self, other):
        self.__check_dimensions(other)
        result = Matrix(self)
        result -= other
        return result

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        if self.columns_count != other.rows_count:
            raise ValueError(f"Incompatible matrix sizes for multiplication: number of columns {self.columns_count}"
                             f" is not equal to number of rows {other.rows_count}")

        transposed_other = Matrix(other).transpose()
        return Matrix([[row_1.get_dot_product(row_2) for row_2 in transposed_other.__rows] for row_1 in self.__rows])

    def transpose(self):
        self.__rows = [Vector(list(item)) for item in zip(*self.__rows)]
        return self

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be int, not ", type(index))

        if not isinstance(value, (list, Vector)):
            raise TypeError("Value must be list or Vector, not ", type(index))

        if not all(isinstance(item, (int, float)) for item in value):
            raise TypeError("List or Vector must be contains number, not ", [type(item).__name__ for item in value])

        self.__check_index(index)

        if isinstance(value, list) and self.columns_count != len(value):
            raise ValueError(f"Incompatible rows length: matrix row length {self.columns_count} is not equal to"
                             f" row-vector length {len(value)}")

        if isinstance(value, Vector) and self.columns_count != value.size:
            raise ValueError(f"Incompatible rows length: matrix row length {self.columns_count} is not equal to"
                             f" row-vector length {value.size}")

        self.__rows[index] = Vector(value)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int, not ", type(index))

        self.__check_index(index)

        return Vector(self.__rows[index])

    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError("Item must be int, not ", type(index))

        if index < -self.columns_count or index >= self.columns_count:
            raise IndexError(f"Column index out of range. Index is {index}, "
                             f"index must be in [{-self.columns_count}, {self.columns_count}]")

        return Vector([row[index] for row in self.__rows])

    def __get_algebraic_complement(self, row_item_index, col_item_index):
        matrix_elements = []

        for i in range(self.rows_count):
            for j in range(self.columns_count):
                if i != row_item_index:
                    if j != col_item_index:
                        matrix_elements.append(self.__rows[i][j])

        return Matrix([Vector(matrix_elements[i:i + (self.rows_count - 1)]) for i in range(0, len(matrix_elements),
                                                                                            (self.rows_count - 1))])

    def get_determinant(self):
        if self.rows_count != self.columns_count:
            raise TypeError("Matrix must be square. "
                            f"The input matrix has size {self.rows_count} x {self.columns_count}")

        if self.rows_count == 1:
            return self[0][0]

        if self.rows_count == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        determinant = 0

        for i in range(self.rows_count):
            determinant += (-1) ** i * self.__rows[0][i] * self.__get_algebraic_complement(0, i).get_determinant()

        return determinant

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.__rows == other.__rows

    def __hash__(self):
        return hash(tuple(self.__rows))

    def __repr__(self):
        return f'{{{", ".join(repr(row) for row in self.__rows)}}}'
