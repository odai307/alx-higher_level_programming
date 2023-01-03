import unittest
"""Module to find the max integer in a list"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers if the list is empty, the funciton returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result
