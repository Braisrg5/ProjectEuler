'''https://projecteuler.net/problem=58'''
# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.

#             37 36 35 34 33 32 31
#             38 17 16 15 14 13 30
#             39 18  5  4  3 12 29
#             40 19  6  1  2 11 28
#             41 20  7  8  9 10 27
#             42 21 22 23 24 25 26
#             43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued, what is the
# side length of the square spiral for which the ratio of primes along both
# diagonals first falls below 10%?
from sympy import isprime


def elements_diags(target_ratio=float('-inf'), target_dim=-1):
    '''Finds the first side length for which the ratio of prime elements in the
    diagonals of a spiral matrix constructed by the methods in (1*) is below
    the target_ratio.'''
    k = 1  # Initialize first element
    # Number of prime and not prime elements in the diagonals (start with x=1)
    primes_in_diags, nums_in_diags = 0, 1

    # Initialize dimension and ratio
    dim, ratio = 1, float('inf')
    while ratio >= target_ratio and dim != target_dim:
        # Next loop
        dim += 2
        step = dim - 1
        for _ in range(3):  # Only check first three corners
            k += step
            primes_in_diags += isprime(k)
        k += step
        nums_in_diags += 4
        ratio = primes_in_diags/nums_in_diags
    return dim, ratio


if __name__ == '__main__':
    print(elements_diags(target_dim=7))  # (7, 0.615)
    print(elements_diags(target_ratio=0.1))  # (26241, 0.0999), 0.068s


# ----- #
# Notes #
# ----- #

# (1*) Inherited from Problem 28
# CASE n IS ODD
# If we enumerate the numbers that we need to sum in increasing order, we have:
# 1, 3, 5, 7, 9, 13, 17, 21, 25.
# By observing their properties, we can group them by the difference that there
# is between them:
#             Difference of 2: 1, 3, 5, 7, 9
#             Difference of 4: 9, 13, 17, 21, 25
# By creating a 7 x 7 spiral, we can confirm that the next numbers are:
#             Difference of 6: 25, 31, 37, 43, 49
# We need then to construct this list of numbers and then sum them:
#                         01,
#             03,  7,  5,  9, (Diff 2, 3x3)
#             13, 17, 21, 25, (Diff 4, 5x5)
#             31, 37, 43, 49, (Diff 6, 7x7)
#             etc
# And we stop when the number is n x n. Observe that when the square is n x n,
# the last four numbers have a difference of n-1, so we can use that to stop.
