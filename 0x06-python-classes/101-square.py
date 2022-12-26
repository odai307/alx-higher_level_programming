#!/usr/bin/python3
# 6-square.py
"""Defines a class Square"""


class Square:
    """Creates a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the sauare class"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of the class"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the class square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the class square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the class square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = position

    def my_print(self):
        """Prints the size of the square with "#\" """
        if self.__size = 0:
            print()
        for i in range(len(self.__size)):
            for j in range(len(self.__size)):
                print("#", end='')
            print()
