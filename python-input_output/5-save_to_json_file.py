#!/usr/bin/python3
"""Module that documented"""
import json


def save_to_json_file(my_obj, filename):
    """documented func"""

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
