#!/usr/bin/env python3
"""Classes
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle

    Args:
        BaseGeometry: base geo
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)

    def area(self):
        return self._width * self._height
