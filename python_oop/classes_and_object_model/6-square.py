#!/usr/bin/env python3
"""Classes
"""


class Square:
    """Square with size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size: int = size
        self.position: tuple = position

    def __str__(self):
        return self.shape()

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        pos_ints = [x for x in value if isinstance(x, int) and x >= 0]
        if len(pos_ints) == 2 and len(value) == 2:
            self._position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.size * self.size

    def shape(self):
        ret = ""
        if self.size != 0:
            ret += "\n" * self.position[1]
            for h in range(self.size):
                ret += " " * self.position[0]
                ret += "#" * self.size
                ret += "\n"
        else:
            ret = "\n"
        return ret

    def my_print(self):
        print(self.shape(), end='')
