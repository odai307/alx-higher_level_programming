#!/usr/bin/python3
#2-square.py
"""Creates a Class"""

class Square:
    """Represents a square class"""
    def __init__(self, size=0):
        """Initializes a class square
        Args:
            Size: Represents the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            """
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """
        Calculate area of the square
        """
        return self.__size ** 2
