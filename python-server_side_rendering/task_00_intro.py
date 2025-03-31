import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and
    a list of attendees.

    Parameters:
    - template (str): The template string with placeholders for attendee data
      (name, event_title, event_date, event_location).
    - attendees (list of dict): A list of dictionaries, where each dict
        contains attendee data.

    The function checks the following:
    - Validates that the template is a string and attendees is a list of dicts.
    - Checks if the template or attendees list is empty.
    - Replaces any missing attendee data (name, event_title,
    event_date, event_location) with "N/A" in the generated output files.
    - Generates sequentially named invitation files with the formatted content.

    Error Handling:
    - Logs an error if invalid input types are provided.
    - Logs an error if the template is empty or the attendees list is empty.
    - Replaces any missing data in the attendee dictionary with "N/A"
      in the output files.
    """
    if not isinstance(template, str):
        print(f"Invalid input: Template must be a string, \
              but got {type(template)}.")
        return

    if not isinstance(attendees, list) or \
            not all(isinstance(att, dict) for att in attendees):
        print(f"Invalid input: Attendees must be a list of dictionaries, \
            but got {type(attendees)}.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("ENo data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        try:
            name = attendee.get("name", "N/A")
            event_title = attendee.get("event_title", "N/A")
            event_date = attendee.get("event_date", "N/A")
            event_location = attendee.get("event_location", "N/A")

            invitation = template.replace("{name}", name) \
                                 .replace("{event_title}", event_title) \
                                 .replace("{event_date}", event_date) \
                                 .replace("{event_location}", event_location)
            filename = f"invitation_{i}.txt"

            if os.path.exists(filename):
                print(f"Skipping {filename}: File already exists.")
                continue

            with open(filename, "w") as file:
                file.write(invitation)

        except KeyError as e:
            print(f"Error: Missing key in attendee data - {e}")
