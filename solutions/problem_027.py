'''https://projecteuler.net/problem=27
Euler discovered the remarkable quadratic formula:
                n^2 + n + 41
It turns out that the formula will produce 40 primes for the
consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 +
40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
The incredible formula n^2 - 79n + 1601 was discovered, which produces
80 primes for the consecutive values 0 <= n <= 79. The product of the
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
                n^2 + an + b, where |a| < 1000 and |b| <= 1000
                where |n| is the modulus/absolute value of n
                e.g. |11| = 11 and |-4| = 4.
Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.


When n = 0, n^2 + an + b = b, and this has to be a prime, let's call it
p. Also, when n = 1, n^2 + an + b = 1 + a + p, which is also a prime,
let's call it p'. So, instead of looking for a and b, we can search for
p and p'.
                0 < p < 1000
                1 + a + p = p'  =>  a = p' - p - 1
                |a| = |p' - p - 1| < 1000
                -1000 < p' - p - 1 < 1000
                -1000 + p + 1 < p' < 1000 + p + 1
p' has to be positive (it's a prime number), so, in summary, we need to
find p and p' such that:
                2 < p < 997 (biggest prime lesser than 1000)
                2 < p' < 1001 + p
And then calculate a and b.
'''


from resources.useful_functions import is_prime


def consecutive_primes(a, b, bound=83):
    '''Finds the number of consecutive primes that produces the formula
    n^2 + an + b, starting with n = 0.
    '''
    for n in range(0, bound):
        val = n*n + a*n + b
        if val <= 0:
            return n
        elif not is_prime(val):
            return n
    # In case the bound is not enough
    return -1


def max_cons_primes(bound):
    '''Finds the pair (a, b) that produces the maximum number of primes
    in the formula n^2 + an + b, starting with n = 0, where
    |a| < bound and |b| <= bound.
    '''
    list_p = {i for i in range(2, bound) if is_prime(i)}
    list_p_prime = {i for i in range(2, 2*(bound + 1)) if is_prime(i)}
    d_primes = dict()
    for p in list_p:
        for p_prime in range(2, bound + p + 1):
            if p_prime in list_p_prime:
                a = p_prime - p - 1
                b = p
                d_primes[(a, b)] = consecutive_primes(a, b)
    return max(d_primes, key=d_primes.get)


if __name__ == '__main__':
    print(consecutive_primes(1, 41))  # 40
    print(consecutive_primes(-79, 1601, 100))  # 80
    print(max_cons_primes(1000))  # (-61, 971), 0.18s
