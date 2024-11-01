# Print decorative header
print("\n****************************************************\n")
print("Welcome Branch")

# Import required libraries
import random  # for random selection of weather conditions
from time import sleep  # for simulating delay in response


# Function to randomly select a weather condition
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    # Randomly choose one condition from the list
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition


# Generate a random weather alert by calling the weather function
weatherAlert = weather()


# Function to simulate a Vehicle Response System (VRS) based on weather
def vehicleResponseSystem():
    # Check for "snowy" condition and set response
    if weatherAlert == "snowy":
        print("\n The National Weather Service has updated alarm by 35 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 60 mph")

    # Check for "blizzard" condition and set response
    elif weatherAlert == "blizzard":
        print("\n The National Weather Service has updated alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 55 mph.")

    # Check for "rainy" condition and set response
    elif weatherAlert == "rainy":
        print("\n The National Weather Service has updated alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 70 mph.")

    # Check for "windy" condition and set response
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 70 mph.")

    # Check for "icy" condition and set response
    elif weatherAlert == "icy":
        print("\n The National Weather Service has updated alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 85 mph.")

    # If no specific weather condition matches, use this default response
    else:
        print("\n The National Weather Service has called for", weatherAlert, "skies,"
                                                                              " drive carefully.")
        sleep(1)
        print("\n VRS System disengaged")


# Call the vehicle response function to execute based on weather condition
vehicleResponseSystem()
