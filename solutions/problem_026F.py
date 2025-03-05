'''https://projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:
                1/2 = 0.5
                1/3 = 0.(3)
                1/4 = 0.25
                1/5 = 0.2
                1/6 = 0.1(6)
                1/7 = 0.(142857)
                1/8 = 0.125
                1/9 = 0.(1)
                1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
'''


def sieve_Eratosthenes25(N):
    '''Returns a list of numbers up to n that are not coprime to 10 (so, not
    divisible by 2 or 5).'''
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in [2, 5]:
        if sieve[i]:
            for j in range(i*i, N+1, i):
                sieve[j] = False
    return [i for i in range(2, N+1) if sieve[i]]


def recurring_cycle(d):
    '''Finds the length of the repitend of 1/d by making a list of the
    remainders of the division of 1 by d. When a remainder is repeated, the
    length of the repitend is the number of remainders between the current one
    and the repeated one (1*).'''
    remainders = [1]
    D = 10
    for i in range(d):
        # Find the remainder
        r = D % d
        # Exact division
        if r == 0:
            return 0
        # Every remainder is added if it is not repeated
        elif r not in remainders:
            remainders.append(r)
        # If the remainder is repeated, we've found the beginning and end of
        # the repitend, so we can find the length (from k to n-k)
        else:
            start = remainders.index(r)
            return len(remainders[start:])
        # Base 10 division
        D = r * 10
    # Something went very wrong if this is executed
    return -1


def longest_recurring_cycle_v2(bound):
    '''Finds the largest repitend of 1/d where d < bound.'''
    # It is not true that it is only necessary to check primes, see (1*)
    nums = sieve_Eratosthenes25(bound)
    d_cycle = dict()
    for d in nums:
        # We store the prime and the length of its repitend
        d_cycle[d] = recurring_cycle(d)
    # Return the prime for which the repitend is the longest
    return max(d_cycle, key=d_cycle.get)


if __name__ == '__main__':
    print(longest_recurring_cycle_v2(11))  # 7
    print(longest_recurring_cycle_v2(1000))  # 983, 0.12s


'''
#-------#
# Notes #
#-------#
(1*)
https://en.wikipedia.org/wiki/Repeating_decimal
At first, I believed that it was only necessary to check prime numbers, but
after doing some research I found out that is not the case. In particular, a
counterexample for this happens when we consider the bound to be 290.
If we consider only primes, we get 269, and if we consider every number, we get
289 = 17*17, which is the solution.
Despite this, we can reduce the amount of numbers checked if we remove every
number that is not coprime to 10, since they will have the repitend of one of
its divisors. The function sieve_Eratosthenes25 does this.


(2*)
A division D/d in base 10 works as follows:
    1.- We divide D by d and get the remainder r1.
    2.- We multiply r1 by 10 and repeat the process to get r2.
We can continue that process until one of two thinks happen:
    -We get a remainder of 0, which means that the division is exact.
    -We get a remainder rn that is equal to one of the previous remainders.
    Let's say rn = rk, then
        r(k+1) = r(n+1), r(k+2) = r(n+2)
    and eventually
        r(k + n - k) = r(n) = r(n + n - k) = r(2n - k),
    which would give us the same remainders all over again.
    So the sequence of remainders will be:
        {r1, r2, ..., rk, r(k+1), ..., r(n-1), rk, r(k+1)...},
    which would mean the repitend has length n - k.
'''
