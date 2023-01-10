#!/usr/bin/python3
"""Inherits from Basee Geometry"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
"""Imports base geometry module"""


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """Initializing"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
