from shapes_task.square import Square
from shapes_task.triangle import Triangle
from shapes_task.rectangle import Rectangle
from shapes_task.circle import Circle


def get_shape_with_max_area(shapes):
    if len(shapes) == 0:
        raise ValueError("List of shapes is empty")

    return sorted(shapes, key=lambda x: x.get_area(), reverse=True)[0]


def get_shape_with_second_perimeter(shapes):
    if len(shapes) == 0:
        raise ValueError("List of shapes is empty")

    return sorted(shapes, key=lambda x: x.get_perimeter(), reverse=True)[1]


shapes_list = [
    Square(32),
    Triangle(1, 2, -1, 1, 0, 5),
    Rectangle(4, 5),
    Circle(7),
    Square(15),
    Triangle(-1, 2, 2, 3, 4, -3),
    Rectangle(7, 8),
    Circle(5.15)
]

print(get_shape_with_max_area(shapes_list), "has maximum area")
print(get_shape_with_second_perimeter(shapes_list), "has the second largest perimeter")
