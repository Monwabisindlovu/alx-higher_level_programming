#!/usr/bin/python3
class Node:
    """A node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list."""

    def __init__(self):
        """Initialize a singly linked list with a head."""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list."""
        new_node = Node(value)
        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
