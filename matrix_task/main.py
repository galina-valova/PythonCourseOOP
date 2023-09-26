from matrix_task.matrix import Matrix
from vector_task.vector import Vector

matrix = Matrix(2, 2)
matrix_1 = Matrix(matrix)
matrix_2 = Matrix([[1, 2, 4], [3, 5, 7], [7, 8, 9]])
matrix_3 = Matrix([Vector([3, 4, 5]), Vector([6, 8, 11]), Vector([8, 59, 0])])

matrix += Matrix([[5, 9], [11, 10]])

for i, row in enumerate([[1, 2], [4, 5]]):
    matrix_1[i] = row

if matrix_2.get_determinant() != 0:
    print("Matrix 2 has inverse matrix")

matrices_product = matrix @ matrix_1
transposed_matrices_product = matrix_1.get_transpose() @ matrix.get_transpose()

if matrices_product.get_determinant() == transposed_matrices_product.get_determinant():
    print("The transposed product of the matrices is equal to the product of the transposed matrices")
