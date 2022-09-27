#!/usr/bin/python3
# dnaTranslate.py
# Author: Riva A. Crystal
# Created on: March 22, 2022
# Version 1.0
# dnaTranslate.py shows the codon sequence of DNA
# Input ONLY ONE dna file in the command line. Make sure it's either FASTA or just a string of DNA with no other text inside.
# Program will examine the DNA and produce the codon sequence from the file, along with a list of the codons themselves.

# Import module to allow for arugments
import sys #allow arguments
import re #allow searching
from collections import Counter #counts for dictionary

# Input file
file = open(sys.argv[1], "rt").read()

# Check if the FASTA has proper formatting
if sys.argv[1].endswith(".fasta"):
    if file[0] != ">":
        print("This FASTA file is not formatted properly. We will proceed, but the file may be corrupted.")

# Check if file contains only DNA sequence
def is_dna(file):
    no_dna = re.search("^[^acgtACGT]+$", file)
    if no_dna:
        print("This file contains information besides a DNA sequence. Please try again with a DNA sequence.")
        quit()
    else:
        return file

#Remove line if it's FASTA
def remove_first_line(file):
    final_file = ""
    with open(file) as f:
        next(f)
        for skip_line in f:
            final_file += skip_line
        return final_file

# Remove line breaks
def make_one_line(file):
    file = file.replace("\n", "")
    return file

# Check if it's divisible by 3
def divisible(file):
    if len(file) % 3 != 0:
        print("This is an incomplete DNA strand, but we will still proceed.\n")
    return(file)

# Turn into lowercase
def lower_case(file):
    lower = file.lower()
    return lower

# Check if it's divisible by threes and break into threes
if sys.argv[1].endswith(".fasta"):
    new_file = divisible(lower_case(is_dna(make_one_line(remove_first_line(sys.argv[1])))))
    initial = re.findall("...", new_file)[1:]
else:
    divisible(lower_case(is_dna(make_one_line(file))))
    initial = re.findall("...", file)[1:]

# End at stop codon
sequence = []
for x in initial:
    if x == "taa" or x == "tag" or x == "tga":
        sequence.append(x)
        break
    else:
        sequence.append(x)

print("Codon sequence:", *sequence)
# Dictionary of amino acids
amino_acids = {"ALA": ["gca", "gcc", "gcg", "gct"],
    "ARG": ["aga", "agg", "cga", "cgc", "cgg", "cgt",],
    "ASN": ["aac", "aat"],
    "ASP": ["gac", "gat"],
    "CYS": ["tgc", "tgt"],
    "GLN": ["caa", "cag"],
    "GLU": ["gaa", "gag"],
    "GLY": ["gga", "ggc", "ggg", "ggt"],
    "HIS": ["cac", "cat"],
    "ILE": ["ata", "atc", "att"],
    "LEU": ["cta", "ctc", "ctg", "ctt", "tta", "ttg"],
    "LYS": ["aaa", "aag"],
    "MET": ["atg"],
    "PHE": ["ttc", "ttt"],
    "PRO": ["cca", "ccc", "ccg", "cct"],
    "SER": ["agc", "agt", "tca", "tcc", "tcg", "tct"],
    "THR": ["aca", "acc", "acg", "agt"],
    "TRP": ["tgg"],
    "TYR": ["tac", "tat"],
    "VAL": ["gta", "gtc", "gtg", "gtt"]
    }

# Print out amino acid sequence
print("Amino acid sequence:", end = " ")
acid_count = [] #initialize for later
for x in sequence:
    for key, value in amino_acids.items():
        if x in value:
            acid_count.append(key)
            if len(acid_count) == 0:
                print("No codon sequence found in file.")
                quit()
            else:
                print(key, end = " ")
print("***")

# Write number of bases, codons, and animo acids
print("Number of bases:", len(''.join(map(str,sequence))))
print("Number of codons:", len(sequence))

print("Amino acid counts:")
for key, value in sorted(dict(Counter(acid_count)).items(), key=lambda k: (-k[1], k[0])):
    print(key, value)
