#!/usr/bin/python3
"""
Module that prints a square with the character #
"""


def print_square(size):
    """
    Function to print square with the character #

    Args:
        size: The length of the square character to be printed

    raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
