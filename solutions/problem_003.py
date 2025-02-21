'''https://projecteuler.net/problem=3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''
from resources.useful_functions import prime_factors


if __name__ == '__main__':
    print(prime_factors(13195))  # [5, 7, 13, 29]
    print(prime_factors(600851475143))  # [71, 839, 1471, 6857], 0.0s
