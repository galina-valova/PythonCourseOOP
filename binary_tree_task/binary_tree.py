from collections import deque
from binary_tree_task.node import Node


class BinaryTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def insert(self, data):
        inserted_node = Node(data)

        if self.__root is None:
            self.__root = inserted_node
        else:
            current_node = self.__root
            while True:
                if data < current_node.data:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = inserted_node
                        break
                else:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = inserted_node
                        break

        self.__size += 1

    def __find(self, data):
        if self.__root is None:
            return None, None

        parent_node = None
        current_node = self.__root

        while True:
            if data == current_node.data:
                return parent_node, current_node

            if data < current_node.data:
                if current_node.left is not None:
                    parent_node = current_node
                    current_node = current_node.left
                    continue
            else:
                if current_node.right is not None:
                    parent_node = current_node
                    current_node = current_node.right
                    continue

            return None, None

    @staticmethod
    def __find_minimum(next_node):
        leftmost_node = next_node.left
        parent_leftmost_node = next_node

        while leftmost_node.left is not None:
            leftmost_node = leftmost_node.left
            parent_leftmost_node = parent_leftmost_node.left

        return parent_leftmost_node, leftmost_node

    def __assign_value(self, parent_node, deleted_node, value):
        if parent_node is None:
            self.__root = value
        elif deleted_node.data < parent_node.data:
            parent_node.left = value
        else:
            parent_node.right = value

    def remove(self, data):
        parent_node, deleted_node = self.__find(data)

        if deleted_node is None:
            return False

        # deleting leaf
        if deleted_node.left is None and deleted_node.right is None:
            self.__assign_value(parent_node, deleted_node, None)

        # deleting node with one child
        elif deleted_node.left is None or deleted_node.right is None:
            child = deleted_node.left if deleted_node.left is not None else deleted_node.right
            self.__assign_value(parent_node, deleted_node, child)

        # deleting node with two children
        else:
            next_node = deleted_node.right

            if next_node.left is None:
                next_node.left = deleted_node.left
                self.__assign_value(parent_node, deleted_node, next_node)

            else:
                parent_leftmost_node, leftmost_node = self.__find_minimum(next_node)
                parent_leftmost_node.left = leftmost_node.right
                leftmost_node.right = deleted_node.right
                leftmost_node.left = deleted_node.left
                self.__assign_value(parent_node, deleted_node, leftmost_node)

        deleted_node.left = None
        deleted_node.right = None

        self.__size -= 1
        return True

    def traverse_in_width(self, function):
        if self.__root is None:
            return False

        nodes_queue = deque()
        nodes_queue.appendleft(self.__root)

        while nodes_queue:
            node = nodes_queue.pop()
            function(node.data)

            if node.left is not None:
                nodes_queue.appendleft(node.left)
            if node.right is not None:
                nodes_queue.appendleft(node.right)

    def traverse_in_depth(self, function):
        if self.__root is None:
            return False

        nodes_stack = deque()
        nodes_stack.append(self.__root)

        while nodes_stack:
            node = nodes_stack.pop()
            function(node.data)

            if node.right is not None:
                nodes_stack.append(node.right)
            if node.left is not None:
                nodes_stack.append(node.left)

    def traverse_in_depth_with_recursion(self, function):
        if self.__root is None:
            return False

        self.__visit_node(self.__root, function)

    def __visit_node(self, node, function):
        if node is None:
            return

        function(node.data)
        left_child, right_child = node.left, node.right
        self.__visit_node(left_child, function)
        self.__visit_node(right_child, function)

    def __contains__(self, data):
        return bool(self.__find(data)[1])

    def __iter__(self):
        result = []
        self.traverse_in_width(result.append)
        return result.__iter__()
