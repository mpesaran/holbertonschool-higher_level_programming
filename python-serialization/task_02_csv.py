#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename, json_fielename= 'data.json'):
    """Converts a csv file to serialized json file"""
    try:
        with open(csv_filename, encoding='utf-8') as file:
            csv_read = csv.DictReader(file)
            data = list(csv_read)

        with open(json_fielename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
            return True
    except FileNotFoundError:
        return False

convert_csv_to_json('data.csv')