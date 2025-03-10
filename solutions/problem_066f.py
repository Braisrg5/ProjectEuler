'''https://projecteuler.net/problem=66'''
# Consider quadratic Diophantine equations of the form:
#             x^2 - D*y^2 = 1

# For example, when D = 13, the minimal solution in x is 649^2 - 13*180^2 = 1.
# It can be assumed that there are no solutions in positive integers when
# D is square.

# By finding the minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:
#             3^2 - 2*2^2 = 1
#             2^2 - 3*1^2 = 1
#             9^2 - 5*4^2 = 1
#             5^2 - 6*2^2 = 1
#             8^2 - 7*3^2 = 1

# Hence, by considering minimal solutions in x for D <= 7, the largest x is
# obtained when D = 5.

# Find the value of D <= 1000 in minimal solutions of x for which the largest
# value of x is obtained.
from math import sqrt
from resources.useful_functions import period_for_root, recurring_convergents


def minimal_value(d):
    '''Finds the minimal solution in x for the Diophantine equation
    x^2 - d*y^2 = 1.
    https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
    The solution in Wikipedia is actually wrong, what I've found is in (2*).'''
    # d can't be a square
    if sqrt(d).is_integer():
        return True

    # We first find the sequence of the continued fraction for sqrt(d)
    sequence_rep = period_for_root(d)
    # Length of the periodic part (we can call this r)
    period_len = len(sequence_rep) - 1
    # The maximum term that has the minimal solution is 2r-1
    max_terms = sequence_rep[:1] + sequence_rep[1:]*2
    # Special case when the periodic part is len 1
    if len(sequence_rep) == 2:
        min_values = recurring_convergents(max_terms[:2])
    else:
        # First option
        min_values = recurring_convergents(max_terms[:period_len])
        x, y = min_values.numerator, min_values.denominator
        # If it isn't a solution, try index 2r-1
        if x*x - d*y*y != 1:
            min_values = recurring_convergents(max_terms[:-1])
    # Minimal solution in x for Pell's equation
    x, y = min_values.numerator, min_values.denominator

    # The numerator of the fraction is the minimal x solution
    return x


def max_x_minimal_solutions(bound):
    '''Finds the value of d <= bound in minimal solutions of x for which
    the largest value of x is obtained.'''
    max_x = float('-inf')
    max_d = 0
    for d in range(2, bound+1):
        x = minimal_value(d)
        if x > max_x:
            max_x = x
            max_d = d
    return max_d


if __name__ == '__main__':
    print(minimal_value(13))  # 649
    print(max_x_minimal_solutions(7))  # 5
    print(max_x_minimal_solutions(1000))  # 661, 0.02s

# ----- #
# Notes #
# ----- #

# (1*)
# I first tried to do this by brute force, but the program wouldn't find the
# solutions, so I did some research on how to find the solutions of quadratic
# Diophantine equations. After banging my head on the wall a couple of times I
# found out that the problem deals with what is called Pell's equation.
# https://en.wikipedia.org/wiki/Pell%27s_equation

# (2*)
# The Wikipedia solution, found in
# https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
# considers Pell's equation of the form x^2 - n*y^2 = 1:
# Let hi/ki denote the unique sequence of convergents of the regular continued
# fraction of sqrt(n). [...] [The continued fraction] can be written in the
# form [floor(sqrt(n)); a1, a2, ..., a(r-1), 2*floor(sqrt(n))].
# The fundamental solution is:
#             (x1, y1) = {(h(r-1), k(r-1)),       for k even
#                         (h(2r-1), k(2r-1)),     for k odd}
# This is wrong. In my testing I've found odd numbers where the fundamental
# solution is h(r-1), k(r-1) (for example: 7, 19, 21, 23...) and even numbers
# where the fundamental solution is h(2r-1), k(2r-1) (for example: 58)
