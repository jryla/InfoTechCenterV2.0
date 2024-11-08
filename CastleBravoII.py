print("\n****************************************************\n")
print("Gasoline Branch\n")

import random
from time import sleep

def gasLevelGuage():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1, 25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGuage()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is close to empty, checking GPS for closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank of gas, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is",gasStations(),"which is",milesToGasStationQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank has a half tank of gas")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter tank full")
    else:
        print("Your gas tank is full")
    
gasLevelAlert()