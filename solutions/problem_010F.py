'''https://projecteuler.net/problem=10'''
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
from resources.useful_functions import sieve_Eratosthenes


if __name__ == '__main__':
    print(sum(sieve_Eratosthenes(10)))  # 17
    print(sum(sieve_Eratosthenes(2000000)))  # 142913828922, 0.06s
