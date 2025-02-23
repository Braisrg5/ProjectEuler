'''https://projecteuler.net/problem=32
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
'''
from itertools import permutations
from resources.useful_functions import is_pandigital


def check_1st(perm):
    '''Checks if the given permutation satisfies the first operation.'''
    LHS = int(perm[0]) * int(perm[1:5])
    RHS = int(perm[5:])
    return LHS == RHS


def check_2nd(perm):
    '''Checks if the given permutation satisfies the second operation.'''
    LHS = int(perm[:2]) * int(perm[2:5])
    RHS = int(perm[5:])
    return LHS == RHS


def pandigital_products():
    '''Find the sum of all products that are the result of a pandigital
    multiplication 1 to 9.'''
    # Generate all permutations of 1 to 9
    perms = [''.join(p) for p in permutations('123456789')]
    solutions = set()
    for perm in perms:
        # If the permutation satisfies either operation, add product to set
        if check_1st(perm) or check_2nd(perm):
            prod = int(perm[5:])
            solutions.add(prod)
    return sum(solutions)


def pandigital_products_v2():
    '''Find the sum of all products that are the result of a
    pandigital multiplication 1 to 9, using a more efficient method.'''
    # Solutions set
    solutions = set()
    # Iterate through all possible products for the first option
    for i in range(1, 10):
        for j in range(1234, 9876):
            result = i*j
            if result < 9877 and is_pandigital(str(result) + str(i) + str(j)):
                # The result is the right size and it is pandigital
                solutions.add(result)

    # Iterate through all possible products for the second option
    for i in range(12, 98):
        for j in range(123, 987):
            result = i*j
            if result < 9877 and is_pandigital(str(result) + str(i) + str(j)):
                # The result is the right size and it is pandigital
                solutions.add(result)
    return sum(solutions)


if __name__ == '__main__':
    print(check_2nd('391867254'))  # True
    # print(pandigital_products())  # 45228, 0.25s
    print(pandigital_products_v2())  # 45228, 0.019s


'''
#-------#
# Notes #
#-------#

(1*)
The only options for the position of the multiplication and equal sign are:
            1 x 2345 = 6789
            12 x 345 = 6789
            123 x 45 = 6789
            1234 x 5 = 6789
Iterating for the first and fourth equation would give the same results, and
the same happens with the second and third. So, for each permutation, we only
need to check for the first and second operations.
'''
