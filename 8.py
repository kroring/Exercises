#!/usr/bin/python
import random

# Variable declarations
numbers = []
random_number = 0
deck = {
    0: '2 of Spades',
    1: '3 of Spades',
    2: '4 of Spades',
    3: '5 of Spades',
    4: '6 of Spades',
    5: '7 of Spades',
    6: '8 of Spades',
    7: '9 of Spades',
    8: '10 of Spades',
    9: 'Jack of Spades',
    10: 'Quenn of Spades',
    11: 'King of Spades',
    12: 'Ace of Spades',
    13: '2 of Clubs',
    14: '3 of Clubs',
    15: '4 of Clubs',
    16: '5 of Clubs',
    17: '6 of Clubs',
    18: '7 of Clubs',
    19: '8 of Clubs',
    20: '9 of Clubs',
    21: '10 of Clubs',
    22: 'Jack of Clubs',
    23: 'Quenn of Clubs',
    24: 'King of Clubs',
    25: 'Ace of Clubs',
    26: '2 of Diamonds',
    27: '3 of Diamonds',
    28: '4 of Diamonds',
    29: '5 of Diamonds',
    30: '6 of Diamonds',
    31: '7 of Diamonds',
    32: '8 of Diamonds',
    33: '9 of Diamonds',
    34: '10 of Diamonds',
    35: 'Jack of Diamonds',
    36: 'Quenn of Diamonds',
    37: 'King of Diamonds',
    38: 'Ace of Diamonds',
    39: '2 of Hearts',
    40: '3 of Hearts',
    41: '4 of Hearts',
    42: '5 of Hearts',
    43: '6 of Hearts',
    44: '7 of Hearts',
    45: '8 of Hearts',
    46: '9 of Hearts',
    47: '10 of Hearts',
    48: 'Jack of Hearts',
    49: 'Quenn of Hearts',
    50: 'King of Hearts',
    51: 'Ace of Hearts',
    }

# Add 5 unique, random numbers to numbers list
while (len(numbers) < 5):
    
    random_number = random.randrange(0, 51)
    
    if random_number not in numbers:
        numbers.append(random_number)

# Print out card & suit that corresponds to each random number in
# numbers list by using a dictionary lookup
for number in numbers:
    print deck[number]

