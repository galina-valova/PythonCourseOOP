from minesweeper_task.model.cell_status import CellStatus


class Controller:
    def __init__(self, model, main_window):
        self.__nrow = None
        self.__ncol = None
        self.__nmines = None
        self.__player_name = None
        self.__model = model
        self.__main_window = main_window

    def start_game(self, nrow, ncol, nmines, player_name):
        self.__nrow = nrow
        self.__ncol = ncol
        self.__nmines = nmines
        self.__player_name = player_name
        self.__model.set_game_data(nrow, ncol, nmines)
        self.__main_window.start(nrow, ncol, nmines)

    def click_left(self, x, y):
        self.__model.start_timer()
        self.update_time()
        opened_cell_coordinates = self.__model.open_cell(x, y)

        if opened_cell_coordinates["status"][0] == CellStatus.MINE:
            self.__main_window.show_mines(opened_cell_coordinates)
            self.disable_field()
            self.__model.stop_timer()
        else:
            self.__main_window.show_opened_cells(opened_cell_coordinates)
            self.check_win()

    def click_right(self, x, y):
        self.__model.start_timer()
        self.update_time()
        flagged_cell_coordinates = self.__model.toggle_flag(x, y)
        self.__main_window.set_flag(flagged_cell_coordinates)
        self.check_win()

    def reinit_game(self):
        self.__model.reset_timer()
        self.__main_window.update_time(0)
        self.__model.set_game_data(self.__nrow, self.__ncol, self.__nmines)
        self.__main_window.create_game_field(self.__nrow, self.__ncol)

    def disable_field(self):
        unopened_cells = self.__model.get_unopened_cells()
        self.__main_window.disable_cells(unopened_cells)

    def check_win(self):
        mines_coordinates = self.__model.get_mined_cells()
        flags_coordinates = self.__model.get_flagged_cells()
        unopened_cells_coordinates = self.__model.get_unopened_cells()

        if mines_coordinates == flags_coordinates and len(unopened_cells_coordinates) == 0:
            self.__main_window.disable_cells(flags_coordinates)
            self.__main_window.set_win_logo()
            win_time = self.__model.stop_timer()
            self.__model.add_player(self.__player_name, win_time)

    def update_time(self):
        if self.__model.timer.is_running:
            current_time = self.__model.get_elapsed_time()
            self.__main_window.update_time(current_time)
            self.__main_window.state_frame.after(1000, self.update_time)

    def get_score(self):
        return self.__model.get_score()
