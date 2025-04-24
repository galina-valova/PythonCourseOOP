from time import time


class Timer:
    def __init__(self):
        self.__is_running = False
        self.__start_time = 0
        self.__elapsed_time = 0

    @property
    def is_running(self):
        return self.__is_running

    def start(self):
        if not self.__is_running:
            self.__is_running = True
            self.__start_time = time() - self.__elapsed_time

    def stop(self):
        if self.__is_running:
            self.__is_running = False
            self.__elapsed_time = time() - self.__start_time
            return self.__elapsed_time

    def reset(self):
        self.__is_running = False
        self.__elapsed_time = 0

    def get_elapsed_time(self):
        return int(time() - self.__start_time) if self.__is_running else self.__elapsed_time
