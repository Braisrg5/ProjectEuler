'''https://projecteuler.net/problem=80'''
# It is well known that if the square root of a natural number is not an
# integer, then it is irrational. The decimal expansion of such square roots is
# infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital sum of
# the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.
from decimal import getcontext, Decimal


def decimal_expansion_sqrt(n, prec=100):
    '''Finds the decimal expansion of the square root of n for a certain
    precision.'''
    getcontext().prec = prec+2
    dec_n = Decimal(n)
    return dec_n.sqrt()


def sum_decimals(x, prec=100):
    '''Sums the first prec decimal digits of a Decimal number x.'''
    str_x = str(x).replace('.', '')
    return sum(int(d) for d in str_x[:prec])


def sum_square_digital_expansion(bound, prec=100):
    '''Finds the total of the digital sums of the first prec decimal digits for
    the first bound natural numbers.'''
    total = 0
    for i in range(1, bound+1):
        sqrt_i = decimal_expansion_sqrt(i, prec)
        # Exact root, not interested
        if sqrt_i % 1 == 0:
            continue
        total += sum_decimals(sqrt_i, prec)
    return total


def main():
    '''Main code of module.'''
    print(sum_square_digital_expansion(2))  # 475
    print(sum_square_digital_expansion(100))  # 40886


if __name__ == '__main__':
    main()
