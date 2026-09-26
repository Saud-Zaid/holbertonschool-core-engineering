#!/usr/bin/env python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square using Rectangle."""

    def __init__(self, size):
        """Initialize the square with size.

        Args:
            size: Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
