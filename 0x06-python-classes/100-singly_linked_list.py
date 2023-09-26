#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The next node in the linked list (default is None).
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data stored in the node.

        Args:
            value (int): The new value to be stored in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next node in the linked list.

        Args:
            value (Node): The new next node to be set.

        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        """Initializes a new SinglyLinkedList object with an empty list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the linked list while maintaining the sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(values)
