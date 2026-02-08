def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        result = template

        for key in placeholders:
            value = attendee.get(key)
            value = "N/A" if value is None else str(value)
            result = result.replace(f"{{{key}}}", value)

        with open(f"output_{i}.txt", "w") as f:
            f.write(result)