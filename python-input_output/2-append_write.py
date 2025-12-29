#!/usr/bin/python3
"""need modul is documented"""


def append_write(filename="", text=""):
    """function is documented with this"""
    with open(filename, "a") as file:
        file.write(text)
    return len(text)
