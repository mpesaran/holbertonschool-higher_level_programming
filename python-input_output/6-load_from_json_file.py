#!/usr/bin/python3
"""This module is about creating an object from a json file"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, encoding='utf-8') as f:
        read_line = f.read()
        return json.loads(read_line)
