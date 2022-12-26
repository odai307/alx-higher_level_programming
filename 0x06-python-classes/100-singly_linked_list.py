#!/usr/bin/python3

"""Defines a node of a singly linked list"""


class Node:
    """Creates a class Node"""
    def __init__(self, data, next_node=None):
        """Initializes the node"""
        self.__data = data
        self.__node = next_node

    @property
    def data(self):
        """Retrieves the data data of the linked list"""
        return self.__data

    @property.setter
    def data(self, value):
        """Set's the data of the linked list"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node of the linked list"""
        return self.__node

    @property.setter
    def next_node(self, value):
        """Set the next node of the linked list"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__node = value



class SinglyLinkedList:
    """Creates a class SingleLinkedList"""
    def __init__(self):
        """Initializes the linked list"""
        self.__head = None


