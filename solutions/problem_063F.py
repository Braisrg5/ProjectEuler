'''https://projecteuler.net/problem=63
The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also a nth power?
'''
from math import ceil, pow


def n_digit_power():
    '''Finds how many of n-digit positive integers that are also a nth power.
    The process is explained in (1*).'''
    count = 0
    for i in range(1, 22):
        low = ceil(pow(10, (i-1)/i))
        count += 10 - low
    return count


if __name__ == '__main__':
    print(n_digit_power())


'''
#-------#
# Notes #
#-------#

(1*)
For n = 2:
            10 <= x^2 < 100
            10^(1/2) <= x < 10 -> 3.16 <= x < 10 -> 4 <= x < 100

For n = 3:
            100 <= x^3 < 1000
            100^(1/3) <= x < 10 -> 4.64 <= x < 10 -> 5 <= x < 10

For an arbitrary n:
            10^(n-1) <= x^n < 10^n
            10^((n-1)/n) <= x < 10
x has to be an integer, so we can check for what n the expression
10^((n-1)/n) > 9 (in that case, 9 < x < 10, so x can't be an integer).
            10^((n-1)/n) > 9 -> (n-1)/n > log(9) -> n-1 > n*log(9)
            n*(1-log(9)) > 1 -> n > 1/(1-log(9)) ≈ 21.85
So:
            9^21 = 109418989131512359209  has 21 digits.
            9^22 = 984770902183611232881 also 21 digits.

For each n, the amount of n-digit numbers that are also n-th powers will be
precisely the sum of the differences between 10 and ceil(10^((n-1)/n))
'''
