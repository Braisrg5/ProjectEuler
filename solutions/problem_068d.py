'''https://projecteuler.net/problem=68'''
# Consider the "magic" 3-gon rig in resources/0068_1.png, filled with the
# numbers 1 to 6, and each line adding to nine.

# Working clockwise, and starting from the group of three with the numerically
# lowest external node (4,3,2 in this example), each solution can be described
# uniquely. For example, the aforementioned solution can be described by the
# set: 4,3,2;6,2,1;5,1,3.

# It is possible to complete the ring with four different totals: 9, 10, 11 and
# 12. There are eight solutions in total.

#     Total           Solution Set
#       9           4,2,3;5,3,1;6,1,2
#       9           4,3,2;6,2,1;5,1,3
#      10           2,3,5;4,5,1;6,1,3
#      10           2,5,3;6,3,1;4,1,5
#      11           1,4,6;3,6,2;5,2,4
#      11           1,6,4;5,4,2;3,2,6
#      12           1,5,6;2,6,4;3,4,5
#      12           1,6,5;3,5,4;2,4,6

# By concatenating each group it is possible to form 9-digit strings; the
# maximum string for a 3-gon is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to
# form 16- and 17-digit strings. What is the maximum 16-digit string for a
# "magic" 5-gon ring?

# See resources/0068_2.png
from itertools import permutations
from time import perf_counter
from tqdm import tqdm
import numpy as np


def lowest_permutations(n):
    '''Finds all the permutations of the external nodes of a n-gon ring where
    the first value is the lowest external node, explained in (1.1*).'''
    # Numbers in the n-gon ring
    nums = list(range(1, 2*n + 1))
    # Max value for the lowest external node
    max_num = n + 1
    perms = []
    for i in range(max_num):
        # Permutations for the external node i
        for perm in permutations(nums[i+1:], n-1):
            perms.append((i+1,) + perm)
    return perms


def remove_permutations(perms):
    '''For the special case n=5, removes the permutations of the external nodes
    that don't contain the number 10, as seen in (1.2*)'''
    perms = [perm for perm in perms if any(el == 10 for el in perm)]
    return perms


def check_permutation(perm, n, limits, a):
    '''Checks if the current permutation of the external nodes give a
    solution for the internal nodes that makes sense.'''
    low_lim, high_lim = limits
    for i in range(low_lim, high_lim+1):
        # Create vector y
        y = [i - el for el in perm]
        # Solution of the system described in (1*)
        sol = np.linalg.solve(a, y).tolist()
        # Valid if all are integers
        if all(s.is_integer() for s in sol):
            sol = [int(s) for s in sol]
            ngon = list(perm) + sol
            # All values are between 1 and 2*n
            if all(1 <= x <= 2*n for x in ngon):
                # Exactly 2n values
                if len(set(ngon)) == len(ngon) == 2*n:
                    return sol
    return False


def ngon_permutations(n):
    '''Finds all the possible ordered sets of the elements 1-2n for which a
    "magic" n-gon ring is possible.'''
    perms = lowest_permutations(n)
    if n == 5:
        perms = remove_permutations(perms)

    limits = (6, sum(range(2*n, 2*n-3, -1)))
    # Creation of matrix A
    x = np.zeros(n)
    x[:2] = 1
    a = np.matrix(x)
    for shift in range(1, n):
        a = np.vstack([a, np.roll(x, shift)])

    pandigital_perms = []
    for perm in tqdm(perms):
        internal = check_permutation(perm, n, limits, a)
        if internal:
            digit_string = ''
            for i, el in enumerate(perm):
                if i == (n-1):
                    str_sum = str(el) + str(internal[n-1]) + str(internal[0])
                    digit_string += str_sum
                else:
                    str_sum = str(el) + str(internal[i]) + str(internal[i+1])
                    digit_string += str_sum
            pandigital_perms.append(int(digit_string))
    return max(pandigital_perms)


def check_permutation_v2(ext_perm, rest_perms):
    '''Checks if a permutation of the external nodes is valid by checking if
    there exists a permutation of the rest of the values'''
    x1, x2, x3, x4, x5 = ext_perm
    for int_perm in rest_perms:
        a, b, c, d, e = int_perm
        val = x1 + a + b
        if (
            x2 + b + c == val and x3 + c + d == val and
            x4 + d + e == val and x5 + e + a == val
        ):
            return int_perm
    return False


