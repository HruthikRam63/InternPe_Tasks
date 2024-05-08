import datetime  # Importing the datetime module to work with dates and times
import time  # Importing the time module to introduce delays
import os  # Importing the os module to interact with the operating system

def clear_screen():
    # Function to clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def digital_clock():
    while True:  # Infinite loop to continuously update the clock
        clear_screen()  # Clear the screen before printing the current time
        # Get the current time
        current_time=datetime.datetime.now()
        # Format the current time as HH:MM:SS
        formatted_time=current_time.strftime("%H:%M:%S")
        # Print the formatted time
        print("Current Time:",formatted_time)
        # Wait for one second before updating the time
        time.sleep(1)
        
# Run the digital clock
digital_clock()