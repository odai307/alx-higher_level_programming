#!/usr/bin/python3
"""
This module is composed by a function that prints a message
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints "My name is <first_name> <last_name>"
    Args:
        first_name = first name
        last_name = last name

    Raises:
        TypeError if first_name or last_name is not a string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
