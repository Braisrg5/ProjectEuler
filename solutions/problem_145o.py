'''https://projecteuler.net/problem=145'''
from time import time
from resources.useful_functions import flip_number


def find_reversibles(bound):
    '''Finds all numbers lower than bound such that the sum [n + reverse(n)]
    consists only of odd digits.'''
    start = time()
    processed = set()
    count = 0
    for n in range(1, bound):
        if n in processed or n % 10 == 0:
            continue
        flipped = flip_number(n)
        if all(int(digit) % 2 == 1 for digit in str(n + flipped)):
            count += 2
            processed.add(flipped)
        if time() - start > 5:
            print(f'{n} numbers done. {n/bound*100:.2f}% progress.')
            start = time()
    return count


def main():
    '''Main code of module.'''
    total = time()
    print(find_reversibles(10**8))  # 608720, 78.12s
    print(time() - total)


if __name__ == '__main__':
    main()
