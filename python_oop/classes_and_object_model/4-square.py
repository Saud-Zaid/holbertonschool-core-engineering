#!/usr/bin/env python3
"""Module that defines a Square class with getters and setters."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with size.

        Args:
            size: Size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
