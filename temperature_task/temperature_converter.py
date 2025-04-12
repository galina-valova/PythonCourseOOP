from temperature_task.scale import Scale


class TemperatureConverter:
    @staticmethod
    def __convert():
        convertion_functions = {
            (Scale.CELSIUS, Scale.FAHRENHEIT): lambda celsius: celsius * 1.8 + 32,
            (Scale.CELSIUS, Scale.KELVIN): lambda celsius: celsius + 273.15,
            (Scale.FAHRENHEIT, Scale.CELSIUS): lambda fahrenheit: (fahrenheit - 32) / 1.8,
            (Scale.FAHRENHEIT, Scale.KELVIN): lambda fahrenheit: (fahrenheit - 32) / 1.8 + 273.15,
            (Scale.KELVIN, Scale.CELSIUS): lambda kelvin: kelvin - 273.15,
            (Scale.KELVIN, Scale.FAHRENHEIT): lambda kelvin: (kelvin - 273.15) * 1.8 + 32
        }
        return convertion_functions

    def convert_temperature(self, temperature, from_scale, to_scale):
        if from_scale == to_scale:
            return temperature

        selected_function = self.__convert()[(from_scale, to_scale)]
        return round(selected_function(temperature), 3)
