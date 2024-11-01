import sys  # Import the sys module for system-specific parameters and functions
import time  # Import the time module for time-related functions

green = "\033[92m"
bold = "\033[1m"
reset = "\033[0m"


# Print a welcome message to the user
print("\nWelcome to InfoTechCenter V2.0")

x = 0  # Initialize a counter variable
ellipsis = 0  # Initialize a variable to track the number of dots for the loading message

# Loop until the counter reaches 20
while x != 20:
    x += 1  # Increment the counter
    # Create a loading message that includes an increasing number of dots
    message = (bold+"InfoTechCenter System Booting" + "." * ellipsis + reset)
    ellipsis += 1  # Increment the ellipsis counter to add more dots
    # Write the message to the console, using '\r' to overwrite the line
    sys.stdout.write("\r" + message)
    time.sleep(0.5)  # Pause for 0.5 seconds to simulate loading time
    # Reset the ellipsis counter after it reaches 4 to cycle through 0-3 dots
    if ellipsis == 4:
        ellipsis = 0
    # Once the counter reaches 20, print the final boot-up message
    if x == 20:
        print(green + "\n\nOperating System Booted up - Retina Scanned - Access Granted" + reset)
