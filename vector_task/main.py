from vector_task.vector import Vector

vector = Vector(3, [1, 2, 3, 4, 5])
vector_1 = Vector(4, [1, 2, 3])
vector_2 = Vector(8)
vector_3 = Vector(vector_1)
vector_4 = Vector([1, 7, 4, 8])

vectors_sum = vector_3 + vector_2
vectors_sub = vectors_sum - vector_1

vector_5 = 4 * vector_3
vector_5.turn()

if vector_1 == vector_3:
    print("Vector 1 is equal to vector 3")

if vector_1.size < vector_2.size:
    print("Vector 1 has less number of components than vector 2")

vector_3 *= (1 / vector_3.norm)

for i in range(vector_2.size):
    vector_2[i] = i

print("Norm of vector 3:", vector_3.norm)
print("Sum of two vectors:", vectors_sum)
print("Subtraction of two vectors:", vectors_sub)
print("Turned vector 5:", vector_5)
print("Dot product:", Vector([1, 1, 1, 1]).get_dot_product(Vector([2, 2])))
print("Changed vector 2:", vector_2)
