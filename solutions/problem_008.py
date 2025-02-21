'''The four adjacent digits in the 1000-digit number in the file that
have the greatest product are 9 x 9 x 8 x 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number in
8_big_number.txt that have the greatest product. What is the value of
this product?
'''
from functools import reduce


def load_number(path):
    '''Loads the 1000-digit number from path and returns it as a
    string.'''
    file = open(path, 'r')
    num = ''.join([i.replace('\n', '') for i in file.readlines()])
    file.close()
    return num


def prod_adj_dig(n):
    '''Finds the nth adjacent digits in the 1000-digit number with the
    greatest product.
    '''
    num = load_number('resources/8_big_number.txt')
    digits = len(num)
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
