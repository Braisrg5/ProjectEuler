"""The decimal number, 585 = 1001001001 (binary), is palindromic in
both bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not
include leading zeros.)
"""


from resources.useful_functions import is_palindrome


def palindrome_sum(bound):
    """Finds the sum of all numbers that are palindromic in base 10 and
    base 2.
    """
    s = 0
    for i in range(1, bound):
        if is_palindrome(i):
            bin_i = int("{0:b}".format(i))
            if is_palindrome(bin_i):
                s += i
    return s


def palindrome_sum_v2(bound):
    """Finds the sum of all numbers that are palindromic in base 10 and
    base 2.
    """
    s = 0
    # Only odd numbers can be palindromic in base 2
    for i in range(1, bound, 2):
        if is_palindrome(i):
            bin_i = int("{0:b}".format(i))
            if is_palindrome(bin_i):
                s += i
    return s


if __name__ == "__main__":
    print(palindrome_sum(1000000))  # 872187, 0.36s
    print(palindrome_sum_v2(1000000))  # 872187, 0.19s
