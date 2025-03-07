'''https://projecteuler.net/problem=39'''
# If p is the perimeter of a right angle triangle with integral length sides,
# {a, b, c}, there are exactly three solutions for p = 120.

# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}.

# For which value of p <= 1000, is the number of solutions maximized?
from resources.useful_functions import count_pyth_triples


def max_pyth_triples(num_pt):
    '''Finds the value p <= bound such that the number of pythagorean triples
    that sum p is maximized.'''
    return max(num_pt, key=num_pt.get)


if __name__ == '__main__':
    triples_under_1000 = count_pyth_triples(1000)
    print(triples_under_1000[120])  # 3
    print(max_pyth_triples(triples_under_1000))  # 840, 0.0004s


# ----- #
# Notes #
# ----- #

# (1*)
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# If m > n are positive integers, then:
#             a = m^2 - n^2
#             b = 2mn
#             c = m^2 + n^2
# forms a Pythagorean triple.

# There is a bijection between primitive Pythagorean triples and positive
# integers m and n such that m > n, m and n are coprime, and only one is even.

# Since a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m(m + n), we need to compute
# for 2m(m+n) <= bound <=> m(m+n) <= bound/2.

# If we take n = 0, then m^2 <= bound/2, so m <= sqrt(bound/2).
