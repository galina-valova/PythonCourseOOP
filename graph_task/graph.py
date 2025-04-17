from collections import deque


class Graph:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise TypeError("Graph matrix must be list type, not", type(matrix).__name__)

        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("Rows of graph matrix must be list type, not", [type(row).__name__ for row in matrix])

        n_rows = len(matrix)
        max_n_cols = len(max(matrix, key=lambda x: len(x)))
        min_n_cols = len(min(matrix, key=lambda x: len(x)))

        if max_n_cols != min_n_cols or n_rows != max_n_cols:
            raise ValueError("Graph matrix must be square")

        matrix_values = [i for row in matrix for i in row]

        if not all(isinstance(value, int) for value in matrix_values):
            raise TypeError("Graph matrix values must be int")

        self.__matrix = matrix
        self.__size = len(matrix)

    def traverse_in_width(self, function):
        queue = deque()
        visited = [False] * self.__size

        for vertex in range(self.__size):
            if not visited[vertex]:
                queue.appendleft(vertex)
                visited[vertex] = True

                while queue:
                    current_vertex = queue.pop()
                    function(current_vertex)

                    for neighbor, vertex_neighbour in enumerate(self.__matrix[current_vertex]):
                        if vertex_neighbour == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.appendleft(neighbor)

    def traverse_in_depth(self, function):
        stack = deque()
        visited = [False] * self.__size

        for vertex in range(self.__size):
            if not visited[vertex]:
                stack.append(vertex)
                visited[vertex] = True

                while stack:
                    current_vertex = stack.pop()
                    function(current_vertex)

                    for neighbor, vertex_neighbour in enumerate(reversed(self.__matrix[current_vertex])):
                        index = self.__size - neighbor - 1

                        if vertex_neighbour == 1 and not visited[index]:
                            visited[index] = True
                            stack.append(index)

    def traverse_in_depth_with_recursion(self, function):
        visited = [False] * self.__size

        for vertex in range(self.__size):
            if not visited[vertex]:
                self.__visit_vertex(vertex, visited, function)

    def __visit_vertex(self, vertex, visited, function):
        function(vertex)
        visited[vertex] = True

        for neighbor, vertex_neighbour in enumerate(reversed(self.__matrix[vertex])):
            index = self.__size - neighbor - 1

            if vertex_neighbour == 1 and not visited[index]:
                self.__visit_vertex(index, visited, function)
