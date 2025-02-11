"""Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:
                1634 = 1^4 + 6^4 + 3^4 + 4^4
                8208 = 8^4 + 2^4 + 0^4 + 8^4
                9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.


If we sum the fifth powers of the digits of 999999, we get
6*9^5 = 354294 < 999999. I will set the bound at 354294 because any
bigger number cannot have this property.
After a while, I've further expanded the approach for nth powers.
"""


def calc_bound(n):
    """Calculates the bound for the numbers that can be written as the
    sum of nth powers of their digits.
    """
    nine_pow = 9**n
    i = 2
    while True:
        bound = i*nine_pow
        if bound < int("9"*i):
            break
        i += 1
    return bound


def pow_digit_sum(n, power):
    """Sums the digits in base 10 of a number n."""
    return sum([int(i)**power for i in str(n)])


def sum_sum_nth_pows(n):
    """Sums the numbers that can be written as the sum of nth powers of
    their digits.
    """
    bound = calc_bound(n)
    sum_nth = set()
    for i in range(10, bound):
        if pow_digit_sum(i, n) == i:
            sum_nth.add(i)
    return sum_nth


if __name__ == "__main__":
    print(sum_sum_nth_pows(4))  # 19316
    print(sum_sum_nth_pows(5))  # 443839, 0.53s
