#!/usr/bin/python3
"""defining class and object"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) is not a_class
