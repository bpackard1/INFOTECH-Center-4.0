# Programmer: Brennan Packard
# Date: 1/20/2023
# Program: Infotech Center Upgrades
import random
import time
import sys
from time import sleep


def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarters Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel
  
  #Variable Calling gasLevelGauge function to store its value
  gasLevelIndicator = gasLevelGauge()
  
  # List of gas stations Fucntion
  
  def listOfGasStations():
    gasStations = ["Shell", "Costco", "Buc-ee's", "Speedway", "7-11", "Circle-K", "Meijer", "Marathon" 
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby
                   
 # Determine Gas level & closest gas station
                   
def gasLevelAlert():
     milesToGasStationLow =  round(random.uniform(1,25),2)
     milesToGasStationQuarterTank = round(random.uniform(26, 50),2)
     
    if gasLevelindicator == "Low":
                   print("\n***Warning***")
                   sleep(1)
                   print("Your gas tnak is extremely low, checking Google Maps for the nearest Gas Stations.")
                   sleep(1)
                   print("The Nearest Gas STations is", listofGasStations(), "which is", miles ToGastStationLow"miles away.")
                   elif gasLevelIndicator == "Quarter Tank": 
                   print("\n***Warning***")
                   sleep(1)
                   print("Your gas tank is only a quarter full.")
                   sleep(1)
                   print("The closest gas station is" listofGasStations(), "which is", milesToGasStationQuarterTank, "miles away")
                   elif gasLevelIndicator == "Half Tank"
                   print("\n***Warning***")
                   sleep(1)
                   print("\nYour gas tank is half full, which is enough gas to safely arrive to your destintion")
                   elif gasLevelIndicator == "ThreeQuarterTank")
                   print("\nYour gas tank is three quarters full, which is more than enough to safely arrive to your destination")
                   else:
                   print("\nYour gas tank is full, Good Job, Vroom Vroom")
                   
                   
                   
                   #Create Weather Conditions ina  list and choose it randomly
                   
                   def weather():
                   weatherForecast = ["Snow", "Blizzard", "Rain", "Fog", "Windy", "Icy", "Sunshine"]
                   weatherCondition = random.choice(weatherForecast)
                   return weatherCondition
                   
                   #Variable to call weather() once in our VRS
                   weatherAler = weather()
                   
                   #VRS() to respond to the weather conditions
                   
                   def vehicleResponseSystem():
                   if weatherAlert == "snow':
                   print("NWS has changed your alarm by 15 minutes because of the weather forecast of", weatherAlert)
                   print("VRS has been engaged only allowing your vehicle to go 45 MPH")
                   elif weatherAlert == "Blizzard"
                   print("NWS has changed your alarm by 30 minutes because of the weather forecast of" weatherAlert)
                   print("VRS has been engaged only allowing your vehicle to go 35 MPH")
                   elif weatherAlert == "Fog"
                   print("NWS is calling for", weatherAlert, "conditions, please drive extra careful")
                   elif weatherAlert == "Windy"
                   print("NWS is calling for", weatherAlert, "conditions, please drive extra careful")
                   elif weatherAlert == "Icy"
                   print("NWS ha changed your alarm by 60 minutes because of", weatherAlert, "road conditions")
                   print("VRS has been engaged only allowing your vehicle to go 25 MPH")
                   else:
                   print("NWS is calling for", weatherAlert, "drive safely and have a Wonderful Day")
                   
                   
                   
                   #Call Function here
                   
                   if gasLevelIndicator == "Empty"
                   print("\n***WARNING YOU ARE ON EMPTY***)
                         sleep(1)
                         print("Calling Emergency Contact")
                         else:
                         print("Nation Weather Service is checking conditions...\n")
                         sleep(2)
                         vehicleResponseSystem()
                         print("\nChecking your vehicle's current gas levels...")
                         sleep(2)
                         gasLevelAlert()
                         
                         
                         
