'''We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from itertools import permutations
from resources.useful_functions import is_prime


def generate_pandigitals(n):
    '''Generates all n-digit pandigital numbers from biggest to smallest.
    '''
    pandigitals = list(permutations([str(i) for i in range(1, n+1)]))
    return sorted([int(''.join(p)) for p in pandigitals])[::-1]


def largest_pandigital_prime():
    '''Returns the largest n-digit pandigital prime that exists.
    '''
    for n in range(9, 0, -1):
        pandigital = generate_pandigitals(n)
        for num in pandigital:
            if is_prime(num):
                return num
        print("No primes found for n = ", n)
    # If no prime is found for any n, return -1.
    return -1


if __name__ == "__main__":
    print(largest_pandigital_prime())  # 7652413, 0.23s
