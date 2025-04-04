#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file."""
    root = ET.Element("data")  # Root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Construct the dictionary
        data = {}
        for child in root:
            data[child.tag] = child.text.strip() if child.text else ""

        return data
    except ET.ParseError:
        return None

# def main():
#     sample_dict = {
#         'name': 'John',
#         'age': '28',
#         'city': 'New York'
#     }

#     xml_file = "data.xml"
#     serialize_to_xml(sample_dict, xml_file)
#     print(f"Dictionary serialized to {xml_file}")

#     deserialized_data = deserialize_from_xml(xml_file)
#     print("\nDeserialized Data:")
#     print(deserialized_data)

# if __name__ == "__main__":
#     main()