#!/usr/bin/python3

"""Module to creat a singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return __data

            Attributes:
                __data (int): the data in linked list
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set __data"""

        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Return __next_node

            Attributes:
                __next_node (Node): the next node of linked list
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set __next_node"""

        if not isinstance(value, Node) and not isinstance(value, type(None)):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
            in the list (increasing order)
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        head = self.__head
        new_node = Node(value, self.__head)
        found = 1
        while head:
            if head.data < value:
                if head.next_node and head.next_node.data < value:
                    head = head.next_node
                else:
                    break
            else:
                found = 0
                break
        if head and found:
            new_node.next_node = head.next_node
            head.next_node = new_node
        else:
            self.__head = new_node

    def __str__(self):
        head = self.__head
        while head:
            if head.next_node:
                print(head.data)
            else:
                print(head.data, end="")
            head = head.next_node
        return ("")
