#!/usr/bin/env python3
# report.py
# Author: Riva A. Crystal
# Created on: April 20, 2022
# Version 1.0
# report.py examines COVID data in NYS
# Input ONLY ONE CSV from the NYS government website about COVID-19 in the command line
# The program will then prompt the user to write a NYS county to see the statistics given by the CSV file. Proper spelling is required.
# After displaying the data and statistics, the program will prompt the user to type in another county.
# The user can quit at any time typing "quit."

# import modules
import sys # allows command-line arguments
import os # checks file existence
import pandas as pd # csv manipulator

# check if file was inputted
if len(sys.argv) != 2:
    print("You did not input a file. Please input a file.")
    quit()

# check if file exists
if os.path.isfile(sys.argv[1]) == False:
    print("File does not exist. Please input file that exists.")
    quit()

# check if file is readable
if os.access(sys.argv[1], os.R_OK) == False:
    print("File is not readable. Please change permissions with chmod.")
    quit()

# upload file
df = pd.read_csv(sys.argv[1]).sort_index(ascending = False)

# start while loop
repeat = True
while repeat:

# user input
    query = input('Enter the name of a county, or enter "quit" to quit: ').title()
# check if user response is quit:
    if query == 'quit' or query == 'Quit':
        print("Quitting now.")
        repeat == False
        quit()

# check if user wrote real county
    try:
        county = df.groupby('County').get_group(query)
    except KeyError:
        print("That is not a proper county name. \nPossible county names:", ", ".join(sorted(df['County'].unique())))
        print()
        continue

# set up columns for new table
    frequency = round(((county['New Positives']) / (county['Total Number of Tests Performed']) * 100), 2)
    cum = round(frequency.cumsum(), 2)

# create new table
    df2 = pd.DataFrame().assign(Test_Date = county['Test Date'], New_Positives = county['New Positives'], Tests_Performed = county['Total Number of Tests Performed'], Frequency = frequency, Cumulative_Frequency = cum)

# create variable for first positive 
    first_date = ""
    for index, row in df2.iterrows():
        if row['New_Positives'] > 0:
            first_date += row['Test_Date']
            break

# print results
    print()
    print(f"{query} County:")
    print(df2.to_string(index=False))

    print()
    print(f"Statistics for {query} County")
    print(f"First positives discovered: {first_date}")
    print('Highest number of tests performed:', df2["Tests_Performed"].max(), "on", df2["Test_Date"][df2["Tests_Performed"].idxmax()])
    print("Highest number of positives discovered:", df2["New_Positives"].max(), "on", df2["Test_Date"][df2["New_Positives"].idxmax()])
    print("Average positivity frequency:", round(df2["Frequency"].mean(),2))
    print("Average cumulative frequency:", round(df2["Cumulative_Frequency"].mean(),2), "\n\n")
