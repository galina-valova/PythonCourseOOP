from shape_task.shape import Square, Triangle, Rectangle, Circle


def get_max_shape_area(shapes):
    return sorted(shapes, key=lambda x: x.get_area(), reverse=True)[0]


def get_second_shape_perimeter(shapes):
    return sorted(shapes, key=lambda x: x.get_perimeter(), reverse=True)[1]


shapes_list = [
    Square(12),
    Triangle(1, 5, 2, 5, 4, 6),
    Rectangle(4, 5),
    Circle(7),
    Square(15),
    Triangle(-1, 2, 2, 3, 4, -3),
    Rectangle(7, 8),
    Circle(5.15)
]

print(get_max_shape_area(shapes_list), "has maximum area")
print(get_second_shape_perimeter(shapes_list), "has the second largest perimeter")
