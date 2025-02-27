'''https://projecteuler.net/problem=53
There are exactly ten ways of selecting three from five, 12345:
            123, 124, 125, 134, 135, 145, 234, 235, 245, and 345.

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/[r!(n-r)!], where r <= n, n! = n*(n-1)*...*2*1 and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1 <= n <= 100 are greater
than one-million?
'''
from math import comb


def combinatorics_greater(N, bound):
    '''Finds the values of nCr for 1 <= n <= N that are greater than bound.'''
    # Total number of values
    total_count = 0
    for n in range(1, N+1):
        # Values for this particular n
        n_count = 0
        for r in range(n//2, -1, -1):
            if comb(n, r) <= bound:
                break
            n_count += 1
        n_count *= 2
        if n % 2 == 0:
            n_count -= 1
        total_count += max(n_count, 0)
    return total_count


def combinatorics_greater_v2(N, bound):
    '''Finds the values of nCr for 1 <= n <= N that are greater than bound.'''
    # Total count of values for all n
    total_count = 0
    for n in range(1, N+1):
        # Values for this particular n
        n_count = 0
        # We take the biggest value in nCr
        current = comb(n, n//2)
        # If the biggest value isn't bigger than bound, we can skip this n
        if current > bound:
            n_count += 1
            # Go backwards from biggest to smallest (1*)
            for r in range(n//2, 0, -1):
                # Relationship between nCr and nC(r-1) (2*)
                current = current*r//(n-r+1)
                # No more values bigger than bound
                if current <= bound:
                    break
                n_count += 1
            # Multiply by 2 because of symmetry
            n_count *= 2
            # Compensate for even numbers
            if n % 2 == 0:
                n_count -= 1
        total_count += n_count
    return total_count


if __name__ == '__main__':
    # print(combinatorics_greater(100, 1000000))  # 4075, 0.000
    # Much faster for bigger values
    print(combinatorics_greater_v2(100, 1000000))  # 4075, 0.000


'''
#-------#
# Notes #
#-------#

(1*)
https://math.stackexchange.com/a/723017
Let's prove that nC(r-1) <= nCr for r <= ceil(n/2):
            Check first case: r = 0
            nC0 = 1 <= nC1 = n

            nC(r-1) = n!/[(r-1)!(n-r+1)!] = n!/[r!(n-r)!] * r/(n-r+1) =
            = nCr * r/(n-r+1)
so nC(r-1) <= nCr iff r/(n-r+1) <= 1 but that is equivalent to:
            r <= n-r+1 <-> 2r <= n+1 <-> r <= (n+1)/2 <-> r <= ceil(n/2)

If we also consider that nCr = nC(n-r):
            nC(n-r) = n!/[(n-r)!(n-(n-r))!] = n!/[(n-r)!r!] = nCr
we can see that nCr has a maximum in r1 = floor(n/2) and r2 = ceil(n/2) (which
can be equal if n is even).

So, to solve the problem, we can start checking if values exceed one-million at
nC(r1) and go downwards. We will need to multiply by two the number of values
we find and adjust for even numbers (r1 == r2).


(2*)
We can even use the relationship we found before:
            nC(r-1) = nCr * r/(n-r+1)
'''
