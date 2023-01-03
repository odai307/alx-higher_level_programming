#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """Function to add two integers and or float numbers
    rasie TypeError if a is not integer or float or b is not integer of float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
