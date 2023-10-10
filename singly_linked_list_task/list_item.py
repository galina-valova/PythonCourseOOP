class ListItem:
    def __init__(self, data, next_item=None):
        self.__data = data
        self.__next_item = next_item

    @property
    def next_item(self):
        return self.__next_item

    @next_item.setter
    def next_item(self, next_item):
        self.__next_item = next_item

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
