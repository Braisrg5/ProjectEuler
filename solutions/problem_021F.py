'''https://projecteuler.net/problem=21'''
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
# 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
# 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
from resources.useful_functions import sum_divisors


def is_amicable(n):
    '''Checks if n is an amicable number.'''
    if n == 1:
        return False

    # We first find the number that is the sum of the divisors of n
    friend_n = sum_divisors(n)
    # If this number is equal to n, it is not amicable (it's perfect)
    if friend_n == n:
        return False
    # If the sum of friend_n's divisors is equal to n, then n is amicable
    if sum_divisors(friend_n) == n:
        return True
    # If the above tests fails, then n is not amicable
    return False


def sum_amicables(bound):
    '''Sums all amicable numbers under a given bound.'''
    return sum(i for i in range(1, bound) if is_amicable(i))


if __name__ == '__main__':
    print(is_amicable(284))  # True
    print(is_amicable(220))  # True
    print(sum_amicables(10000))  # 31626, 0.08s
