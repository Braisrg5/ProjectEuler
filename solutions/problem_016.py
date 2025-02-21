'''https://projecteuler.net/problem=16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

from resources.useful_functions import digit_sum


if __name__ == '__main__':
    print(digit_sum(2**15))  # 26
    print(digit_sum(2**1000))  # 1366, 0.0s
