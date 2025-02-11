"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial
of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.


The bound is taken because 7*9! = 2540160 < 9999999.

In sum_sum_factorial_v2, what I'm doing is to find all the possible
sums that there can be done with the factorials of the digits, because,
for example, 1! + 4! + 5! = 4! + 1! + 5!, but only one of 145 and 415
is the sum of the factorials of its digits.
So, I create combinations_wr of the factorials of the numbers 1 to 10,
also 0, and here's why:
For combinations_wr, 0034 is the same as 3400, but the sums of the
factorials of their digits are 30 and 32, respectively. So, we need to
take into account this cases.

What I did is, given a tuple (0, 0, ..., x, ...), where x is the first
number that is not 0 (and, because of how the function works, any
number after x won't be 0 either), I create n+1 different tuples, where
n is the number of zeros, of the form:
                (0, 0, ..., x, ...)
                (1, 0, ..., x, ...)
                (2, 0, ..., x, ...)
                ...
                (n, 0, ..., x, ...)
That way covering every case where any number of 0s are before or after
the first non-zero digit.
"""


from math import factorial, floor, log10
from itertools import combinations_with_replacement as combinations_wr


def is_sum_digit_factorial(n, factorials=[factorial(i) for i in range(10)]):
    """Checks if a number is the sum of the factorials of its
    digits.
    """
    return sum([factorials[int(i)] for i in str(n)]) == n


def sum_sum_factorial(bound):
    """Finds the sum of the numbers that are the sum of the factorials
    of their digits.
    """
    factorials = [factorial(i) for i in range(10)]
    s = 0
    for i in range(10, bound):
        if is_sum_digit_factorial(i, factorials):
            s += i
    return s


def transform(combs):
    """Transforms the combinations to add the cases explained at the
    beginning.
    """
    combs_copy = combs.copy()
    for i in range(len(combs)):
        c = list(combs[i])
        if c[0] != 0:
            break
        else:
            for i in range(len(c)):
                if c[i] != 0:
                    for j in range(1, i + 1):
                        c[0] = j
                        combs_copy.append(tuple(c))
    return combs_copy


def sum_sum_factorial_v2(bound):
    """Finds the sum of the numbers that are the sum of the factorials
    of their digits.
    """
    factorials = [factorial(i) for i in range(1, 10)]
    digits_lim = floor(log10(bound)) + 1
    all_combinations = list(combinations_wr([0] + factorials, digits_lim))
    all_combinations = transform(all_combinations)
    sums = {sum(c) for c in all_combinations}
    sum_factorial = []
    for num in sums:
        if num >= 10 and is_sum_digit_factorial(num, [1] + factorials):
            sum_factorial.append(num)
    return sum(sum_factorial)


if __name__ == "__main__":
    print(is_sum_digit_factorial(145))  # True
    # print(sum_sum_factorial(2540160))  # 40730, 3.17s
    print(sum_sum_factorial_v2(2540160))  # 40730, 0.06s
