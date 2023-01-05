#!/usr/bin/python3
"""A class that defines a Rectangle class"""


class Rectangle:
    """A class that represents a Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrives the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints a diagram of the triangle with the '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """Returns a string represtntation of the class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
