#!/usr/bin/python3
"""module documented"""


def class_to_json(obj):
    obj_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
    return obj_dict
