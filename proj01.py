#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########################################################
#  Programming Project #01
#
#  define constants
#  prompt for floating-point value and assign to variable
#  do mathematical conversions
#  output results
###########################################################

# Define symbolic constants for conversions
ROD_METERS = 5.0292
FURLONG_RODS = 40
MILE_METERS = 1609.34
FOOT_METERS = 0.3048
MILE_PER_MINUTE = 3.1 / 60

# Get user input for # rods
rods_float = float(input("Input rods: "))

# Convert rods to other values
meters = rods_float * ROD_METERS
feet = meters / FOOT_METERS
miles = meters / MILE_METERS
furlongs = rods_float / FURLONG_RODS
minutes_walking = miles / MILE_PER_MINUTE

# Output conversions and results
print("You input", rods_float, "rods.\n")
print("Conversions\nMeters:", round(meters,3))
print("Feet:", round(feet,3))
print("Miles:", round(miles, 3))
print("Furlongs:", round(furlongs, 3))
print("Minutes to walk", rods_float, "rods:", round(minutes_walking,3))