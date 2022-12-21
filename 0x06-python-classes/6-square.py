#!/usr/bin/python3
# 5-square.py
"""Defines a class square"""


class Square:
    """Represent the class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class"""
        self.size = size
        self.position = position

    @property
