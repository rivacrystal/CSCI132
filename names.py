#!/usr/bin/env python3
# names.py
# Author: Riva A. Crystal
# Created on: April 22, 2022
# Version 1.0
# names.py examines US baby name statistics
# Input at least two baby name CSVs into the command line in chronological order.
# The program will prompt the user to type in the numbers to show the proper order, e.g. if the files are 1934.csv 2002.csv 1967.csv, the user must type in "1 3 2" for proper order.
# The popularity of the names will then be displayed over the years.
# At the end, the user can write in names to see how popular they are in the years originally inputted

# Import modules
import pandas as pd # csv tool
import sys # allow arguments

# Check if it has enough arguments
if len(sys.argv) < 3:
    print("You need to input at least two files to compare.")
    quit()

# Make sure there aren't corrupted files
def corruption(file):
    check = pd.read_csv(file, header = None)
    if len(check.columns) > 3 and list(check[0].str.isalpha() and len(check[0]) < 30):
        print(f"{file} is corrupted. Skipping it.\n\n")
    else:
        return file

# Upload files
csvs = []
for x in range(1,len(sys.argv)):
    if corruption(sys.argv[x]) != None:
        csvs.append(corruption(sys.argv[x]))

# Combine CSV into single table
files = []
for x in csvs:
   files.append(pd.read_csv(x, header = None).assign(filename = x)) # read csv
df = pd.concat(files, ignore_index = True) # lines up dataframes into one csv

# Print most popular names
print("Most popular names are:", end = " ")
most_pop = df.loc[df.groupby('filename')[2].nlargest(10).reset_index(level=0, drop=True).index]
print(*list(most_pop[0]))

# List files given
print()
print((len(sys.argv) - 1), "files given:")
for x in range(1, len(sys.argv)):
    print(f"    {x}. {sys.argv[x]}")

# User input for file order
print()
order = list(map(int, input("Please specify chronological order of the files\nbased on the order of files above, from oldest to newest.\nPlease make sure there is a space between each number\nand please skip any corrupted files: ").split()))

# Print data
print()
print("Reporting trend based on this order:", end = " ")
for x in order:
    print(sys.argv[x], end = " ")

print()

# Function to compare the years
def next_year(name, year1, year2):
    print(f"Trend for popular name {name}:", end = " ")
    data = df.loc[df[0] == name].groupby('filename').max().reset_index(level=0).sort_values(by=[2], ascending = False) # Find max name in database
    x = data.loc[data['filename'] == year1] # Look for year
    y = data.loc[data['filename'] == year2] # Look for compared year
    if int(x[2]) == int(y[2]):
        print("remains unchanges in the data of", year2)
    elif int(x[2]) > int(y[2]):
        print("less popular in the data of", year2)
    else:
        print("more popular in the data of", year2)

# Function for first year
def first_year(name, year):
    print(f"Trend for popular name {name}:", end = " ")
    if name != most_pop.iloc[0][0]:
        print("less popular in the data of", year)
    else:
        print("more popular in the data of", year)

# Function for last year
def last_year(name, year):
    print(f"Trend for popular name {name}:", end = " ")
    data = df.loc[df[0] == name].groupby('filename').max().reset_index(level=0).sort_values(by=[2], ascending = False)
    data = data['filename'].tolist()
    if year != data[0]:
        print("less popular in the data of", year)
    else:
        print("more popular in the data of", year)

# Loop to go through the years
other_years = []
for x in order:
    data = most_pop.loc[most_pop['filename'] == sys.argv[x]]
    names = list(data[0])
    if sys.argv[x] == sys.argv[order[0]]:
        for y in names:
            first_year(y, sys.argv[order[0]])
            for z in order[1:]:
                next_year(y, sys.argv[x], sys.argv[z])
    elif sys.argv[x] == sys.argv[order[-1]]:
        for y in names:
            last_year(y, sys.argv[x])
    else:
        other_years = order.copy() # make variable so that it goes through every year
        other_years.remove(x) # except the one we're doing
        for y in names:
            for z in other_years:
                next_year(y, sys.argv[x], sys.argv[z])

# While loop for user input
print()
query_time = True
while query_time:
    name = input("Query: ")
    list_of_names = name.split(" ") # turn string of names into list
    for x in order:
        if sys.argv[x] == sys.argv[order[0]]:
            for y in list_of_names:
                first_year(y, sys.argv[order[0]])
                for z in order[1:]:
                    next_year(y, sys.argv[x], sys.argv[z])
        elif sys.argv[x] == sys.argv[order[-1]]:
            for y in list_of_names:
                last_year(y, sys.argv[x])
        else:
            other_years = order.copy()
            other_years.remove(x)
            for y in list_of_names:
                for z in other_years:
                    next_year(y, sys.argv[x], sys.argv[z])
    print()
