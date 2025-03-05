'''https://projecteuler.net/problem=23
A perfect number is a number for which the sum of its proper divisors is
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
'''
from resources.useful_functions import sum_divisors


def is_abundant(n):
    '''Checks if n is an abundant number.'''
    return n > 1 and sum_divisors(n) > n


def is_sum_abundants(n, abundants):
    '''Checks if n is a sum of two abundant numbers.'''
    # Integer division for the half of the number (eq to floor(n/2))
    half_n = n//2
    # We iterate over the abundant numbers from smallest to largest
    for num in abundants:
        # If the abundant number is greater than half of n, we can stop (1*)
        if num > half_n:
            break
        if (n - num) in abundants:
            return True
    return False


def not_sum_abundants_v3(n):
    '''Generates the sum of all the numbers that are not the sum of two
    abundant numbers and that are less than n.
    '''
    # Set of all the abundant numbers
    abundants = {i for i in range(1, n+1) if is_abundant(i)}
    # If the number is not a sum of abundants, we add it to the sum
    return sum(i for i in range(1, n+1) if not is_sum_abundants(i, abundants))


if __name__ == '__main__':
    print(not_sum_abundants_v3(28123))  # 4179871, 0.55s


'''
#-------#
# Notes #
#-------#

(1*)
We iterate through the list of abundant numbers in increasing order.
For each abundant number num, we check if the difference n - num is also in the
set of abundant numbers. If both num and (n - num) are abundant numbers, then n
can be expressed as the sum of two abundant numbers, num + (n - num) = n.

We can stop the test when num is greater than n/2, because at that point
(n - num) > num and we would be running over values we already checked.
'''
