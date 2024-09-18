"""
Created by: Emre Guzel
Created on: Sep 17 2024
This module is a Micro:bit and it can calculate the area and perimeter
Perimeter 16 cm
Area 15 cm^2
"""

from microbit import *

from time import sleep
display.clear()


sleep(1)


l = 2
w = 4
perimeter = 2 * (l + w)

display.scroll("Perimeter: " + str(perimeter) + "cm")
