# Print introductory message with decorative lines
print("\n****************************************************\n")
print("Gasoline Branch\n")

# Import necessary libraries
import random  # for generating random selections
from time import sleep  # for pausing the program briefly (used for simulating delay)


# Function to generate a random gas level from predefined options
def gasLevelGuage():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select and return one of the gas levels
    return random.choice(gasLevelList)


# Function to generate a random gas station from a predefined list
def gasStations():
    # List of possible gas station names
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly select and return one of the gas stations
    return random.choice(gasStationsList)


# Main function to determine the gas level and display an alert or suggestion
def gasLevelAlert():
    # Generate random distances to gas stations based on different gas levels
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Random distance for low gas (1 to 25 miles)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50),
                                         1)  # Random distance for quarter tank (25 to 50 miles)

    # Get the current gas level by calling the gasLevelGuage function
    gasLevelIndicator = gasLevelGuage()

    # Conditional checks for each gas level and corresponding messages
    if gasLevelIndicator == "Empty":
        # If the gas level is "Empty", display a warning and simulate calling Triple AAA
        print("***WARNING - YOU ARE EMPTY***\n")
        sleep(2)  # Pause for 2 seconds to simulate a delay
        print("Calling Triple AAA")  # Simulate calling for roadside assistance

    elif gasLevelIndicator == "Low":
        # If the gas level is "Low", suggest a nearby gas station
        print("Your gas tank is close to empty, checking GPS for closest gas station")
        sleep(2)  # Pause to simulate the GPS lookup
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away")

    elif gasLevelIndicator == "Quarter Tank":
        # If the gas level is "Quarter Tank", suggest a nearby gas station
        print("Your gas tank is on a quarter tank of gas, checking GPS for the closest gas station")
        sleep(2)  # Pause to simulate the GPS lookup
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away")

    elif gasLevelIndicator == "Half Tank":
        # If the gas level is "Half Tank", inform the user that they have enough gas
        print("Your gas tank has a half tank of gas")

    elif gasLevelIndicator == "Three Quarter Tank":
        # If the gas level is "Three Quarter Tank", inform the user that they are good for now
        print("Your gas tank is three quarter tank full")

    else:
        # If the gas level is "Full", inform the user that they have a full tank
        print("Your gas tank is full")


# Call the gasLevelAlert function to execute the gas level check and alert
gasLevelAlert()
