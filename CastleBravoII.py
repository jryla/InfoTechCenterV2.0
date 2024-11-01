print("\n****************************************************\n")

print("Welcome Branch")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForecast = ["snowy","blizzard","rainy","windy","icy","sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

print(weather())