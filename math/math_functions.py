#!/bin/python3
from functools import reduce
from copy import deepcopy


def average(*args):
	return sum(args, 0.0) / len(args)

def factorial(num):
    # TODO: fix this exception. 
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

# Uses the reduce function from the inbuilt module functools. 
# Also defines a method spread for javascript like spreading of lists.

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

def lcm(*args):
# Returns the least common multiple of two or more numbers.
# Use the greatest common divisor (GCD) formula and the fact that lcm(x,y) = x * y / gcd(x,y) to determine the least common multiple. The GCD formula uses recursion.
# Uses reduce function from the inbuilt module functools. Also defines a method spread for javascript like spreading of lists.
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    def _lcm(x, y):
        return x * y / _gcd(x, y)

    return reduce((lambda x, y: _lcm(x, y)), numbers)


def max_n(lst, n=1, reverse=True):
    return sorted(lst, reverse=reverse)[:n]

def min_n(lst, n=1):
    numbers = deepcopy(lst)
    numbers.sort()
    return numbers[:n]



avg = average(1,5,99)
print("Average ", avg)

factored = factorial(3)
print ("Factorial ", factored)

gcd_value = gcd(110, 56)
print("Greatest Common Denominator: ", gcd_value)

lcm_value = lcm(12,7,3)
print("Least Common Multiple ", lcm_value)

max_n_data = [121, 309, 29, 12, 86, 402, 607]
max_n_value = max_n(max_n_data, 3)
print("max_n = 3 values", max_n_value)

min_n_data = [121, 309, 29, 12, 86, 402, 607]
min_n_value = min_n(min_n_data, 3)
print("min_n = 3 values", min_n_value)
