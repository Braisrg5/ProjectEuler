"""A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from itertools import combinations_with_replacement as combinations_wr
from resources.useful_functions import sum_divisors


def is_abundant(n):
    """Checks if n is an abundant number."""
    return n > 1 and sum_divisors(n) > n


def is_sum_abundants(n, abundants):
    """Checks if n is a sum of two abundant numbers."""
    half_n = n // 2
    for num in abundants:
        if num > half_n:
            break
        if (n - num) in abundants:
            return True
    return False


def not_sum_abundants(n):
    """Generates all the numbers that are not the sum of two abundant
    numbers and that are less than n.
    """
    abundants = [i for i in range(1, n) if is_abundant(i)]
    sum_abundants = [n+m for (n, m) in combinations_wr(abundants, 2)]
    for i in range(1, n):
        if i not in sum_abundants:
            yield i
    return


def not_sum_abundants_v2(n):
    """Generates the sum of all the numbers that are not the sum of two
    abundant numbers and that are less than n.
    """
    abundants = {i for i in range(1, n+1) if is_abundant(i)}
    not_sums = set(x for x in range(1, n+1))
    for n in abundants:
        for m in abundants:
            not_sums.discard(n+m)
    return sum(not_sums)


def not_sum_abundants_v3(n):
    """Generates the sum of all the numbers that are not the sum of two
    abundant numbers and that are less than n.
    """
    abundants = {i for i in range(1, n+1) if is_abundant(i)}
    return sum(i for i in range(1, n+1) if not is_sum_abundants(i, abundants))


if __name__ == "__main__":
    # print(sum(not_sum_abundants()))  # 4179871, 647s
    # print(not_sum_abundants_v2(28123))  # 4179871, 2.5s
    print(not_sum_abundants_v3(28123))  # 4179871, 0.30s
