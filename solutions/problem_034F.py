'''https://projecteuler.net/problem=34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial, floor, log10
from itertools import combinations_with_replacement as combinations_wr


def is_sum_digit_factorial(n, factorials=[factorial(i) for i in range(10)]):
    '''Checks if a number is the sum of the factorials of its digits.'''
    return sum(factorials[int(i)] for i in str(n)) == n


def transform(combs):
    '''Transforms the combinations to add the cases explained in (1*).'''
    combs_copy = combs.copy()
    for i in range(len(combs)):
        c = list(combs[i])
        # If the first digit is not 0, we're not interested in this combination
        # or any of the next ones (they are ordered)
        if c[0] != 0:
            break

        # Run through each value of the combination
        for i in range(len(c)):
            # We find the index of the first non-zero digit
            if c[i] != 0:
                # And add a new combination from 1 to the index
                for j in range(1, i + 1):
                    c[0] = j
                    combs_copy.append(tuple(c))
    # List with the old and new combinations
    return combs_copy


def sum_sum_factorial_v2(bound):
    '''Finds the sum of the numbers that are the sum of the factorials of their
    digits.'''
    # Generate all combinations of the factorials of numbers 1 to 9,
    factorials = [factorial(i) for i in range(1, 10)]
    # The max number of digits for a number to have the property
    digits_lim = floor(log10(bound)) + 1

    # Combinations of the factorials of numbers and 0
    all_combinations = list(combinations_wr([0] + factorials, digits_lim))
    # Transform the combinations to add the cases explained in (1*)
    all_combinations = transform(all_combinations)
    # Find out all distinct sums of the combinations
    sums = {sum(c) for c in all_combinations}
    print(max(sums))

    # Initialize the list of numbers that can be written as the sum of the
    # factorials of their digits
    sum_factorial = []
    # Check each number in the set of sums
    for num in sums:
        # The number has to be at least 10 and have the property
        if num >= 10 and is_sum_digit_factorial(num, [1] + factorials):
            sum_factorial.append(num)
    return sum_factorial


if __name__ == '__main__':
    print(is_sum_digit_factorial(145))  # True
    # print(sum_sum_factorial(2540160))  # 40730, 3.17s
    print(sum_sum_factorial_v2(2540160))  # 40730, 0.06s


'''
#-------#
# Notes #
#-------#

(1*)
The bound is selected because 7*9! = 2540160 < 9999999, so any number bigger
than 2540160 can't have the property.

In sum_sum_factorial_v2, what I'm doing is to find all the possible sums that
can be done with the factorials of the digits, because, for example,
1! + 4! + 5! = 4! + 1! + 5!, but only 145 satisfies the condition, so the
number of possibilities is drastically reduced.

So, I create combinations_wr of the factorials of the numbers 1 to 10, and
also 0, and here's why:
For combinations_wr, 0034 is the same as 3400, but the sums of the factorials
of their digits are 30 and 32, respectively. So, we need to take into account
this cases.

What I did is, given a tuple (0, 0, ..., x, ...), where x is the first number
that is not 0, we will say that x is in the position n+1. I then create n+1
different tuples of the form:
                (0, 0, ..., x, ...)
                (1, 0, ..., x, ...)
                (2, 0, ..., x, ...)
                ...
                (n, 0, ..., x, ...)
That way covering every case where any number of 0s are before or after the
first non-zero digit.

For example, I can have the tuple (0, 0, 0, 1, 2, 6) and the transformed tuples
would be:
            (0, 0, 0, 1, 2, 6) (Number 123, for example)
            (1, 0, 0, 1, 2, 6) (Number 1203, for example)
            (2, 0, 0, 1, 2, 6) (Number 10023, for example)
            (3, 0, 0, 1, 2, 6) (Number 102003, for example)
'''
