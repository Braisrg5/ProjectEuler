'''https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any reminder.

What is the smallest positive number that is evenly divisible by all the
numbers from 1 to 20?
'''
from collections import Counter
from resources.useful_functions import prime_factors


def factors_to_number(factors):
    '''Translates a dictionary of prime factors and exponents to a number.'''
    n = 1
    for key, value in factors.items():
        n *= key**value
    return n


def lcm(numbers):
    '''Finds the least common multiple of a list of numbers, following the
    method of multiplying the prime factors to the highest exponent.'''
    factors_list = [Counter(prime_factors(n)) for n in numbers]
    new_factors = dict()
    # For the factors of each number in the list
    for factors in factors_list:
        # And for every factor and its exponent
        for key, value in factors.items():
            # If the factor is already in the new_factors dictionary, we check
            # if the exponent is higher in this case
            if key in new_factors.keys():
                if value > new_factors[key]:
                    new_factors[key] = value
            # If it isn't in the dictionary, we add it with its exponent
            else:
                new_factors[key] = value
    # Finally, we convert the dictionary of factors to a number and return it.
    return factors_to_number(new_factors)


def lcm_to_number(n):
    '''Finds the least common multiple of the number from n to n.'''
    return lcm(list(range(1, n+1)))


if __name__ == '__main__':
    print(lcm_to_number(10))  # 2520
    print(lcm_to_number(20))  # 232792560, 0.0s
