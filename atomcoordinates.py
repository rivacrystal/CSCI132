#!/usr/bin/env python3
# atomcoordinates.py
# Author: Riva A. Crystal
# Created on: March 30, 2022
# Version 1.0
# Usage: This program sorts atoms by their coordinates

# Import modules
import sys # allows for command-line arguments
import os # check if file is readable
import re # searches

# Check if it's a single-line argument
if len(sys.argv) != 2:
	print('You did not input a file. Plase input a file.')
	quit()

# Check if it's a readable file
if os.access(sys.argv[1], os.R_OK) == False:
	print("This file isn't readable. Please submit a file that is readable.")
	quit()

# Open file
for line in open(sys.argv[1]):
# Search for ATOM
	if lines.startswith("ATOM"):
# Print
		print('Atom serial number:',line[7:11].strip(),'\nX coordinates:',line[32:38].strip(),'\nY coordinates:',line[40:47].strip(),'\nZ coordinates:',line[49:56].strip(),'\n')