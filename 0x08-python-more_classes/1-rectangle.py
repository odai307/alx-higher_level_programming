#!/usr/bin/python3
"""A class that defies a rectangle"""


class Rectangle:
    """A class that represents a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrive the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
