'''https://projecteuler.net/problem=30
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:
                1634 = 1^4 + 6^4 + 3^4 + 4^4
                8208 = 8^4 + 2^4 + 0^4 + 8^4
                9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
'''
global digit_power


def calc_bound(n):
    '''Calculates the bound for the numbers that can be written as the
    sum of nth powers of their digits.
    How I calculate the bound and why is explained in (1*).
    '''
    nine_pow = 9**n
    i, bound = 1, float('inf')
    while bound >= 10**(i-1):
        bound = i*nine_pow
        i += 1
    return bound


def pow_digit_sum(n, p):
    '''Sums the digits of a number n raised to the power p.'''
    return sum(int(i)**p for i in str(n))


def sum_sum_nth_pows(n):
    '''Sums the numbers that can be written as the sum of nth powers of
    their digits.
    '''
    # Initialize the bound and the sum
    total, bound = 0, calc_bound(n)
    # One digit numbers do not count
    for i in range(10, bound):
        # If the number fulfills the property, we can sum it
        if pow_digit_sum(i, n) == i:
            total += i
    return total


if __name__ == '__main__':
    print(sum_sum_nth_pows(4))  # 19316
    print(sum_sum_nth_pows(5))  # 443839, 0.29s


'''
#-------#
# Notes #
#-------#

(1*)
If we sum the fifth powers of the digits of 99, we get:
            2*9^5 = 118089 > 99.
We can continue to do this for a larger amount of digits:
            3*9^5 = 177147 > 999.
            4*9^5 = 236196 > 9999.
            5*9^5 = 295245 > 99999.
            6*9^5 = 354294 < 999999.
The sequence k*9^p - (10^k-1) will eventually be negative (1.1*)
The bound can then be set at 354294 because any bigger number cannot have
this property. This approach can be adapted to nth powers:
            For k = 1...
                max_num = k*9^n
                if max_num < 10^(k-1):
                    break

    (1.1*)
    f(x) = x*9^n - 10^x + 1, f is continuous
    f(1) = 9^n - 9 > 0 for n > 1
    If we take the limit when x -> +inf:
        lim_{x->+inf} x*9^n - 10^x + 1 = lim_{x->+inf} - 10^x + x*9^n + 1 =
        = lim_{x->+inf} -10^x = -inf
    Bolzano tells us that there is a root x0 between 1 and inf, so we can see
    that for the natural number k0 = ceil(x0), f(k0-1) > 0 and f(k0) < 0.
    Therefore, the bound is k0*9^n.
'''
