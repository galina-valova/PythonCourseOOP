import os
import json


class Players:
    def __init__(self, name, play_time):
        self.__name = name
        self.__play_time = play_time

    def add_player(self):
        file_name = "model/data/players_scores.json"
        data = {"name": self.__name, "time": round(self.__play_time, 2)}

        if os.path.exists("model/data/players_scores.json"):
            with open(file_name, "r") as file:
                is_found = False
                loaded_file = json.load(file)

                for item in loaded_file:
                    if item.get("name") == self.__name:
                        item.update(time=round(self.__play_time, 2))
                        is_found = True
                        break

                if not is_found:
                    loaded_file.append({"name": self.__name, "time": round(self.__play_time, 2)})

        else:
            loaded_file = [data]

        with open(file_name, "w") as file:
            json.dump(loaded_file, file)

    @staticmethod
    def get_score():
        if os.path.exists("model/data/players_scores.json"):
            with open("model/data/players_scores.json") as input_file:
                return sorted(json.load(input_file), key=lambda x: x["time"])

        return []
