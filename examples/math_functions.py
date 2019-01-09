#!/bin/python3
from functools import reduce


def average(*args):
	return sum(args, 0.0) / len(args)

def factorial(num):
	# TODO: fix this. 

    # if not ((num >= 0) & (num % 1 == 0)):
    #     raise Exception(
    #         f"Number( {num} ) can't be floating point or negative ")
    return 1 if num == 0 else num * factorial(num - 1)


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

# Calculates the greatest common divisor between two or more numbers/lists.

# The helperGcdfunction uses recursion. Base case is when y equals 0. 
# In this case, return x. 
# Otherwise, return the GCD of y and the remainder of the division x/y.

# Uses the reduce function from the inbuilt module functools. Also defines a method spread for javascript like spreading of lists.

def gcd(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
    # The helperGcdfunction uses recursion. 

    # Base case is when y equals 0. 
	# In this case, return x. 
	# Otherwise, return the GCD of y and the remainder of the division x/y.
        return x if not y else gcd(y, x % y)

    return reduce((lambda x, y: _gcd(x, y)), numbers)



avg = average(1,5,99)
print("Average ", avg)

factored = factorial(3)
print ("Factorial ", factored)

gcd_value = gcd(110, 56)
print("Greatest Common Denominator: ", gcd_value)