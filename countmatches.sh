#!/bin/bash
# countmatches.sh
# Author: Riva A. Crystal
# Created on: March 7, 2022
# Version: 1.0
# This program checks frequency of certain DNA

# Check if it's a readable file
if test! -f $1
then
	echo 'This is not a file, please resubmit file.'
	exit
fi

# Check if there are DNA sequences inputted
if test $# -lt 2
then
	echo 'PLease write in DNA sequences to search for in this file.'
	exit
fi

# Seach for DNA sequences
for x in "${@:2}"
do
	dna=$(grep -o $x $1 | wc -l)
	echo $x $dna
done