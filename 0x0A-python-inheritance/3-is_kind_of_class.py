#!/usr/bin/python3
"""This module returns True if an object is an instance or if the object is an instance of a class inherited from the specified class otherwise 
return False"""


def is_kind_of_class(obj, a_class):
    """ This function returns True if an object is an instance or if the object is an instance of a class inherited from the specified class otherwise return False"""
    return (isinstance(obj, a_class))
