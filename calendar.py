import os
from icloud_sdk import iCloudService

# Set your iCloud account credentials
username = "your-username"
password = "your-password"

# Connect to the iCloud API
service = iCloudService(username, password)

# Set the voice command to listen for
command = "check calendar"

while True:
    # Wait for a voice command
    voice_command = input("Enter a voice command: ")

    if voice_command == command:
        # Get the events for the current day
        calendar = service.calendar.get_calendar()
        events = calendar.events_today()

        # Print the events
        print("Today's events:")
        for event in events:
            print(event.title)
    else:
        # Unrecognized command
        print("Unrecognized command")

