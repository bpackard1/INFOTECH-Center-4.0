# Programmer: Brennan Packard
# Date: 1/20/2023
# Program: Infotech Center Upgrades

import random

def tirePressure():
    pressures = ["Left Front", "Right Front", "Left Back", "Right Back"]
    tireState = random.choice(pressures)
    return(tireState)

trireStatus = tirePressure()

def pressureSensor():
    if tireStatus == "Left Front":
        print("\n Your",tireStatus,"tire has a low pressure, please fill it soon.")
        elif tireStatus == "Right Front"
        print("\n Your",tireStatus,"tire has a low pressure, please fill it soon.")
        elif tireStatus == "Right Back"
        print("\n Your",tireStatus,"tire has a low pressure, please fill it soon.")
        elif tireStatus == "Left Back"
        print("\n Your",tireStatus,"tire has a low pressure, please fill it soon.")
        else:
            print("\All of your tires are at safe Pressures")
            
            pressureSensor()
