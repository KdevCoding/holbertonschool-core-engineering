#!/usr/bin/env python3
"""Classes
"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size: int = size

    def area(self):
        return self._Square__size * self._Square__size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size: int = value
