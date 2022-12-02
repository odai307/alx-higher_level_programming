#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import sys
    import hidden_4

    for i in dir(hidden_4):
        if n[:2] != "__":
            print(n)
