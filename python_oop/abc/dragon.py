#!/usr/bin/env python3
"""Module demonstrating mixins with Dragon."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print creature swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print creature flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly."""

    def roar(self):
        """Print dragon roaring action."""
        print("The dragon roars!")
