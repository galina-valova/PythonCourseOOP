from graph_task.graph import Graph

matrix_1 = [[0, 1, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0]]

matrix_2 = [[0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]]

graph_1 = Graph(matrix_1)
graph_1.traverse_in_depth(print)
print("======")
graph_1.traverse_in_depth_with_recursion(print)
print("======")
graph_1.traverse_in_width(print)
