#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """serializes the dictionary into XML and save it to the given filename."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """"Deserializes the xml file given and return a deserialize dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result_dict = {}

        for child in root:
            text_value = child.text.strip() if child.text else ""
            if text_value.isdigit():
                result_dict[child.tag] = int(text_value)
            elif text_value.replace('.', '', 1).isdigit() and text_value.count('.') < 2:
                result_dict[child.tag] = float(text_value)
            elif text_value.lower() in ["true", "false"]:
                result_dict[child.tag] = text_value.lower() == "true"
            else:
                result_dict[child.tag] = text_value

        return result_dict
    except FileNotFoundError:
        return None
