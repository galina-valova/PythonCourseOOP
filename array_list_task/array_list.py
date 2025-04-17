from collections.abc import MutableSequence


class ArrayList(MutableSequence):
    def __init__(self, capacity=10):
        self.__items = [None] * capacity
        self.__size = 0

    def __len__(self):
        return self.__size

    def increase_capacity(self):
        self.__items = self.__items + [None] * len(self.__items)

    def ensure_capacity(self, capacity):
        if not isinstance(capacity, int):
            raise TypeError("Capacity must be int")

        if capacity < 0:
            raise ValueError("Capacity must be positive int")

        if len(self.__items) < capacity:
            self.__items = self.__items + [None] * (capacity - len(self.__items))

    def trim_to_size(self):
        self.__items = self.__items[:self.__size]

    def index(self, element, start=None, end=None):
        if start is None:
            start = 0

        if end is None:
            end = self.__size

        if not isinstance(start, int):
            raise TypeError("Start index must be int")

        if not isinstance(end, int):
            raise TypeError("End index must be int")

        if start >= end:
            raise ValueError("Start index must be greater than end index")

        returned_index = None

        for i in range(start, end):
            if self.__items[i] == element:
                returned_index = i
                break

        if returned_index is None:
            raise ValueError(f"Element {element} is not in list")

        return returned_index

    def count(self, element):
        count = 0

        for i in range(self.__size):
            if self.__items[i] == element:
                count += 1

        return count

    def clear(self):
        del self.__items[:]
        self.__size = 0

    def append(self, element):
        if self.__size >= len(self.__items):
            self.increase_capacity()

        self.__items[self.__size] = element
        self.__size += 1

    def extend(self, data):
        try:
            iter(data)
        except TypeError:
            print(f"{type(data).__name__} object is not iterable")

        for element in data:
            self.append(element)

    def __contains__(self, item):
        return item in self.__items[:self.__size]

    def remove(self, item):
        is_not_found = True

        for i in range(self.__size):
            if self.__items[i] == item:
                self.__delitem__(i)
                is_not_found = False
                break

        if is_not_found:
            raise ValueError(f"{item} not in list")

    def reverse(self):
        i = 0
        j = self.__size - 1

        while i < j:
            tmp = self.__items[i]
            self.__items[i] = self.__items[j]
            self.__items[j] = tmp
            i += 1
            j -= 1

    def __reversed__(self):
        for i in range(self.__size - 1, -1, -1):
            yield self.__items[i]

    def insert(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index > self.__size:
            self.append(value)
        else:
            if self.__size >= len(self.__items):
                self.increase_capacity()

            position = index if index >= 0 else max(self.__size + index, 0)

            for i in range(self.__size, position, -1):
                self.__items[i] = self.__items[i - 1]

            self.__items[position] = value
            self.__size += 1

    def pop(self, index=-1):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index < -self.__size or index >= self.__size:
            raise IndexError(f"Array list index out of range. Index must be in {(-self.__size, self.__size)}")

        deleted_value = self.__items[:self.__size][index]
        self.__delitem__(index)
        return deleted_value

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index < -self.__size or index >= self.__size:
            raise IndexError(f"Array list index out of range. Index must be in {(-self.__size, self.__size)}")

        position = index if index >= 0 else self.__size + index

        if position < self.__size - 1:
            for i in range(position, self.__size - 1):
                self.__items[i] = self.__items[i + 1]

        self.__items[self.__size - 1] = None
        self.__size -= 1

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index < -self.__size or index >= self.__size:
            raise IndexError(f"Array list index out of range. Index must be in {(-self.__size, self.__size)}")

        if index < 0:
            return self.__items[self.__size + index]

        return self.__items[index]

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("Index must be int")

        if index < self.__size or index >= self.__size:
            raise IndexError(f"Array list index out of range. Index must be in {(-self.__size, self.__size)}")

        if index < 0:
            self.__items[self.__size + index] = value
        else:
            self.__items[index] = value

    def __iter__(self):
        for i in range(self.__size):
            yield self.__items[i]

    def __iadd__(self, other):
        if not isinstance(other, ArrayList):
            TypeError("The second value must be ArrayList type")

        for element in other:
            self.append(element)

        return self

    def __repr__(self):
        return f"{self.__items[:self.__size]}"
