#!/usr/bin/env python3
"""Module that defines a Square class with position and str representation."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size: Size of the square (default 0).
            position: Tuple of 2 positive integers (default (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or isinstance(value[0], bool) or
                not isinstance(value[1], int) or isinstance(value[1], bool) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square."""
        if self.__size == 0:
            return ""
        lines = ["\n" * self.__position[1]]
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
            if i != self.__size - 1:
                lines.append("\n")
        return "".join(lines)
