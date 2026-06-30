'''https://projecteuler.net/problem=145'''

from resources.useful_functions import flip_number
from time import time


def find_reversibles(bound):
    '''Finds all numbers n such that the sum [n + reverse(n)] consists only
    of odd digits, amd that are lower than bound.'''
    numbers = list(range(1, bound))
    count = 0
    for n in numbers:
        if n % 10 == 0:
            continue
        flipped = flip_number(n)
        if all(int(digit) % 2 == 1 for digit in str(n + flipped)):
            count += 2
            numbers.remove(flipped)

    return count


def main():
    '''Main code of module.'''
    start = time()
    print(find_reversibles(10**6))
    print(time() - start)


if __name__ == '__main__':
    main()
