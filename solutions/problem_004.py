'''https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.


Find the largest palindrome made from the product of two 3-digit numbers.
'''
from resources.useful_functions import is_palindrome


def palindromes():
    '''Returns the largest palindromic number that is a product of two
    3-digit numbers.
    '''
    largest = 0
    # Generate all 3-digit numbers pairs from biggest to smallest
    for i in range(999, 100, -1):
        for j in range(999, i - 1, -1):
            large = i * j
            # If the new product is larger than the current largest palindrome
            # and it is a palindrome, update the value
            if large > largest and is_palindrome(large):
                largest = large
    return largest


if __name__ == '__main__':
    print(palindromes())  # 906609, 0.07s
