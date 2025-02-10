#!/usr/bin/pyhton3
"""This module is about convert to JSON string"""
import json


def to_json_string(my_obj):
    """returns th eJSON representation of an object"""
    return json.dumps(my_obj)
