from minesweeper_task.model.cell_status import CellStatus
from minesweeper_task.model.game_field import GameField
from minesweeper_task.model.players import Players
from minesweeper_task.model.timer import Timer


class GameModel:
    def __init__(self):
        self.__field = None
        self.__timer = Timer()

    @property
    def timer(self):
        return self.__timer

    def set_game_data(self, nrow, ncol, nmines):
        self.__field = GameField(nrow, ncol, nmines)
        self.__field.set_mines()
        self.__field.calculate_mines_around()

    def toggle_flag(self, x, y):
        cell = self.__field.field[x][y]

        if not cell["is_open"]:
            cell["is_flagged"] = not cell["is_flagged"]

        toggled_cells_coordinate = {"x": x, "y": y, "status": cell["is_flagged"]}
        return toggled_cells_coordinate

    def open_cell(self, x, y):
        cell = self.__field.field[x][y]
        opened_cells_coordinate = {"x": [x], "y": [y], "status": [cell["mines_around"]]}

        if cell["is_flagged"]:
            return

        if cell["is_mine"]:
            mines_coordinates = self.__field.get_mines_indexes()
            opened_cells_coordinate["x"] = mines_coordinates["x"]
            opened_cells_coordinate["y"] = mines_coordinates["y"]
            opened_cells_coordinate["status"] = [CellStatus.MINE] * len(opened_cells_coordinate["x"])
        else:
            cell["is_open"] = True
            if cell["mines_around"] == 0:
                self.open_neighbours(x, y, opened_cells_coordinate)

        return opened_cells_coordinate

    def open_neighbours(self, x, y, opened_cells_coordinate):
        mines_neighbours = self.__field.get_neighbours(x, y)

        for neighbours in range(len(mines_neighbours)):
            cell_x = mines_neighbours[neighbours][0]
            cell_y = mines_neighbours[neighbours][1]
            cell = self.__field.field[cell_x][cell_y]

            if not cell["is_open"] and not cell["is_flagged"]:
                cell["is_open"] = True
                opened_cells_coordinate["x"].append(cell_x)
                opened_cells_coordinate["y"].append(cell_y)
                opened_cells_coordinate["status"].append(cell["mines_around"])

                if cell["mines_around"] == 0:
                    self.open_neighbours(cell_x, cell_y, opened_cells_coordinate)

    def get_unopened_cells(self):
        return [
            (x, y) for x, row in enumerate(self.__field.field)
            for y, cell in enumerate(row) if not cell["is_open"] and not cell["is_mine"]
        ]

    def get_mined_cells(self):
        return [
            (x, y) for x, row in enumerate(self.__field.field)
            for y, cell in enumerate(row) if cell["is_mine"]
        ]

    def get_flagged_cells(self):
        return [
            (x, y) for x, row in enumerate(self.__field.field)
            for y, cell in enumerate(row) if cell["is_flagged"]
        ]

    @staticmethod
    def add_player(name, time):
        Players(name, time).add_player()

    @staticmethod
    def get_score():
        return Players.get_score()

    def start_timer(self):
        self.__timer.start()

    def stop_timer(self):
        return self.__timer.stop()

    def reset_timer(self):
        self.__timer.reset()

    def get_elapsed_time(self):
        return self.__timer.get_elapsed_time()

    def is_running(self):
        return self.__timer.is_running
