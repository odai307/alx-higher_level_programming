#!/usr/bin/python3
# 4-square.py
"""Defines a square class"""


class Square:
    """Represents a class square"""
    def __init__(self, size=0):
        """
        Initializes the class
        """
        self.__size = size

        @property
        def size(self):
            """Retrieves size of square"""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size to value"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Returns the area of the square"""
            return self.__size ** 2

        def my_print(self):
            """prints # the number of times the value of size"""
            if self.__size = 0:
                print()
            for i in range(self.__size):
                print("#" * self.__size)
