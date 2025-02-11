#!/usr/bin/python3
"""This module is about serialization in python"""
import json


def serialize_and_save_to_file(data, filename):
    """Opens and writes given data in the file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_str = json.dumps(data)
        f.write(json_str)


def load_and_deserialize(filename):
    """Opens and readds a file and deserialize it"""
    with open(filename, encoding= 'utf-8') as f:
        read_file = f.read()
        return json.loads(read_file)
