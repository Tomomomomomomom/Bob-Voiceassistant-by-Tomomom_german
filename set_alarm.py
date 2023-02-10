import datetime

def set_alarm(time):
    # Parse the time string and get the current time
    alarm_time = datetime.datetime.strptime(time, "%H:%M")
    current_time = datetime.datetime.now()

    # Calculate the time difference between the current time and the alarm time
    time_difference = alarm_time - current_time

    # Set the alarm to go off in the time difference
    timer = threading.Timer(time_difference.total_seconds(), play_alarm)
    timer.start()

    # Return a response
    return f"Ich habe einen Wecker für {time} gestellt."

