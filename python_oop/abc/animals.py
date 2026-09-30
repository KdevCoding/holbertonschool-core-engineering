#!/usr/bin/env python3
"""classes
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal

    Args:
        ABC (_type_): abstract class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog

    Args:
        Animal: Animal
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat

    Args:
        Animal: Animal
    """
    def sound(self):
        return "Meow"
