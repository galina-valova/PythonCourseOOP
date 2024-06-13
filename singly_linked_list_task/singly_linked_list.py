from singly_linked_list_task.list_item import ListItem


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def __len__(self):
        return self.__count

    def __is_in_range(self, index):
        if index < 0 or index >= len(self):
            raise IndexError(f"List index out of range. Index is {index}, index must be in (0, {len(self)})")

    def __get_item_by_index(self, index):
        current_item = self.__head

        for i in range(1, index):
            current_item = current_item.next_item

        return current_item

    def get_first(self):
        if self.__head is None:
            raise ValueError("List is empty")

        return self.__head.data

    def insert_first(self, data):
        self.__head = ListItem(data, self.__head)
        self.__count += 1

    def insert(self, index, data):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if index < 0:
            raise ValueError("Index must be positive number, not", index)

        if self.__head is None or index == 0:
            self.insert_first(data)

        elif index >= len(self):
            current_item = self.__get_item_by_index(len(self))
            current_item.next_item = ListItem(data)
            self.__count += 1

        else:
            current_item = self.__get_item_by_index(index)
            current_item.next_item = ListItem(data, current_item.next_item)
            self.__count += 1

    def delete_by_data(self, value):
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

    def delete_first(self):
        if self.__head is None:
            raise ValueError("List is empty. No data to delete")

        deleted_data = self.__head.data
        self.__head = self.__head.next_item
        self.__count -= 1
        return deleted_data

    def delete(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise IndexError(f"List is empty, no way delete item by index {index}")

        self.__is_in_range(index)

        if index == 0:
            return self.delete_first()

        current_item = self.__get_item_by_index(index)

        deleted_data = current_item.next_item.data
        current_item.next_item = current_item.next_item.next_item
        self.__count -= 1
        return deleted_data

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
            raise IndexError("List is empty")

        self.__is_in_range(index)

        if index == 0:
            return self.__head.data

        current_item = self.__get_item_by_index(index)

        returned_data = current_item.next_item.data

        return returned_data

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError(f"Index must be int, not {type(index).__name__}")

        if self.__head is None:
            raise IndexError("List is empty")

        self.__is_in_range(index)

        if index == 0:
            self.__head.data = value
        else:
            current_item = self.__get_item_by_index(index)

            current_item.next_item.data = value

    def __repr__(self):
        items_list = []
        current_item = self.__head

        while current_item is not None:
            items_list.append(repr(current_item.data))
            current_item = current_item.next_item

        return f"{{{', '.join(items_list)}}}"
