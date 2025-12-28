#!/usr/bin/python3
"""funksiyani yaradaq"""


def add_attribute(obj, name, value):
    """funksiyani yaratdiq """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
