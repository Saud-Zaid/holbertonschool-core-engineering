#!/usr/bin/env python3
"""Module exploring multiple inheritance with FlyingFish."""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print fish swimming action."""
        print("The fish is swimming")

    def habitat(self):
        """Print fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print bird flying action."""
        print("The bird is flying")

    def habitat(self):
        """Print bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish inheriting from Fish and Bird."""

    def fly(self):
        """Print flying fish flying action."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print flying fish swimming action."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print flying fish habitat."""
        print("The flying fish lives both in water and the sky!")
