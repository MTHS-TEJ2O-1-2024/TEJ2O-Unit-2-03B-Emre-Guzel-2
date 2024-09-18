"""
Created by: Emre Guzel
Created on: Sep 17 2024
This module is for a Micro:bit and can calculate the area and perimeter.
Perimeter: 16 cm
Area: 15 cm^2
"""

from microbit import *
from time import sleep

display.clear()

sleep(1) 

display.scroll(str(3 + 2))
