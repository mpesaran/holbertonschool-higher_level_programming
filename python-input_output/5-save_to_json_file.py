#!/usr/bin/python3
"""This module is about saving an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
