#!/usr/bin/python3
"""need modul is documented """


def write_file(filename="", text=""):
    """function is documented with this """
    with open(filename, "w") as file:
        file.write(text)
