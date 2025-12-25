#!/usr/bin/python3
"""creating class"""


class MyList(list):
    """A class that inherits from the built-in list class."""

    def print_sorted(self):
        print(sorted(self))
