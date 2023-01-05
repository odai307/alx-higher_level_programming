#!/usr/bin/python3
"""
A module that prints a test with 2 new lines after characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    A function that prints new lines after characters '.', '?' and ':'

    Args:
        text: the text to be indented
    raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    signs = ['.', '?', ':']

    for char in text:
        print(char, end='')
        if char in signs:
            print()
            print()
