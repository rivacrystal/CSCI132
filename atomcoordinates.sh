#!/bin/bash
# atomcoordinates.sh
# Created on: March 28, 2022
# Version 1.0
# This program writes atom coordinates in a more readable format

# Check if it's a single-line argument
if test $# -lt 1
then
	echo 'You did not entre a file name. Please enter file name.'
	exit
fi

# Check if it's a readable file
if test ! -r $1
then
	echo 'This is not a readable file, please resubmit file or change permissions with chmod.'
	exit
fi

# Print atom coordinates
grep ^ATOM $1 | awk '{print "Atom:",$2,"\nX coordinates:",$7,"\nY coordinates:",$8,"\nZ coordinates:"$9"\n"}'