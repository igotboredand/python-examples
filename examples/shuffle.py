#!/bin/python3

# What should my nickname be?

# This script creates a shuffle function, then creates an array to shuffle.
# The idea is we can randomly select a "winner" from the array we shuffle.


from copy import deepcopy
from random import randint


def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

# Create an array to shuffle. 
array_to_shuffle = ['Scotty Quick Hands', 'Scottt', 'Scoot','Scott','Scooter','Scoots Pa Toots', 'Scoota']

# Shuffle and store the result.
result = shuffle(array_to_shuffle)

print('Shuffled array results: ', result)
print('Winner: ' + result[0])


