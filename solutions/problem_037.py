'''https://projecteuler.net/problem=37
The number 3797 has an interesting property. Being prime itself, it
is possible to continuously remove digits from left to right, and
remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work
from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


from resources.useful_functions import is_prime, digits_odd, sieve_Eratosthenes
from math import floor, log10


def mod_digits_odd(n):
    '''Returns True if all the digits of a number n are odd or all are odd and
    the first digit is 2.'''
    n = str(n)
    all_odd = all(int(i) % 2 for i in n)
    first2_all_odd = all(int(i) % 2 for i in n[1:]) and n[0] == '2'
    return all_odd or first2_all_odd


def remove_digits(prime):
    '''Returns a list of the truncations from left to right and from
    right to left of a prime.'''
    prime = str(prime)
    n_digits = len(prime)
    left_to_right = [prime[:i+1] for i in range(n_digits-1)]
    right_to_left = [prime[i+1:] for i in range(n_digits-1)]
    digits_removed = set(left_to_right) | set(right_to_left)
    return [int(i) for i in digits_removed]


def check_truncatable(prime):
    '''Returns whether a prime is truncatable.'''
    n_digits = floor(log10(prime))
    reverse = int(str(prime)[::-1])
    for i in range(n_digits):
        prime = prime//10
        if not is_prime(prime):
            return False
        reverse = reverse//10
        unreverse = int(str(reverse)[::-1])
        if not is_prime(unreverse):
            return False
    return True


def sum_truncatable_primes(bound):
    '''Sums all the truncatable primes.
    Knowing the last truncatable prime is 739397, a bigger number can
    be the bound.'''
    trunc_primes = []
    for k in range(12, bound, 6):
        p1 = k-1
        p2 = k+1
        for p in [p1, p2]:
            if is_prime(p) and digits_odd(p):
                trunqued = remove_digits(p)
                if all(is_prime(p) for p in trunqued):
                    trunc_primes.append(p)
        if len(trunc_primes) == 11:
            return sum(trunc_primes)
    # Bound too small
    return -1


def sum_truncatable_primes_v2(bound):
    '''Sums all the truncatable primes.
    Knowing the last truncatable prime is 739397, a bigger number can
    be the bound.'''
    trunc_primes = [23]
    for k in range(12, bound, 6):
        p1 = k-1
        p2 = k+1
        for p in [p1, p2]:
            if is_prime(p) and digits_odd(p):
                if check_truncatable(p):
                    trunc_primes.append(p)
        if len(trunc_primes) == 11:
            return sum(trunc_primes)
    # Bound too small
    return -1


def check_truncatable_v2(p, primes_set):
    '''Returns whether a prime is truncatable.'''
    num_digits = int(log10(p))

    # Right to left
    p_check = p
    while p_check > 10:
        # Integer division by 10 returns the number without the last digit
        p_check //= 10
        # If any of the truncations fail, return False
        if p_check not in primes_set:
            return False

    # Left to right
    p_check = p
    while p_check > 10:
        # Modulo by powers of 10 gives the number without the first digit
        p_check %= 10**num_digits
        num_digits -= 1
        # If any of the truncations fail, return False
        if p_check not in primes_set:
            return False
    # If all truncations are prime, return True
    return True


def sum_truncatable_primes_v3(bound):
    '''Sums all the truncatable primes.'''
    primes = sieve_Eratosthenes(bound)
    primes_set = set(primes)
    # Exclude 2, 3, 5, 7
    primes = primes[4:]

    # Initialize the list of truncatable primes
    trunc_primes = []
    for p in primes:
        # If any of the digits is even (except if the first is 2), skip prime
        if mod_digits_odd(p) and check_truncatable_v2(p, primes_set):
            trunc_primes.append(p)
        # We've found all the truncatable primes
        if len(trunc_primes) == 11:
            return sum(trunc_primes)
    # Bound too small
    return -1


if __name__ == '__main__':
    print(check_truncatable(3797))  # True
    # print(sum_truncatable_primes(800000))  # 748317, 1.24s
    # print(sum_truncatable_primes_v2(800000))  # 748317, 0.63s
    print(sum_truncatable_primes_v3(800000))  # 748317, 0.09s
