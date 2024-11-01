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
        print("\n The National Weather Service has updated alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")

vehicleResponseSystem()