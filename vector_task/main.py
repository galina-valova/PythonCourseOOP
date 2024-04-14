from vector_task.vector import Vector

vector_1 = Vector(3, [1, 2, 3, 4, 5])
vector_2 = Vector(4, [1, 2, 3])
vector_3 = Vector(8)
vector_4 = Vector(vector_1)
vector_5 = Vector([1, 7, 4, 8])

vectors_sum = vector_3 + vector_4
print("Sum of two vectors:", vectors_sum)

vectors_difference = vectors_sum - vector_2
print("Vectors difference:", vectors_difference)

vector_6 = 4 * vector_4
vector_6.turn()
print("Turned vector 6:", vector_6)

vector_2 += vector_5

if vector_2 == vector_4:
    print("Vector 2 is equal to vector 4")

if vector_2.size < vector_3.size:
    print("Vector 2 has less number of components than vector 3")

vector_4 *= 1 / vector_4.norm
print("Norm of vector 4:", vector_4.norm)

for i in range(vector_3.size):
    vector_3[i] = i

print("Changed vector 3:", vector_3)
print("Dot product:", Vector([1, 1, 1, 1]).get_dot_product(Vector([2, 2])))
