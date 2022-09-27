#!/usr/bin/env python3
# mathq.py
# Author: CUNY Hunter CS Department, edited by Riva A. Crystal
# March 10, 2022
# Usage: This program makes a basic arithmatic test.


# Import modules
import random
import re

# Initialize Scoring Variables
score = 0
total = 0

print("Welcome to the mathq program. Press 'q' to quit at any time.")
keep_asking_questions = True
while keep_asking_questions:

# Generate a random math question and its solution 
    first_num = random.randint(0,9)
    second_num = random.randint(0,9)
    denominator = random.randint(1,9)
    operator = random.randint(0,3)

# Create multiplication question and solution
    if operator == 1:
        solution = first_num * second_num
        question = "%d x %d = " % (first_num, second_num)

# Create division question and solution
    elif operator == 2:
        if second_num == 0:
            continue
        solution = denominator * second_num
        (solution, denominator) = (denominator, solution)
        question = "%d / %d = " % (denominator, second_num)

# Create addition question and solution
    elif operator == 3:
        solution = first_num + second_num
        question = "%d + %d = " % (first_num, second_num)

# Create subtraction question and solution
    else:
        if first_num >= second_num:
            solution = first_num - second_num
            question = "%d - %d = " % (first_num, second_num)
        else:
            solution = second_num - first_num
            question = "%d - %d = " % (second_num, first_num)

# Display the question and get valid response
    response_is_not_valid = True
    while response_is_not_valid:
        print(question, '?')
        response = input("> ")

# Check if response is valid
        match = re.search("^[0-9]+$|^q$$|^Q$", response)
        if match:
            response_is_not_valid = False
        else:
            print("That was an invalid response. Enter a number or 'q' to quit.")
    
# Check correctness of user's response
    if response == 'q' or response == 'Q':
        keep_asking_questions = False
    else:
        total += 1
        if int(response) == solution:
            print('Correct!')
            score += 1
        else:
            print("Incorrect! %s %d" % (question, solution))

if total == 0:
    print("Exiting math q.")
else:
    print(f"""You answered {score} out of {total} questions correctly.

Thank you for playing mathq.""")