#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """A rectangle class with atrributes and methods"""
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

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
    def height(self, value)
    if type(value) is not int:
        raise TypeError("length must be an integer")
    if value < 0:
        raise ValueError("length must be >= 0")
    self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.width + self.length) * 2
