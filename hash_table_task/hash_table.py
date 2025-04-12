from hash_table_task.node import Node
from collections.abc import Collection
from typing import Any


class HashTable(Collection):
    def __init__(self, capacity=10):
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be an integer number, not", capacity)

        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer number, not", capacity)

        self.__capacity = capacity
        self.__size = 0
        self.__items: list[Any] = [None] * capacity

    def __load_factor(self):
        return len(self) / self.__capacity

    def __len__(self):
        return self.__size

    def __get_hash(self, index):
        return abs(hash(index) % self.__capacity)

    def __insert_impl(self, key, value):
        index = self.__get_hash(key)

        if self.__items[index] is None:
            self.__items[index] = [Node(key, value)]
            self.__size += 1
        else:
            current_node = self.__items[index]
            if current_node[0].key == key:
                current_node[0].value = value
            else:
                current_node.append(Node(key, value))
                self.__size += 1

    def insert(self, key, value):
        if self.__load_factor() > 0.6:
            self.__rehash_table()

        self.__insert_impl(key, value)

    def pop(self, key):
        if key not in self:
            raise KeyError(f"Key {key} is not in hash table.")

        index = self.__get_hash(key)
        returned_value = None

        for sub_index, node in enumerate(self.__items[index]):
            if node.key == key:
                returned_value = self.__items[index].pop(sub_index).value
                break

        self.__size -= 1
        return returned_value

    def __rehash_table(self):
        rehashed_table = HashTable(capacity=self.__capacity * 2)

        for node in self:
            rehashed_table.__insert_impl(node.key, node.value)

        self.__items = rehashed_table.__items
        self.__capacity = rehashed_table.__capacity
        self.__size = rehashed_table.__size

    def __contains__(self, key):
        for node in self:
            if node.key == key:
                return True

        return False

    def __iter__(self):
        for i in self.__items:
            if i is not None:
                yield from i

    def __repr__(self):
        result = {}

        for i in self:
            result.update({i})

        return f"{result}"
