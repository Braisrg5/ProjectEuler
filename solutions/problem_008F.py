'''https://projecteuler.net/problem=8
The four adjacent digits in the 1000-digit number in the file that
have the greatest product are 9 x 9 x 8 x 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number in
8_big_number.txt that have the greatest product. What is the value of
this product?
'''
from functools import reduce


def load_number(path):
    '''Loads the 1000-digit number from path and returns it as a
    string.'''
    with open(path, 'r') as file:
        num = ''.join([i.replace('\n', '') for i in file.readlines()])
    return num


def prod_adj_dig(n):
    '''Finds the nth adjacent digits in the 1000-digit number with the
    greatest product.
    '''
    num = load_number('resources/8_big_number.txt')
    digits = len(num)
    # The total number of products is the length of the number minus the amount
    # of digits we want to multiply plus one (1*)
    totalProds = digits - n + 1
    biggest = 1
    for i in range(totalProds):
        # We select, convert and multiply the adjacent digits
        adj = [int(dig) for dig in num[i:n + i]]
        product = reduce(lambda x, y: x * y, adj)
        if product > biggest:
            biggest = product
    return biggest


if __name__ == '__main__':
    print(prod_adj_dig(4))  # 5832
    print(prod_adj_dig(13))  # 23514624000, 0.003s


'''
#-------#
# Notes #
#-------#

(1*)
For example, the number 1234567890 has 10 digits, and all of the possible 4
adjacent digits would be:

    1234, 2345, 3456, 4567, 5678, 6789, 7890

Which is precisely 10 - 4 + 1 = 7 possible products.
'''
