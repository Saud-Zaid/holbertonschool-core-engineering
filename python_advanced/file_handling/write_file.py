#!/usr/bin/env python3
"""Module that defines a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
