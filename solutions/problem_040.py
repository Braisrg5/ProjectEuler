'''https://projecteuler.net/problem=40
An irrational decimal fraction is created by concatenating the positive
integers:

            0.123456789101112131415161718192021...

It can be seen that the 12^th digit of the fractional part is 1.

If d[n] represents the n^th digit of the fractional part, find the value
of the following expression.

            d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
'''
from math import prod


def calc_start(nth):
    '''Calculates the last power of 10 for which the decimal position of its
    first digit is less than nth in the number 0.12345678910111213...'''
    index, exp = 0, 1
    # Index for the first digit of 10
    next_index = 9 * 10**(exp - 1) * exp

    # If we haven't surpassed the desired number
    while next_index < nth:
        # Update the index to return
        index = next_index
        # Increase the exponent
        exp += 1
        # Index for the first digit of 10^exp
        next_index = next_index + 9 * 10**(exp - 1) * exp

    # Number of digits in the appropriate power of 10
    digits = exp
    return index, digits


def find_digit(nth):
    '''Finds the nth digit in the decimal number 0.123456789101112131415...'''
    nth -= 1  # Adjust for 0-based indexing
    # Find the last power of 10 for which the decimal position of its first
    # digit is less than nth
    start, digits = calc_start(nth)
    # The aforementioned power of 10 and the index of its first digit
    current_num, current_index = 10**(digits-1), start

    # Move by steps of digits until we surpass the nth digit
    while current_index <= nth:
        current_index += digits
        current_num += 1
    # We surpassed so we need to go back to the previous step
    current_index -= digits
    current_num -= 1

    # Find the correct index of the current number
    diff = nth - (current_index)
    digit = str(current_num)[diff]

    # Return d[nth]
    return int(digit)


def digit_prod():
    '''Calculates the value of the expression d[1] * d[10] * ... * d[1000000]
    '''
    return prod(find_digit(10**i) for i in range(7))


if __name__ == '__main__':
    print(find_digit(17))
    print(digit_prod())  # 210, 0.005


'''
#-------#
# Notes #
#-------#

(1*)
What is the index of the first digit of the number 10?
Before 10, there are 9 numbers of length 1 and the indexes begin at 0.
D = 9*1 = 9

What is the index of the first digit of the number 100?
9 numbers of length 1 and 90 of length 2
D = 9*1 + (99-10+1)*2 = 189

What is the index of the first digit of the number 1000?
9 numbers of length 1, 90 of length 2 and 900 of length 3
D = 9*1 + (99-10+1)*2 + (999-100+1)*3 + 1 = 2889

What is the index of the first digit of the number 10^x?
We just repeat the sum until we reach the desired power of 10.
D = 9*1 + 9*10*2 + 9*100*3 + ... + 9*10^(x-1)*x =
= sum(9*10^(i-1)*i for i in range(1, x+1)).

So, we can find the last D that is smaller than nth, and then keep adding the
appropriate number of digits until we surpass nth.
Once there, we will have a candidate, we only need to find the correct index.
'''
