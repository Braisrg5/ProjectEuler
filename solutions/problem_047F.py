'''https://projecteuler.net/problem=47'''
# The first two consecutive numbers to have two distinct prime factors are:

#             14 = 2 * 7
#             15 = 3 * 5.

# The first three consecutive numbers to have three distinct prime factors are:

#             644 = 2² * 7 * 23
#             645 = 3 * 5 * 43
#             646 = 2 * 17 * 19.

# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these numbers?
from resources.useful_functions import prime_factors


def transform_factors_v2(n):
    '''Transforms the list of factors of a number into a list of the powers of
    the factors.'''
    pf = prime_factors(n)
    return [p ** pf.count(p) for p in sorted(set(pf))]


def distinct_pf(x, upper, lower=0):
    '''Finds the first x consecutive integers with x distinct prime factors.'''
    # The lowest bound is set to 10^(x-1). This is a wild guess and could
    # probably be improved.
    if lower == 0:
        lower = 10**(x-1)
    n = lower
    x_squared = x * x

    # Calculate for the first x consecutive integers
    # We use sets to check easily if they're disjoint
    factors = [set(transform_factors_v2(n+i)) for i in range(x)]
    while n < upper:
        # We check if all are of length x
        if all(len(f) == x for f in factors):
            all_factors = set.union(*factors)
            # And if the number of distinct prime factors is x^2
            if len(all_factors) == x_squared:
                # In that case, we found the solution
                return factors, n
        n += 1
        # Otherwise, we move on to the next number and update the factors
        # We can take advantage of the previous calculated factors
        factors = factors[1:] + [set(transform_factors_v2(n+x-1))]
    # Bound isn't large enough to find the solution
    return -1


if __name__ == '__main__':
    print(distinct_pf(2, 100))  # 14
    print(distinct_pf(3, 1000))  # 644
    print(distinct_pf(4, 200000))  # 134043, 0.51
