from matrix_task.matrix import Matrix
from vector_task.vector import Vector

matrix_1 = Matrix(2, 2)
matrix_2 = Matrix([[4, 3], [7, 5]])
matrix_3 = Matrix([Vector([3, -4, 7]), Vector([6, -8, 0]), Vector([-8, 59])])
matrix_4 = Matrix(matrix_1)

matrix_4[0] = Vector([2, 5])
print("matrix_4", matrix_4)

matrix_5 = matrix_2 + matrix_4
print("Sum of two matrices:", matrix_5)

if matrix_3.get_determinant() > 0:
    print("Transposed matrix_5:", matrix_5.transpose())

matrix_6 = matrix_2 @ matrix_4 * 2
print("Product of matrix_2 and matrix_4 =", matrix_6)
