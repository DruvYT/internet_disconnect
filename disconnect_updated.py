import schedule
import time
import subprocess
import pyautogui

# Function to check for user inactivity based on mouse position
def check_inactivity():
    # Initial mouse position
    initial_position = pyautogui.position()
    time.sleep(1)  # Wait for 15 seconds
    new_position = pyautogui.position()
    
    # Check if mouse position has changed
    if initial_position == new_position:
        log_message = "User inactive for 15 seconds"
        write_log(log_message)
        return True
    else:
        log_message = "User activity detected"
        write_log(log_message)
        return False

# Function to disable internet using AppleScript
def disable_internet():
    try:
        # AppleScript code to disable internet connection
        applescript_code = 'do shell script "sudo ifconfig en0 down" with administrator privileges'
        subprocess.run(['osascript', '-e', applescript_code], check=True)
        
        # Log the event
        log_message = "Internet connection disabled"
        write_log(log_message)
    except subprocess.CalledProcessError as e:
        log_message = f"Failed to disable internet: {e}"
        write_log(log_message)

# Function to write log messages to a file
def write_log(message):
    with open("internet_off_log_3.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# Log the start of the script
write_log("Script started")

# Schedule the task to run if inactivity is detected
schedule.every(15).seconds.do(disable_internet)

# Main loop
inactive = False
while True:
    write_log("Checking for user inactivity")
    inactive = check_inactivity()
    if inactive:
        schedule.run_pending()
    time.sleep(1)  # Log update interval set to 1 second
