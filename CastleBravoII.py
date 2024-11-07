<<<<<<< HEAD
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
    message = (bold+"InfoTechCenter System Booting" + "." * ellipsis + reset) # Used bold variable to give text weight
    ellipsis += 1  # Increment the ellipsis counter to add more dots
    # Write the message to the console, using '\r' to overwrite the line
    sys.stdout.write("\r" + message)
    time.sleep(0.5)  # Pause for 0.5 seconds to simulate loading time
    # Reset the ellipsis counter after it reaches 4 to cycle through 0-3 dots
    if ellipsis == 4:
        ellipsis = 0
    # Once the counter reaches 20, print the final boot-up message
    if x == 20:
        print(green + "\n\nOperating System Booted up - Retina Scanned - Access Granted" + reset) # Changed text to green using green variable
=======
# Print decorative header
print("\n****************************************************\n")
print("Weather Branch")

# Import required libraries
import random  # for random selection of weather conditions
from time import sleep  # for simulating delay in response

# Function to randomly select a weather condition
def weather():
    # List of possible weather conditions
    weather_forecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly choose one condition from the list
    return random.choice(weather_forecast)

# Generate a random weather alert by calling the weather function
weather_alert = weather()

# Function to simulate a Vehicle Response System (VRS) based on weather
def vehicle_response_system():
    # Dictionary to store weather conditions and corresponding responses
    weather_responses = {
        "snowy": (35, 60),
        "blizzard": (45, 55),
        "rainy": (15, 70),
        "windy": (15, 70),
        "icy": (50, 85)
    }

    # Check if the weather condition has a specific response
    if weather_alert in weather_responses:
        delay, speed_limit = weather_responses[weather_alert]
        print(f"\n The National Weather Service has updated alarm by {delay} minutes because"
              f" of the forecast of {weather_alert} weather conditions.")
        sleep(1)
        print(f"\n VRS System has been engaged, only allowing {speed_limit} mph.")
    else:
        # Default response for unlisted conditions
        print(f"\n The National Weather Service has called for {weather_alert} skies, drive carefully.")
        sleep(1)
        print("\n VRS System disengaged")

# Call the vehicle response function to execute based on weather condition
vehicle_response_system()
>>>>>>> Weather
