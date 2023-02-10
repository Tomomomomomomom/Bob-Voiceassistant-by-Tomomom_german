import vlc

# Create a VLC media player instance
player = vlc.MediaPlayer()

# Set the URL of the web radio station
radio_url = "http://your-radio-station-url.com/stream"

# Set the voice commands to listen for
play_command = "play radio"
stop_command = "stop radio"

while True:
    # Wait for a voice command
    command = input("Enter a voice command: ")

    if command == play_command:
        # Set the media to the radio URL and play it
        player.set_media(vlc.Media(radio_url))
        player.play()
    elif command == stop_command:
        # Stop the radio
        player.stop()
    else:
        # Unrecognized command
        print("Unrecognized command")

