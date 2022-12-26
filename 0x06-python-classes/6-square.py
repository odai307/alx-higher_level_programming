#!/usr/bin/python3
# 5-square.py
"""Defines a class square"""


class Square:
    """Creates a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @property.setter
    def size(self, value):
        """
        sets the value of size to value
        If size is not an integer, raise a TypeError
        If size is less than 0, raise a ValueErro
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @property.setter
    def position(self, value):
        """
        sets position to value
        position must be a tuple of 2 positive integers,
        otherwise raise a TypeError
        """
        if not isinstance(value, (int, int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character "#\" """
        if self.__size = 0:
            print()
        for i in range(len(self.__size)):
            for j in range(len(self.__size)):
                print("#", end='')
            print()
