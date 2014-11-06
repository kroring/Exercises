#!/usr/bin/python
import random

# Variable declarations
numbers = []
random_number = 0

# Add 5 unique, random numbers to numbers list
while (len(numbers) < 5):
    
    random_number = random.randrange(0, 51)
    
    if random_number not in numbers:
        numbers.append(random_number)

# Print out each number in numbers list
for number in numbers:
    print number
