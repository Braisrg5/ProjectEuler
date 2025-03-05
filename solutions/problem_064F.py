'''https://projecteuler.net/problem=64
All square roots are periodic when written as continued fractions and can be
written in the form:
        sqrt(N) = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...)))

For example, let's consider sqrt(23):
        23 = 4 + sqrt(23) - 4 = 4 + 1/(1/(sqrt(23) - 4)) =
        = 4 + 1/(1 + (sqrt(23) - 3)/7)

If we continue we would get the following expansion:
        sqrt(23) = 4 + 1/(1 + 1/(3 + 1/(1 + 1/(8 + ...))))

The process can be summarized as follows:
        a0 = 4, 1/(sqrt(23) - 4) = (sqrt(23) - 4)/7 = 1 + (sqrt(23) - 3)/7
        a1 = 1, 7/(sqrt(23) - 3) = 7(sqrt(23) + 3)/14 = 3 + (sqrt(23) - 3)/2
        a2 = 3, 2/(sqrt(23) - 3) = 2(sqrt(23) + 3)/14 = 1 + (sqrt(23) - 4)/7
        a3 = 1, 7/(sqrt(23) - 4) = 7(sqrt(23) + 4)/14 = 8 + sqrt(23) - 4
        a4 = 8, 1/(sqrt(23) - 4) = (sqrt(23) + 4)/7 = 1 + (sqrt(23) - 3)/7
        a5 = 1, 7/(sqrt(23) - 3) = 7(sqrt(23) + 3)/14 = 3 + (sqrt(23) - 4)/2
        a6 = 3, 2/(sqrt(23) - 3) = 2(sqrt(23) + 3)/14 = 1 + (sqrt(23) - 4)/7
        a7 = 1, 7/(sqrt(23) - 4) = 7(sqrt(23) + 4)/14 = 8 + sqrt(23) - 4
It can be seen that the sequence is repeating. For conciseness, we use the
notation sqrt(24) = [4; (1, 3, 1, 8)], to indicate that the block (1, 3, 1, 8)
repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:
        sqrt(2) = [1; (2)], period=1
        sqrt(3) = [1; (1, 2)], period=2
        sqrt(5) = [2; (4)], period=1
        sqrt(6) = [2; (2, 4)], period=2
        sqrt(7) = [2; (1, 1, 1, 4)], period=3
        sqrt(8) = [2; (1, 4)], period=2
        sqrt(10) = [3; (6)], period=1
        sqrt(11) = [3; (3, 6)], period=2
        sqrt(12) = [3; (2, 6)], period=2
        sqrt(13) = [3; (1, 1, 1, 1, 6)], period=5
Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
'''
from math import sqrt


def period_for_root(n):
    '''Finds the period for the continued fraction of sqrt(n).
    This function is explained further in (1*).'''
    if sqrt(n).is_integer():
        return 0
    sqrt_n = sqrt(n)

    # Initialize the variables for the continued fraction
    a0 = int(sqrt_n)
    ak = a0
    base, ck = 1, ak

    k = 0
    while True:
        k += 1
        # Base for the kth fraction
        base = (n - ck**2)/base
        # kth element of the period
        ak = int((sqrt_n + ck)/base)
        # Stop condition
        # https://en.wikipedia.org/wiki/Periodic_continued_fraction#Reduced_surds # noqa
        if ak == 2*a0:
            return k
        # Value in the remaining fraction that is subtracted from sqrt(n)
        ck = ak*base - ck


def odd_periods_roots(bound):
    '''Finds how many continued fractions for the square root of N have an odd
    period when N <= bound.'''
    count = 0
    for n in range(2, bound + 1):
        period = period_for_root(n)
        # Sum if the period is odd
        count += (period % 2 == 1)
    return count


if __name__ == '__main__':
    print(odd_periods_roots(10000))  # 1322, 0.05s

'''
#-------#
# Notes #
#-------#

(1*)
Let's continue with the example for N = 23 and try to find a pattern:
a0 = 4, which is precisely the integer part of sqrt(23),
            a0 = int(sqrt(23)).
Let's denote c0 = a0 and base0 = 1.
We can see that:
        sqrt(23) = a0 + (sqrt(23) - c0)/base0.

For the next step, we need to invert the fraction, we will have:
        base0/(sqrt(23) - c0)

Doing rationalisation, we will have:
        base0*(sqrt(23) + c0)/(23 - c0**2) = (sqrt(23) + 4)/7

We can now set base1 = 7, and notice that we obtained it by doing the operation
        base1 = (23 - c0**2)/base0  (even if base1 is a fraction, this works)

Now, a1 is the integer part of (sqrt(23) + 4)/7, which is 1. Notice that:
        a1 = int((sqrt(23) + 4)/7) = int((sqrt(23) + c0)/base1)

The remaining fraction is going to be
        (sqrt(23) + c0)/base1 - a1 = (sqrt(23) + c0 - a1*base1)/base1 =
        = (sqrt(23) - (a1*base1 - c0))/base1

We can set c1 = a1*base1 - c0, and we will have that the remaining fraction is:
        (sqrt(23) + c1)/base1

For the next step, we would need to invert the fraction, and my hypothesis is
that this exact procedure repeats, and we can get 'ak' indefinitely. I also
think that we can do this for any N. I think that it is trivial, and I think
it is proven by construction.

As for when to stop, we can do it when ak = 2*a0:
https://en.wikipedia.org/wiki/Periodic_continued_fraction#Reduced_surds
'''
