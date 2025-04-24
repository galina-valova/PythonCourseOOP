from random import randint


class GameField:
    def __init__(self, nrow, ncol, nmines):
        self.__nrow = nrow
        self.__ncol = ncol
        self.__nmines = nmines
        self.__field = [
            [
                {"is_mine": False, "is_open": False, "is_flagged": False, "mines_around": 0} for _ in range(self.__ncol)
            ]
            for _ in range(self.__nrow)
        ]

    @property
    def field(self):
        return self.__field

    def set_mines(self):
        placed_mines = 0

        while placed_mines < self.__nmines:

            x = randint(0, self.__nrow - 1)
            y = randint(0, self.__ncol - 1)

            if not self.__field[x][y]["is_mine"]:
                self.__field[x][y]["is_mine"] = True

                placed_mines += 1

    def __get_neighbours(self, x, y):
        neighbours = []

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:

                if i == 0 and j == 0:
                    continue

                nx, ny = x + i, y + j

                if 0 <= nx < self.__nrow and 0 <= ny < self.__ncol:
                    neighbours.append((nx, ny))

        return neighbours

    def get_neighbours(self, x, y):
        return self.__get_neighbours(x, y)

    def __get_mines_indexes(self):
        mines_indexes = {"x": [], "y": []}

        for x in range(self.__nrow):
            for y in range(self.__ncol):

                if self.__field[x][y]["is_mine"]:
                    mines_indexes["x"].append(x)
                    mines_indexes["y"].append(y)
        return mines_indexes

    def get_mines_indexes(self):
        return self.__get_mines_indexes()

    def calculate_mines_around(self):
        mines_coordinates = self.__get_mines_indexes()

        for x, y in zip(mines_coordinates["x"], mines_coordinates["y"]):
            mines_neighbours = self.__get_neighbours(x, y)

            for neighbours in range(len(mines_neighbours)):
                cell_x = mines_neighbours[neighbours][0]
                cell_y = mines_neighbours[neighbours][1]

                if not self.__field[cell_x][cell_y]["is_mine"]:
                    self.__field[cell_x][cell_y]["mines_around"] += 1

    def __repr__(self):
        return f'{{{"\n".join(repr(self.__field[row]) for row in range(self.__nrow))}}}'
