#!/usr/bin/python3
"""Unittest for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestInteger(unittest.TestCase):
    """Class which inherits the unittest.TestCase class"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, -3, 8, 6, 2]), 8)
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-3, -4, -2,-1]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([8, 6, 4, 2), 8)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
