'''https://projecteuler.net/problem=57'''
# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
#             sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...))))

# By expanding this for the first four iterations, we get:
#             1 + 1/2 = 3/2
#             1 + 1/(2 + 1/2) = 7/5
#             1 + 1/(2 + 1/(2 + 1/2)) = 17/12
#             1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29
# The next three expansions are 99/70, 239/269, and 577/408, but the eight
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.

# In the first one thousand expansions, how many fractions contain a numerator
# with more digits than the denominator?
from fractions import Fraction


def sequence(bound):
    '''Finds all elements of the sequence a described in (1*) to n = bound.'''
    # First element of the sequence
    a1 = 1 + Fraction(1, 2)
    an_1 = a1  # Set it as a(n-1)
    for _ in range(2, bound+1):
        an = 1 + Fraction(1, an_1 + 1)
        yield an
        # Reset for next iteration
        an_1 = an


def digits_num_den(frac):
    '''Returns the number of digs in the numerator and denominator of frac.'''
    return len(str(frac.numerator)), len(str(frac.denominator))


def problem_57(bound):
    '''In the infinite continued fraction that equals sqrt(2), returns how many
    of the first bound expansions contain a numerator with more digits than the
    denominator.'''
    count = 0
    for an in sequence(bound):
        numerator_d, denominator_d = digits_num_den(an)
        count += (numerator_d > denominator_d)
    return count


if __name__ == '__main__':
    print(problem_57(8))  # 1
    print(problem_57(1000))  # 153, 0.013s


# ----- #
# Notes #
# ----- #

# (1*)
# Let's call the sequence an. For the first two elements of the sequence:
#             a1 = 1 + 1/2 = 2 + 1/2 - 1
#             a2 = 1 + 1/(2 + 1/2) = 1 + 1/(a1 + 1)
# Let's set another parallel sequence, bn, where b1 = a1 + 1
# So, for the first three iterations, we get:
#             a1 = 1 + 1/2 = 2 + 1/2 - 1 -> b1 = 2 + 1/2
#             a2 = 1 + 1/(2 + 1/2) = 1 + 1/b1 = 2 + 1/b1 - 1 -> b2 = 2 + 1/b1
#             a3 = 1 + 1/(2 + 1/(2 + 1/2)) = 1 + 1/(2 + 1/b1) = 1 + 1/b2
# So, eventually, we can generalize to:
#             an = 1 + 1/b(n-1) where b(n-1) = a(n-1) + 1
#             an = 1 + 1/(a(n-1) + 1)
