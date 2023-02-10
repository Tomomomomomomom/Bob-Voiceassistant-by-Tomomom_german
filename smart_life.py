import smart_life_py

# Set your Smart Life account credentials
username = "your-username"
password = "your-password"

# Connect to the Smart Life platform
smart_life = smart_life_py.SmartLife(username, password)

# Set the device and command names
device_name = "your-device-name"
on_command = "turn on the light"
off_command = "turn off the light"

while True:
    # Wait for a voice command
    command = input("Enter a voice command: ")

    if command == on_command:
        # Turn on the light
        smart_life.turn_on(device_name)
    elif command == off_command:
        # Turn off the light
        smart_life.turn_off(device_name)
    else:
        # Unrecognized command
        print("Unrecognized command")

