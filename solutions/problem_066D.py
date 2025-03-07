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
from tqdm import tqdm
from problem_065f import recurring_convergents


def minimal_value(d):
    '''Finds the minimal solution in x for the Diophantine equation
    x^2 - d*y^2 = 1.'''
    # d can't be a square
    if sqrt(d).is_integer():
        return float('-inf')

    y = 1
    while not sqrt(1 + d*y**2).is_integer():
        y += 1
    return int(sqrt(1 + d*y**2))


def max_x_minimal_solutions(bound):
    '''Finds the value of d <= bound in minimal solutions of x for which
    the largest value of x is obtained.'''
    max_x = float('-inf')
    max_d = 0
    for d in tqdm(range(2, bound+1)):
        x = minimal_value(d)
        if x > max_x:
            max_x = x
            max_d = d
    return max_d


if __name__ == '__main__':
    # print(minimal_value(13))  # 649
    # print(max_x_minimal_solutions(7))  # 5
    # Not viable, some d do NOT give a solution
    # print(max_x_minimal_solutions(1000))

    terms = [2, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    for i in range(len(terms)):
        print(recurring_convergents(terms[:i+1]))


# ----- #
# Notes #
# ----- #

# (1*)
# I first tried to do this by brute force, but the program wouldn't find the
# solutions, so I did some research on how to find the solutions of quadratic
# Diophantine equations. I stumbled upon this article:
# https://www.alpertron.com.ar/METHODS.HTM

# Our equation is:
#             x^2 - d*y^2 - 1 = 0 (I'm using lowercase d to avoid confusion)
# so, A = 1, B = 0, C = -d, D = 0, E = 0, F = -1.
# Then
#             B^2 - 4AC = 4d > 0 -> Hyperbolic case
# https://www.alpertron.com.ar/METHODS.HTM#Hyperb

# F != 0 and B^2 - 4AC = 4d = (2sqrt(d))^2, but d is never a square
# (statement), so 4d is not a perfect square.

# gcd(A, B, C) = gcd(1, 0, -d) = gcd(1, d) = 1 = -F, so F is a multiple of gcd.

# B^2 - 4AC = 4d > 4 = 4*F^2, for d > 1.

# So, as the paper says,
#   "the solutions of the equation will be amongst the convergents of the
#   continued fraction of the roots of the equation At2 + Bt + C = 0. The
#   continued fraction expansion of a quadratic irrationality is periodic.
#   Since B2 - 4AC is not a perfect square the number of solutions will be
#   infinite or none"

# So, in order to
