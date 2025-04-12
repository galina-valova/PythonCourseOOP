from temperature_task.view import View
from temperature_task.temperature_converter import TemperatureConverter
from temperature_task.controller import Controller

view = View()
model = TemperatureConverter()
controller = Controller(model, view)
view.set_controller(controller)
view.start()
