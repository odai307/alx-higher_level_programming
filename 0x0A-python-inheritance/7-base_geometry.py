#!/usr/bin/python3
"""This module creates a class BaseGeometry"""


class BaseGeometry:
    """Class to create a BaseGeometry class"""
    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
