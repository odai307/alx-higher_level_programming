#!/usr/bin/python3
"""A MyList class which Inherits from List class"""


class MyList(List):
    """This class Inherits from List class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
