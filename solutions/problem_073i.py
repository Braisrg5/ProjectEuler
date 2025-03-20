# Consider the fraction, n/d, where n and d are positive integers. If n < d and
# HCF(n,d) == 1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in ascending order
# of size, we get:
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
#   4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
# proper fractions for d <= 12000.
from math import gcd, ceil, floor


def fractions_between(a1, b1, a2, b2, max_d):
    '''Calculates the number of fractions between a1/b1 and a2/b2 for
    d <= max_d, explained in (1*).'''
    count = 0
    for d in range(2, max_d+1):
        min_n = floor(d*a1/b1) + 1
        max_n = ceil(d*a2/b2)
        for n in range(min_n, max_n):
            if gcd(n, d) == 1:
                count += 1
    return count


def fractions_between_v2(a1, b1, a20, b20, max_d):
    '''Calculates the number of fractions between a1/b1 and a2/b2 for
    d <= max_d.
    https://projecteuler.net/overview=0073'''
    val = (max_d - b20)//b1
    a2 = a20 + val*a1
    b2 = b20 + val*b1
    count = 0
    while not (a2 == a20 and b2 == b20):
        count += 1
        k = (max_d + b1)//b2
        e = k*a2 - a1
        f = k*b2 - b1
        a1, b1 = a2, b2
        a2, b2 = e, f
    return count


def main():
    '''Main code of module.'''
    print(fractions_between(1, 3, 1, 2, 12000))  # 7295372, 2.09s
    print(fractions_between_v2(1, 3, 1, 2, 12000))  # 7295372, 1.21s


if __name__ == '__main__':
    main()


# ----- #
# Notes #
# ----- #

# (1*)
# For an arbitrary d, the fraction n/d lies between 1/3 and 1/2 if:
#           1/3 < n/d < 1/2 <-> d/3 < n < d/2
# So, for each d, we need to count the values of n that fit in that interval
# and that are coprime with d.

# COULD BE IMPLEMENTED WITH A MODIFIED PHI
