"""
Created by: Emre Guzel
Created on: Sep 17 2024
This module is for a Micro:bit and can calculate the area and perimeter of rectangle .
Perimeter: 16 cm
Area: 15 cm^2
"""

from microbit import *
from time import sleep

display.clear()

sleep(1) 

l = 4

w = 4

perimeter = 2 * (l + w)

display.scroll(" P = 2(l+w) = " + str(perimeter) + 'cm')

A_L = 5

A_w = 3

area = (A_L * A_w )

display.scroll("A = L * w = " + str(area) + " cm^2")

