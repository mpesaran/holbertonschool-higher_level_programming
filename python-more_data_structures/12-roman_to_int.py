#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "M": 1000
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    number = 0
    roman_list = [roman_dict[item] for item in roman_string]
    for i in range(len(roman_list) - 1):
        if roman_list[i] >= roman_list[i+1]:
            number += roman_list[i]
        else:
            number -= roman_list[i]
    number += roman_list[len(roman_list) - 1]
    return number
