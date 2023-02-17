# Programmer: Brennan Packard
# Date: 1/20/2023
# Program: Infotech Center Upgrades

"""

Our Welcome Screen will start our program letting
drivers know that the Infotech Center 4.0 OS is loading
"""



# Import Libraries Here
import time
import sys
import random
from time import sleep





timeToSleep = 2
x = 0
a = 0

print("\n\nWelcome - InfotechCenter 4.0\n")
time.sleep(timeToSleep)
#print("\nInfotech Center 4.0 OS is now loading")



while x != 20:
   x += 1
   b = ("\033[1;33;40mInfotech center is now loading" + "." * a)
   a = a + 1
   sys.stdout.write('\r'+b)
   time.sleep(0.5)
   if a == 4:
       a = 0
   if x ==20:
       print('\033[1;32;40;40m Retina Scan Complete - Access Granted!\n')




# Program: Infotech Center 4.0 - Gasoline




"""
We will create a Function that will tell us our Fuel gauge level
  - Create a list with Gas Levels
  - Randomize and choose from the list to determine our gas level

create a Function to determine our closest Gas Station
  - Create a list of gas stations
  - Randomly choose a gas station from the list
Create s Function to determine our gas level and closest gas station
  - Print Gas level
  - Print Closest Gas Station
"""











# Gas Level Function
def gasLevelGauge():
   gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
   currentGasLevel = random.choice(gasLevelList)
   return currentGasLevel


# Variable calling gasLevelGauge function to store its value
gasLevelIndicator = gasLevelGauge()

# List of gas stations Function


def listOfGasStations():
  gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon"]
  gasStationNearby = random.choice(gasStations)
  return gasStationNearby


# Determine Gas Level & closest gas station


def gasLevelAlert():
   milesToGasStationLow = round(random.uniform(1, 25), 2)
   milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
   if gasLevelIndicator == "Empty":
       print("\n***WARNING YOU ARE ON EMPTY***")
       sleep(1)
       print("Calling Emergency Contact")
   elif gasLevelIndicator == "Low":
       print("\n***Warning***")
       sleep(1)
       print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
       sleep(1)
       print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationLow, "miles away.")
   elif gasLevelIndicator == "Quarter Tank":
       print("\n***Warning***")
       sleep(1)
       print("Your gas tank is only a quarter full.")
       sleep(1)
       print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
   elif gasLevelIndicator == "Half Tank":
       print("\nYour gas tank is half full, which is enough gas to safely make it to your destination")
   elif gasLevelIndicator == "Three Quarter Tank":
       print("\nYour gas tank is three quarters full, which is more than enough to safely make it to your destination")
   else:
       print("\nYour gas tank is full, Good Job, Vroom Vroom")



#Programer:Brennan Packard
#Date: 2.8.2023
#Program: Weather system updates

#Create weather conditions in a list and choose it randomly

def weather():
   weatherForcast = ["Snow", "Blizzard", "Rain", "Fog", "Windy", "Icy", "Sunshine"]
   weatherCondition = random.choice(weatherForcast)
   return weatherCondition



# Variable to call weather() once in our VRS

weatherAlert = weather()





# VRS() to respond to the weather conditions
def vehicleResponceSystem():
   if weatherAlert == "Snow":
       print("NWS has changed your Alarm by 15 minutes because of the weather forcast of", weatherAlert)
       print("VRS has been engaged only allowing your vehicle to go 45 MPH")
   elif weatherAlert == "Blizzard":
       print("NWS has changed your Alarm by 30 minutes because of the weather forcast of", weatherAlert)
       print("VRS has been engaged only allowing your vehicle to go 35 MPH")
   elif weatherAlert == "Rain":
       print("NWS is calling for", weatherAlert, ", please drive extra careful")
   elif weatherAlert == "Fog":
       print("NWS is calling for", weatherAlert, ", please drive extra careful")
   elif weatherAlert == "Windy":
       print("NWS is calling for", weatherAlert, "conditions, please drive extra careful")
   elif weatherAlert == "Icy":
       print("NWS has changed your Alarm by 60 minutes because of", weatherAlert, "road conditions")
       print("VRS has been engaged only allowing your vehicle to go 25 MPH")
   else:
       print("NWS is calling for", weatherAlert,"drive safely and have a wonderful day!")
def tirePressure():
 pressures = ["left front", "right front", "left back", "right back", "none"]
 tireState = random.choice(pressures)
 return(tireState)


tireStatus = tirePressure()

def pressureSensor():
   if tireStatus == "left front":
       print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
   elif tireStatus == "right front":
       print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
   elif tireStatus == "left back":
       print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
   elif tireStatus == "right back":
       print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
   else:
       print("\nAll of your tires are at safe pressures.")
#Call Function Here
if gasLevelIndicator == "Empty":
   print("\n***WARNING YOU ARE ON EMPTY***")
   sleep(1)
   print("Calling Emergency Contact")
else:
   print("Nation Weather Service is checking conditions...\n")
   sleep(2)
   vehicleResponceSystem()
   print("\nChecking your vehicle's current gas levels...")
   sleep(2)
   gasLevelAlert()
   print("\nChecking Your vehicle's tires' pressure")
   sleep(2)

   pressureSensor()

