# Programmer: Brennan Packard
# Date: 1/20/2023
# Program: Infotech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech center 4.0 OS is  loading
"""
# Import Libraries Here
from time import sleep

x=2
print("\n\nWelcome - InfoTechCenter 4.0")
sleep(2)
print("\nInfotechCenter 4.0 OS Loading")

#print("\nInfoTech Center 4.0 OS is Loading


import time  # I imported the time library for further use in code.
import sys  # I imported the system library for further use in code.


print('\n\033[7;34;48m Welcome to TheDeclerationOfIndependence')


x = 0
a = 0

time.sleep(2)
print('')


while x != 20:
    x += 1


    b = ("\033[12;33;48m TheDeclarationOfIndependence" + "." * a)

    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:

        print('\033[4;32;48m Done!')

