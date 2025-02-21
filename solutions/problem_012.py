'''https://projecteuler.net/problem=12
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + + 7 = 28. The first
ten terms would be:
            1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...
Let us list the factors of the first seven triangle numbers:
            1: 1
            3: 1, 3
            6: 1, 2, 3, 6
            10: 1, 2, 5, 10
            15: 1, 3, 5, 15
            21: 1, 3, 7, 21
            28: 1, 2, 4, 7, 14, 28
We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five
hundred divisors?
'''
from functools import reduce
from collections import Counter
from resources.useful_functions import prime_factors


def count_divisors(n):
    '''Returns the number of divisors of the number n'''
    d = Counter(prime_factors(n))
    if not d:
        return 1
    return reduce(lambda x, y: x*y, [v + 1 for v in d.values()])


def div_triangle_number(D):
    '''Calculates the first triangle number to have over D divisors.'''
    n, divs = 1, 0
    while divs <= D:
        T = n*(n + 1)//2
        divs = count_divisors(T)
        n += 1
    return int(T)


if __name__ == '__main__':
    print(div_triangle_number(5))  # 28
    print(div_triangle_number(500))  # 76576500, 0.22s
