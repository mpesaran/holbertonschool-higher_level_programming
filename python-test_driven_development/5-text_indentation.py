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

    replacements = [('.', '.\n\n'), ('?', '?\n\n'), (':', ':\n\n')]

    for char, replacement in replacements:
        if char in text:
            text = text.replace(char, replacement)

    # Strip leading and trailing spaces from each line
    lines = text.split('\n')
    formatted_text = '\n'.join(line.strip() for line in lines)
    print(formatted_text)

