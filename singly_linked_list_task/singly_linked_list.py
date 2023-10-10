from singly_linked_list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    @property
    def size(self):
        return self.__count

    def get_first_item_value(self):
        if self.__head is None:
            raise ValueError("List is empty")

        return self.__head.data

    def push_front(self, data):
        self.__head = ListItem(data, self.__head)
        self.__count += 1

    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise ValueError(f"List is empty, no way insert value by index {index}")

        if index >= self.size or index < 0:
            raise IndexError(f"List index out of range. Index is {index}, index must be in [0, {self.size})")

        if index == 0:
            self.push_front(data)
        else:
            current_item = self.__head

            while current_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            current_item.next_item = ListItem(data, current_item.next_item)
            self.__count += 1

    def delete_item_by_value(self, value):
        if self.__head is None:
            return False

        if self.__head.data == value:
            self.__head = self.__head.next_item
            self.__count -= 1
            return True

        current_item = self.__head
        while current_item is not None:
            if current_item.next_item is not None and current_item.next_item.data == value:
                current_item.next_item = current_item.next_item.next_item
                self.__count -= 1
                return True

            current_item = current_item.next_item
        return False

    def pop_front(self):
        if self.__head is None:
            return None

        head_data = self.__head.data
        self.__head = self.__head.next_item
        self.__count -= 1
        return head_data

    def delete(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise ValueError(f"List is empty, no way delete item by index {index}")

        if index >= self.size or index < 0:
            raise IndexError(f"List index out of range. Index is {index}, index must be in [0, {self.size})")

        if index == 0:
            return self.pop_front()
        else:
            current_item = self.__head

            while current_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            deleted_item_data = current_item.next_item.data
            current_item.next_item = current_item.next_item.next_item
            self.__count -= 1
            return deleted_item_data

    def reverse(self):
        previous_item = None
        current_item = self.__head

        while current_item is not None:
            next_item = current_item.next_item
            current_item.next_item = previous_item
            previous_item = current_item
            current_item = next_item

        self.__head = previous_item

    def copy(self):
        if self.__head is None:
            return SinglyLinkedList()

        list_copy = SinglyLinkedList()

        current_item = self.__head
        copied_item = ListItem(current_item.data)
        list_copy.__head = copied_item
        previous_item = copied_item
        current_item = current_item.next_item

        while current_item is not None:
            copied_item = ListItem(current_item.data)
            previous_item.next_item = copied_item
            previous_item = copied_item
            current_item = current_item.next_item

        list_copy.__count = self.__count

        return list_copy

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise ValueError("List is empty")

        if index >= self.size or index < 0:
            raise IndexError(f"List index out of range. Index is {index}, index must be in [0, {self.size})")

        if index == 0:
            return self.__head.data
        else:
            current_item = self.__head

            while current_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            returned_item_data = current_item.next_item.data
            return returned_item_data

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise ValueError("List is empty")

        if index >= self.size or index < 0:
            raise IndexError(f"List index out of range. Index is {index}, index must be in [0, {self.size})")

        if index == 0:
            self.__head.data = value
        else:
            current_item = self.__head

            while current_item is not None and index > 1:
                current_item = current_item.next_item
                index -= 1

            current_item.next_item.data = value

    def __repr__(self):
        result = []
        current_item = self.__head

        while current_item is not None:
            result.append(repr(current_item.data))
            current_item = current_item.next_item

        return f"{{{', '.join(result)}}}"
