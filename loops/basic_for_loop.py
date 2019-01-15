#!/usr/bin/python3
#
# Python program to demonstrate for loops.
#

# The for loop goes through a list, like foreach in
# some other languages.  A useful construct.

for x in ['Steve', 'Alice', 'Joe', 'Sue' ]:
    print(x, 'is awesome.')

# Powers of 2 (for no obvious reason)
power = 1

for y in range(0,25):
    print("2 to the", y, "is", power)
    power = 2 * power
    
# Scanning a list.
fred = ['And', 'now', 'for', 'something', 'completely', 'different.'];
for i in range(0,len(fred)):
    print(i, fred[i])