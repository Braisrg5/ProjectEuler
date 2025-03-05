'''https://projecteuler.net/problem=20
n! means n x (n-1) x ... x 3 x 2 x 1.
For example, 10! = 10 x 9 x... x 3 x 2 x 1 = 3628800, and the sum of the digits
in the number 10! is 3 + 6 + 2 + 8 + 0 + 0 = 27

Find the sum of the digits in the number 100!.
'''
from resources.useful_functions import digit_sum
from math import factorial


if __name__ == '__main__':
    print(digit_sum(factorial(10)))  # 277
    # Computers are strong
    print(digit_sum(factorial(100)))  # 648, 0.0s
