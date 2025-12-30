#!/usr/bin/python3
"""Module that documented"""
import json


def load_from_json_file(filename):
    """documented function"""

    with open(filename, 'r') as file:
        return json.load(file)
