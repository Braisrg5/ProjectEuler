from math import floor, sqrt, ceil, isqrt, prod


def is_pandigital(num):
    '''Checks if a number is 1 to 9 pandigital.'''
    return set(num) == set('123456789')


def is_palindrome(n):
    '''Checks if a number n is a palindrome'''
    reversed_n = int(str(n)[::-1])
    return n == reversed_n


def is_prime(n):
    '''Checks if n is a prime number'''
    # Edge cases: 1 is not prime
    if n == 1:
        return False
    # 2 and 3 are prime numbers
    elif n in (2, 3):
        return True
    # Check divisibility by 2 and 3
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # Only necessary to check until the integer square root of n (1*)
    end = isqrt(n)
    # It's enough to check the numbers of the form 6*j + 1 and 6*j - 1,
    # because in mod 6 every other number is not prime (2*)
    # end+2 to ensure that 6*j+1 is included in edge cases
    for j in range(6, end + 2, 6):
        if n % (j - 1) == 0 or n % (j + 1) == 0:
            return False
    # If every test fails, n is a prime number
    return True


def prime_factors(n, list_fact=[]):
    '''Constructs an ordered list of the prime factors of a number n
    The factors are generated recursively, starting with an empty list. Once a
    factor is found, it is appended to the list, the number is divided by it
    and the function rerun '''
    # Check until the integer square root of n (1*)
    end = isqrt(n)
    # If n is equal to 1, there are no prime factors
    if n == 1:
        return list_fact
    # If n is even or divisible by 3, the function is called again
    elif n % 2 == 0:
        return prime_factors(n // 2, list_fact + [2])
    elif n % 3 == 0:
        return prime_factors(n // 3, list_fact + [3])
    # Same as is_prime, it's enough to check the numbers of the form 6*j + 1
    # and 6*j - 1 (2*)
    # end+2 to ensure that 6*j+1 is included in edge cases
    for j in range(6, end + 2, 6):
        p1, p2 = j - 1, j + 1
        if n % p1 == 0:
            return prime_factors(n // p1, list_fact + [p1])
        elif n % p2 == 0:
            return prime_factors(n // p2, list_fact + [p2])
    # No more factors found, n is a prime number and the list is returned
    return list_fact + [n]


# Same as collections.Counter? Yes
def counts(ls):
    '''Counts the number of times an element appears on a list.'''
    counts = dict()
    for i in ls:
        counts[i] = counts.get(i, 0) + 1
    return counts


def digit_sum(n):
    '''Sums the digits in base 10 of a number n.'''
    return sum(int(i) for i in str(n))


# Could be optimized, similarly to prime_factors
def find_divisors(n):
    '''Finds the proper divisors of a number n.'''
    if n == 1:
        return []
    divisors = [1]
    # Divisors are always in pair, see (1*)
    # Bound has to be ceil(sqrt(n))
    bound = ceil(sqrt(n))
    for d in range(2, bound + 1):
        # If n / d == d, d is the square root of n
        if n / d == d:
            divisors.append(d)
        elif n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
    return divisors


# Very similar to find_divisors, but we calculate the sum
def sum_divisors(n):
    '''Sums the proper divisors of a number n.'''
    if n <= 1:
        return 0
    total = 1
    bound = isqrt(n)
    for d in range(2, bound + 1):
        if n % d == 0:
            total += d
            pair = n // d
            if d != pair:
                total += pair
    return total


def sieve_Eratosthenes_old(N):
    '''Basic implementation of the sieve of Eratosthenes.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'''
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, floor(sqrt(N))+1):
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
    return [i for i in range(2, N+1) if sieve[i]]


def sieve_Eratosthenes(N):
    '''Basic implementation of the sieve of Eratosthenes.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'''
    sieve = bytearray([True]) * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, isqrt(N)+1):
        if sieve[i]:
            sieve[i*i:N+1:i] = bytearray([False]) * ((N - i*i)//i + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def sieve_Pritchards_wheel(N):
    """Sieve of Eratosthenes optimized with a (2,3,5) wheel."""
    while True:
        primes = [2, 3]
        primes_prod = prod(primes)

        sieve = bytearray([True]) * (primes_prod+1)
        for p in primes:
            sieve[p:primes_prod+1:p] = bytearray([False])*((primes_prod - p)//p + 1)
        print(list(sieve))
        a = input()


def digits_odd(n):
    '''Returns True if all the digits of a number n are odd.'''
    n = str(n)
    return sum(int(i) % 2 for i in n) == len(n)


def is_triangle(t):
    '''Determines if a number is a triangle number.'''
    # Formulas are derived in (3*)
    return sqrt(8*t + 1).is_integer()


def is_pentagonal_old(P):
    '''Checks if a number is pentagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 24*P))/6
    return n.is_integer()


# Slightly faster
def is_pentagonal(P):
    '''Checks if a number is pentagonal.'''
    # Formulas are derived in (3**)
    return sqrt(1 + 24*P) % 6 == 5


def is_hexagonal_old(H):
    '''Checks if a number is hexagonal.'''
    # Formulas are derived in (3*)
    n = (1 + sqrt(1 + 8*H))/4
    return n.is_integer()


def is_hexagonal(H):
    '''Checks if a number is hexagonal.'''
    # Formulas are derived in (3**)
    return sqrt(1 + 8*H) % 4 == 3


'''
#-------#
# Notes #
#-------#

(1*)
For any n, its divisors are always in pairs: if d is a divisor of n,
then so is D = n//d.

If d != D, one of them has to be greater than the square root of n.
If both are, then d*D > sqrt(n)^2 = n
If neither is, then d*D < sqrt(n)^2 = n

So, by checking every possible divisor up to sqrt(n) (or isqrt(n)), we will
necessarily find all of them (or none of them, if the number is prime)


(2*)
For mod 6, the numbers can be organized as follows:

mod 6:  2   3   4   5   0   -1

        2   3   4   5   6   7
        8   9   10  11  12  13
        14  15  16  17  18  19
        20  21...

In the columns 2 and 4, the numbers are always even
In the column 3, the numbers are always divisible by 3
In the column 6, the numbers are divisible by 6

That leaves us with the numbers in the columns 5 and -1, which can be
calculated as 6*j + 1 and 6*j - 1, where j is an integer.


(3*)
For triangle numbers, the formula is:
T(n) = n*(n+1)/2 => n^2 + n - 2T = 0 => n = [-1 +- sqrt(1 + 8T)]/2
n has to be greater than 0 so we only take the positive root.
In order for T to be a triangular number, sqrt(1 + 8*2T) must be an integer.
This is enough because 1+8*2T is odd, and sqrt(odd) = odd (in case it exists)

For pentagonal numbers, the formula is:
P(n) = n*(3n - 1)/2 => 3n^2 - n - 2P = 0 => n = [1 + sqrt(1 + 24*P)]/6
We aren't as lucky as before (sqrt(1 + 24*2) = 7 but 8 is not divisible by 6)
so we need to check if the whole expression for n is an integer. (3**)

For hexagonal numbers, the formula is:
H(n) = 2n^2 + n => 2n^2 + n - H = 0 => n = [1 + sqrt(1 + 8*H)]/4
We also need to check if the whole expression for n is an integer. (3**)


(3**)
For pentagonal numbers, if we take sqrt(1 + 24*P) mod 6, we get sqrt(1). Now,
what numbers mod 6 are the square root of 1?

    0*0 = 0; 1*1 = 1; 2*2 = 4; 3*3 = 3; 4*4 = 4; 5*5 = 1

So, sqrt(1) mod 6 = 1 or 5, and in our particular case we are interested when
it is equal to 5, because then (1 + 5)/6 would be an integer.

For hexagonal numbers, if we take sqrt(1 + 8*H) mod 4, we also get sqrt(1).
What numbers mod 4 are the square root of 1?

    0*0 = 0; 1*1 = 1; 2*2 = 0; 3*3 = 1
So, sqrt(1) mod 4 = 1 or 3, and in our particular case we are interested in 3
'''
