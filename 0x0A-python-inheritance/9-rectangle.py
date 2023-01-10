#!/usr/bin/python3
"""Inherits from Basee Geometry"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
"""Imports base geometry module"""


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """Initializing"""
        super().self.integer_validator("width", width)
        self.__width = width
        super().self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the peint() and str() representation of a Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
