#!/usr/bin/python3

class Node:
    """
    This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The integer data for the node.
            next_node (Node): The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data attribute.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data attribute.

        Args:
            value (int): The new data to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next_node attribute.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next_node attribute.

        Args:
            value (Node): The new next_node to set.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The integer value to insert.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]  # Remove the last newline character
