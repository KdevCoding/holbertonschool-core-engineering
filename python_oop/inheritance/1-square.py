#!/usr/bin/env python3
"""Classes
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square

    Args:
        Rectangle: base geo
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self._width = size
        self._height = size

    def area(self):
        return self._width * self._height
