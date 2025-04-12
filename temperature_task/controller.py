class Controller:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view

    def convert(self, temperature, from_scale, to_scale):
        output_temperature = self.__model.convert_temperature(temperature, from_scale, to_scale)
        self.__view.show(output_temperature)
