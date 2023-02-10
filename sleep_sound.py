import time
import random

# List of sleep sounds to play
sleep_sounds = ["thunderstorm", "ocean waves", "white noise"]

# Length of time to play the sleep sounds (in hours)
duration = 1

# Start playing the sleep sounds
print("Playing sleep sounds for {} hour(s)...".format(duration))
for i in range(duration * 60):
    # Choose a random sleep sound from the list
    sleep_sound = random.choice(sleep_sounds)
    print("Playing {}...".format(sleep_sound))
    
    # Play the sleep sound for one minute
    time.sleep(60)

print("Done playing sleep sounds.")

