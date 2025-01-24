#!/usr/bin/python3
"""
 a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters: ., ? and :"""
    if text is None:
        raise TypeError("text can't be None")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # for char in text:
    #     if char in [":", "?", "."]:
    #         text.replace(char + 1, "\n")
    result = ""
    i = 0
    while i < len(text):
            result += text[i]
            if text[i] in ".?:":
                result += "\n\n"  # Add exactly two new lines after each character
                while i + 1 < len(text) and text[i + 1] == " ":  # Skip extra spaces
                    i += 1
            i += 1

        # Remove any leading/trailing spaces from each line
    result = "\n".join(line.strip() for line in result.split("\n"))
    print(result)

