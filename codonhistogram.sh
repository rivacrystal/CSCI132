#!/bin/bash
# codonhistogram.sh
# Author: Riva A. Crystal
# Created on: March 7, 2022
# Version: 1.0
# This program checsk frequency of certain DNA, Pt. 2

# Check if it's a single-line argument
if test $# -lt 1
then
	echo 'You did not enter a file name. Please enter file name.'
	exit
fi

# Check if file is readable
if test ! -r $1
then
	echo "This file isn't readable. Please change permissions with chmod."
	exit
fi

# Check if the DNA has only acgt
dna_search=$(grep | [^acgt] $1)
if [ "dna_search" ]
then
	echo 'This file does not contain a DNA sequnce. Please input a file with a DNA sequence.'
	exit
fi

# Divide by three, check frequency of the threes, then sort by decreasing frequency
fold -w3 $1 | sort | uniq -c | sort -nr