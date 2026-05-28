
# Alarm Clock in Python

# This program sets an alarm at a specific time
# and plays a message when the time matches.

import datetime
import time


# Set alarm time
alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)


while True:

    # Get current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    print("Current Time:", current_time)

    # Check alarm time
    if current_time == alarm_time:

        print("Wake up! Alarm Ringing...")
        break

    # Wait for 1 second
    time.sleep(1)