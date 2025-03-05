'''https://projecteuler.net/problem=56
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form a^b, where a,b < 100, what is the
maximum digital sum?
'''
from resources.useful_functions import digit_sum


def max_digit_sum(bound):
    '''Finds the maximum digital sum for natural numbers of the form a^b,
    where a, b < bound.'''
    # Keep track of the maximum digital sum found
    maximum = 0
    # Iterate over all possible values for a and b
    for a in range(1, bound):
        for b in range(1, bound):
            d_sum = digit_sum(a**b)  # Computers are strong
            # If sum is greater than maximum, update
            if d_sum > maximum:
                maximum = d_sum
    return maximum


if __name__ == '__main__':
    print(max_digit_sum(100))  # 972, 0.06s
