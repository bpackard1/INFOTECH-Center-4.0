# Programmer: Brennan Packard
# Date: 1/20/2023
# Program: Infotech Center Upgrades

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
                   elif gasLevelIndicator
