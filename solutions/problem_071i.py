'''https://projecteuler.net/problem=71'''
# Consider the fraction, n/d, where n and d are positive integers. If n < d and
# HCF(n,d) == 1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in ascending order
# of size, we get:
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
#   4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.

# By listing the set of reduced proper fractions for d <= 1000000 in ascending
# order of size, find the numerator of the fraction immediately to the left of
# 3/7.
from math import ceil, gcd


def left_frac_v2(og_n, og_d, max_d):
    '''Finds the reduced fraction immediately to the left of n/d for
    d <= max_d.'''
    closest = (0, 1)
    for d in range(2, max_d+1):
        n_inf = ceil(closest[0]*d/closest[1])
        n_sup = ceil(og_n*d/og_d)
        for n in range(n_inf, n_sup):
            if gcd(n, d) == 1:
                closest = (n, d)
    return closest


def left_frac_v3(a, b, max_d):
    '''Finds the reduced fraction immediately to the left of n/d for
    d <= max_d.'''
    best_n, best_d = 0, 1
    d, min_d = max_d, 1
    while d >= min_d:
        n = (a*d - 1)//b
        if best_n*d < n*best_d:
            best_n, best_d = n, d
            delta = a*d - b*n
            min_d = d//delta + 1
        d -= 1
    return best_n, best_d


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    print(left_frac_v3(74, 75, 10**27))  # 428570, 0.31s
    print(f'Calculation completed in {perf_counter()-start} seconds')
