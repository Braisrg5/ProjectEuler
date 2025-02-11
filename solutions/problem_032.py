"""We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once; for example, the 5-digit number,
15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9
pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.

The only options for the position of the multiplication and equal sign
are:
                1 x 2345 = 6789
                12 x 345 = 6789
                123 x 45 = 6789
                1234 x 5 = 6789
Computing for the first and fourth would give the same results, and
the same happens with the second and third. So, for each permutation,
we need to check only the first and second operations.
"""


from itertools import permutations


def check_1st(perm):
    """Checks if given permutation satisfies the first operation."""
    return int(perm[0]) * int(perm[1:5]) == int(perm[5:])


def check_2nd(perm):
    """Checks if given permutation satisfies the second operation."""
    return int(perm[:2]) * int(perm[2:5]) == int(perm[5:])


def pandigital_products():
    """Find the sum of all products that are the result of a
    pandigital multiplication 1 to 9."""
    perms = [''.join(p) for p in permutations('123456789')]
    solutions = set()
    for perm in perms:
        prod = int(perm[5:])
        if check_1st(perm):
            solutions.add(prod)
        elif check_2nd(perm):
            solutions.add(prod)
    return sum(solutions)


if __name__ == "__main__":
    print(check_2nd("391867254"))  # True
    print(pandigital_products())  # 45228, 0.51s
