from minesweeper_task.gui.main_window import MainWindow
from minesweeper_task.gui.welcome_window import WelcomeWindow
from minesweeper_task.controller import Controller
from minesweeper_task.model.game_model import GameModel

model = GameModel()
welcome_window = WelcomeWindow()
main_window = MainWindow()
controller = Controller(model, main_window)
welcome_window.set_controller(controller)
main_window.set_controller(controller)
welcome_window.start()
