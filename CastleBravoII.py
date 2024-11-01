print("\n****************************************************\n")

print("Welcome Branch")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowy","blizzard","rainy","windy","icy","sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\n The National Weather Service has updated alarm by 35 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 60 mph")
    elif weatherAlert == "blizzard":
        print("\n The National Weather Service has updated alarm by 45 minutes because"
              " of the forecast of", weatherAlert ,"weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 55 mph.")
    elif weatherAlert == "rainy":
        print("\n The National Weather Service has updated alarm by 15 minutes because"
              " of the forecast of", weatherAlert ,"weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 70 mph.")
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 70 mph.")
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated alarm by 5 minutes because"
              " of the forecast of", weatherAlert ,"weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 85 mph.")
    elif weatherAlert == "windy":
        print("\n The National Weather Service has updated alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 85 mph.")
    elif weatherAlert == "icy":
        print("\n The National Weather Service has updated alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\n VRS System has been engaged, only allowing 85 mph.")
    else:
        print("\n The National Weather Service has called for", weatherAlert, "skies,"
        " drive carefully.")
        sleep(1)
        print("\n VRS System disengaged")

vehicleResponseSystem()