# Optimized case for n == 5
def five_gon_permutations():
    '''Finds all the possible ordered sets of the elements 1-10 for which a
    "magic" 5-gon ring is possible.
    Returns the maximum 16-digit string for a "magic" 5-gon ring.'''
    n = 5
    nums = set(range(1, 2*n+1))
    perms = lowest_permutations(n)
    perms = remove_permutations(perms)

    valid = []
    for perm in perms:
        rest = list(nums-set(perm))
        rest_perms = permutations(rest)
        internal = check_permutation_v2(perm, rest_perms)
        if internal:
            digit_string = ''
            for i, node in enumerate(perm):
                if i == (n-1):
                    str_sum = str(node) + str(internal[n-1]) + str(internal[0])
                    digit_string += str_sum
                else:
                    str_sum = str(node) + str(internal[i]) + str(internal[i+1])
                    digit_string += str_sum
            valid.append(int(digit_string))
    return max(valid)


if __name__ == '__main__':
    start = perf_counter()
    print(ngon_permutations(3))  # 6531031914842725: 14
    print(perf_counter() - start)
    start = perf_counter()
    print(five_gon_permutations())  # 14870663820: 14
    print(perf_counter() - start)


# ----- #
# Notes #
# ----- #

# (1*)
# For a 5-gon ring, there are 10 possible values and 5 total sums. If we name
# this values from a to j, we can form a system of equations as follows:
#             a + b     + d                         = t
#                     c + d     + f                 = t
#                             e + f     + h         = t
#                                     g + h     + j = t
#             a                             + i + j = t
# being t the value that we want each line to add to. If we want to find a
# solution for the system, we need to fix the value of 5 out of the possible
# values (so that the dimension of the solution set is 0). It makes sense to
# fix the external nodes, because our strings depend on them, so that's what
# I'm going to do.

# After fixing the outside values (x1,...,x5), the resulting system will be:
#             a + b             = t - x1 = y1
#                 b + c         = t - x2 = y2
#                     c + d     = t - x3 = y3
#                         d + e = t - x4 = y4
#             a               e = t - x5 = y5
# where (a, b, c, d, e) are the vertices of the inside pentagon.

# With a bit of Algebra (or a lot), we can find the general solution for this
# system of equations:
#             a = (y1 - y2 + y3 - y4 + y5)/2
#             b = (y1 + y2 - y3 + y4 - y5)/2
#             c = (-y1 + y2 + y3 - y4 + y5)/2
#             d = (y1 - y2 + y3 + y4 - y5)/2
#             e = (-y1 + y2 - y3 + y4 + y5)/2
# Or, taking out the common factor t:
#             a = (t - x1 + x2 - x3 + x4 - x5)/2
#             b = (t - x1 - x2 + x3 - x4 + x5)/2
#             c = (t + x1 - x2 - x3 + x4 - x5)/2
#             d = (t - x1 + x2 - x3 - x4 + x5)/2
#             e = (t + x1 - x2 + x3 - x4 - x5)/2

# (1.1*)
# Now, we have to think about what values can our (x1,...,x5) be. If we set x1
# to be the lowest external node, we will have:
#             x1 = 1 => 9*8*7*6 permutations; e.g., (1, 7, 6, 5, 4)
#             x1 = 2 => 8*7*6*5 permutations; e.g., (2, 4, 10, 5, 3)
#             x1 = 3 => 7*6*5*4 permutations; e.g., (3, 4, 5, 7, 9)
#             x1 = 4 => 6*5*4*3 permutations; e,g., (4, 10, 9, 5, 6)
#             x1 = 5 => 5*4*3*2 permutations; e.g., (5, 7, 8, 9, 10)
#             x1 = 6 => 4*3*2*1 permutations; e.g., (6, 10, 9, 8, 7)
# x1 can't be greater than 6, because we wouldn't have any more values to
# ensure that it remains the smaller.

# (1.2*)
# Also, once we have our (x1,...,x5) and (a, b, c, d, e), the string, as
# explained in the statement, is formed by concatenating the sums, so:
#             x1ab;x2bc;x3cd;x4de;x5ea
# which is formed by 15 elements
# Elements x1,...,x5 each appear once, and the inside nodes each appear twice.
# To have a 16-digit string, 10 has to be one of the x1,...,x5 elements,
# further reducing the permutations we have to check.
