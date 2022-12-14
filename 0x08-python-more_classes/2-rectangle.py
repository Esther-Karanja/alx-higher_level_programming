#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """A rectangle class with attributes width and length, and
    methods area and perimeter
    """
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("length must be an integer")
        if value < 0:
            raise ValueError("length must be >= 0")
        self.__width = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return int(self.__width * 2) + int(self.__height * 2)
