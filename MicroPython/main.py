"""
Created by: Emre Guzel
Created on: Sep 17 2024
This module is a Micro:bit and it can calculate the area and perimeter
Perimeter 16 cm
Area 15 cm^2
"""

from microbit import *
from time import sleep

display.clear

sleep(1)

#display.scroll (2 (" l + w") + (4 * 4) + "cm")

l=4
w=4
display.scroll(f"2{l}+{w}+{l* w}cm")
