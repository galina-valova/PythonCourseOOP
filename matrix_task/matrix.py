from vector_task.vector import Vector


class Matrix:
    def __init__(self, *args):
        arguments_length = len(args)

        if arguments_length == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            rows_number = args[0]
            columns_number = args[1]

            if rows_number < 0 and columns_number < 0:
                raise ValueError("Matrix dimensions must be positive integer, not", rows_number, columns_number)

            self.__rows = [Vector(columns_number) for _ in range(rows_number)]

        elif arguments_length == 1 and isinstance(args[0], Matrix):
            self.__rows = [Vector(vector) for vector in args[0].__rows]

        elif arguments_length == 1 and isinstance(args[0], list):
            rows_list = args[0]

            if all(isinstance(row, list) for row in rows_list):
                if sum([len(row) for row in rows_list]) > 0:
                    columns_number = len(max(rows_list, key=len))
                    self.__rows = [Vector(columns_number, row) for row in rows_list]
                else:
                    raise ValueError("List must contains at least one non-empty list")

            elif all(isinstance(row, Vector) for row in rows_list):
                if len(rows_list) > 0:
                    columns_number = max(rows_list, key=lambda x: x.size).size
                    self.__rows = [Vector(columns_number, list(row)) for row in rows_list]
                else:
                    raise ValueError("List of vectors must be non-empty")

            else:
                raise ValueError("Unsupported type of list elements")

        else:
            raise TypeError("Unsupported arguments type")

    @property
    def rows_number(self):
        return len(self.__rows)

    @property
    def columns_number(self):
        return self.__rows[0].size

    def __is_equal_sizes(self, other):
        return self.rows_number == other.rows_number and self.columns_number == other.columns_number

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
            if self.columns_number != other.size:
                raise ValueError(f"Incompatible matrix and vector sizes for multiplication."
                                 f" Matrix row length {self.columns_number} is not equal to vector length {other.size}")

            return Vector([row.get_dot_product(other) for row in self.__rows])

        raise TypeError("The second value must be number or Vector, not ", type(other))

    __rmul__ = __mul__

    def __iadd__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        if not self.__is_equal_sizes(other):
            raise ValueError(f"Incompatible matrix sizes for addition, your input is"
                             f"{self.rows_number} x {self.columns_number} and"
                             f"{other.rows_number} x {other.columns_number}")

        for i in range(self.rows_number):
            self.__rows[i] += other.__rows[i]

        return self

    def __add__(self, other):
        result = Matrix(self)
        result += other
        return result

    def __isub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        if not self.__is_equal_sizes(other):
            raise ValueError(f"Incompatible matrix sizes for subtraction, your input is"
                             f"{self.rows_number} x {self.columns_number} and"
                             f"{other.rows_number} x {other.columns_number}")

        for i in range(self.rows_number):
            self.__rows[i] -= other.__rows[i]

        return self

    def __sub__(self, other):
        result = Matrix(self)
        result -= other
        return result

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("The second value must be Matrix, not ", type(other))

        if self.columns_number != other.rows_number:
            raise ValueError(f"Incompatible matrix sizes for multiplication: number of columns {self.columns_number}"
                             f" is not equal to number of rows {other.rows_number}")

        transposed_other = Matrix(other).transpose()
        return Matrix([[row_1.get_dot_product(row_2) for row_2 in transposed_other.__rows] for row_1 in self.__rows])

    def transpose(self):
        self.__rows = [Vector(list(item)) for item in (zip(*self.__rows))]
        return self

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be int, not ", type(index))

        if not isinstance(value, (list, Vector)):
            raise TypeError("Value must be list or Vector, not ", type(index))

        if index >= self.rows_number or index < -self.rows_number:
            raise IndexError(f"Row index out of range. Index is {index}, "
                             f"index must be in [{-self.rows_number}, {self.rows_number})")

        if isinstance(value, list) and self.columns_number != len(value):
            raise ValueError(f"Incompatible rows length: matrix row length {self.columns_number} is not equal to"
                             f" row-vector length {len(value)}")

        elif isinstance(value, Vector) and self.columns_number != value.size:
            raise ValueError(f"Incompatible rows length: matrix row length {self.columns_number} is not equal to"
                             f" row-vector length {value.size}")

        self.__rows[index] = Vector(value)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int, not ", type(index))

        if index >= self.rows_number or index < -self.rows_number:
            raise IndexError(f"Row index out of range. Index is {index}, "
                             f"index must be in [{-self.rows_number}, {self.rows_number})")

        return Vector(self.__rows[index])

    def get_column(self, index):
        if not isinstance(index, int):
            raise TypeError("Item must be int, not ", type(index))

        if index >= self.columns_number or index < -self.columns_number:
            raise IndexError(f"Column index out of range. Index is {index}, "
                             f"index must be in [{-self.columns_number}, {self.columns_number})")

        return Vector([row[index] for row in self.__rows])

    def __get_algebraic_complement(self, row_item_index, col_item_index):
        if row_item_index >= self.rows_number or col_item_index >= self.rows_number:
            raise IndexError("Indexes out of range")

        if self.rows_number < 2 or self.columns_number < 2:
            raise TypeError("Requires a matrix, not a vector")

        matrix_elements = []

        for i in range(self.rows_number):
            for j in range(self.columns_number):

                if i != row_item_index:
                    if j != col_item_index:
                        matrix_elements.append(self.__rows[i][j])

        return Matrix([Vector(matrix_elements[i:i + (self.rows_number - 1)]) for i in range(0, len(matrix_elements),
                                                                                            (self.rows_number - 1))])

    def get_determinant(self):
        if self.rows_number != self.columns_number:
            raise TypeError(f"Matrix must be square. Your matrix has size {self.rows_number} x {self.columns_number}")

        if self.rows_number == 1 and self.columns_number == 1:
            return self[0][0]

        if self.rows_number == 2 and self.columns_number == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]

        else:
            determinant = 0

            for i in range(self.rows_number):
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
