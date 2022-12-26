#!/usr/bin/python3
# 4-square.py
"""Defines a square class"""


class Square:
    """Creaes a square class"""
    def __init__(self, size=0):
        """Initializes the square class"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
