# Import necessary libraries
import random  # for generating random selections
from time import sleep  # for pausing the program briefly (used for simulating delay)

# Print introductory message with decorative lines
print("\n****************************************************\n")
print("Gasoline Branch\n")

# List of possible gas levels and gas stations
GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
GAS_STATIONS = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]


# Function to generate a random gas level
def gasLevelGuage():
    return random.choice(GAS_LEVELS)


# Function to generate a random gas station
def gasStations():
    return random.choice(GAS_STATIONS)


# Function to generate a random distance to a gas station
def getDistance(level):
    if level == "Low":
        return round(random.uniform(1, 25), 1)  # 1 to 25 miles
    elif level == "Quarter Tank":
        return round(random.uniform(25.1, 50), 1)  # 25 to 50 miles
    return None  # No need for distance for higher gas levels


# Main function to determine the gas level and display an alert or suggestion
def gasLevelAlert():
    # Get the current gas level
    gasLevelIndicator = gasLevelGuage()

    # Print warning or message based on the gas level
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")

    elif gasLevelIndicator == "Low" or gasLevelIndicator == "Quarter Tank":
        # For "Low" or "Quarter Tank", check the nearest gas station and distance
        print(f"Your gas tank is at {gasLevelIndicator.lower()}, checking GPS for closest gas station...")
        sleep(2)  # Simulate the GPS lookup
        distance = getDistance(gasLevelIndicator)
        print(f"The closest gas station is {gasStations()} which is {distance} miles away")

    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has a half tank of gas")

    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full")

    else:
        print("Your gas tank is full")


# Call the gasLevelAlert function to execute the gas level check and alert
gasLevelAlert()
