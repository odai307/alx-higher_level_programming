#!/usr/bin/python3
"""This module takes a function and returns True if the object
    is an instance of a class otherwise returns False"""


def is_same_class(obj, a_class):
    """
    This functions returns true if obj is an object of class a-class
    """
    return type(obj) == a_class
