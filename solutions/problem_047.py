'''The first two consecutive numbers to have two distinct prime factors are:

            14 = 2 * 7
            15 = 3 * 5.

The first three consecutive numbers to have three distinct prime factors are:

            644 = 2² * 7 * 23
            645 = 3 * 5 * 43
            646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
'''
from resources.useful_functions import prime_factors
from collections import Counter
from time import perf_counter


def transform_factors(n):
    '''Transforms the list of factors of a number into a list of the powers of
    the factors.'''
    pf = prime_factors(n)
    fact_count = Counter(pf)
    return [fact ** count for fact, count in fact_count.items()]


def distinct_pf(x, MAX, MIN=0):
    '''Finds the first x consecutive integers with x distinct prime factors'''
    # The lowest bound is set to 10^(x-1). This is a wild guess and could
    # probably be improved.
    if MIN == 0:
        MIN = 10**(x-1)
    n = MIN
    # Calculate for the first x consecutive integers
    # We use sets to check easily if they're disjoint
    factors = [set(transform_factors(n+i)) for i in range(x)]
    while n < MAX:
        # We check if all are of length x and if they're disjoint
        if all(len(f) == x for f in factors) and all(
            factors[i].isdisjoint(factors[j])
            for i in range(x) for j in range(i+1, x)
        ):
            # In that case, we found the solution
            return factors, n
        n += 1
        # Otherwise, we move on to the next number and update the factors
        # We can take advantage of the previous calculated factors
        factors = factors[1:] + [set(transform_factors(n+x-1))]
    return -1


if __name__ == '__main__':
    start = perf_counter()
    print(distinct_pf(2, 100))  # 14
    print(distinct_pf(3, 1000))  # 644
    print(distinct_pf(4, 200000))  # 134043
    print(perf_counter() - start)  # 0.5967s
