#!/usr/bin/env python3
"""Module that defines a Square class with size validation."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with size.

        Args:
            size: Size of the square (default 0).
        """
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
