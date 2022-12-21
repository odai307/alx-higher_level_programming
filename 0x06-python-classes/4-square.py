#!/usr/bin/python3
# 3-square.py
"""Defines a class"""


class Square:
    """Represents a class square"""
    def __init__(self, size=0):
        """
        Initiallizing the square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError:
                if size is not an integer
            ValueError:
                if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.size

    @size.setter
    def size(self, value):
        """
        If value is not int, raise TypeError
        If value is less than 0, raise a ValueError"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return self.size ** 2