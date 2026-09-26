#!/usr/bin/env python3
"""Module that defines Animal, Dog, and Cat classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
