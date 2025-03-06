'''https://projecteuler.net/problem=65
The square root of 2 can be written as an infinite continued fraction.
            sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))

The infinite continued fraction can be written, sqrt(2) =[1; (2)],
(2) indicates that 2 repeats ad infinitum. In a similar way,
sqrt(23) = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for sqrt(2).
            1 + 1/2 = 3/2
            1 + 1/(2 + 1/2) = 7/5
            1 + 1/(2 + 1/(2 + 1/2)) = 17/12
            1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

Hence, the sequence of the first ten convergents for sqrt(2) are:
            1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985,
            3363/2378, ...

What is most surprising is that the important mathematical constant,
            e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1,...,1,2k,1,...]

The first ten terms in the sequence of convergents for e are:
            2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465,
            1457/563,...

The sum of digits in the numerator of the 10th convergent is
1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
'''
from fractions import Fraction
from resources.useful_functions import digit_sum


def cont_fraction_e(N):
    '''Finds the N elements of the continued fraction of e as explained in the
    problem statement.'''
    # Initialize the variables for the continued fraction
    cont_fraction = [2]
    i, k = 1, 1
    # The pattern is 2; 1, 2*k, 1, 1, 2*(k+1),...
    while i < N:
        i += 1
        if i % 3 == 0:
            # Positions divisible by 3 are 2*k
            cont_fraction.append(2*k)
            k += 1
        else:
            cont_fraction.append(1)
    return cont_fraction


def recurring_convergents(terms):
    '''Finds the nth convergent of the continued fraction of a number,
    where terms are the elements of the continued fraction up to n.
    This function is explained in (1*).'''
    if len(terms) > 1:
        return terms[0] + Fraction(1, recurring_convergents(terms[1:]))
    else:
        return terms[0]


def convergent_e(N):
    '''Finds the sum of the digits in the numerator of the Nth convergent of
    the continued fraction of e.'''
    # Terms for the nth convergent
    terms = cont_fraction_e(N)

    # Find the nth convergent and its numerator
    convergent = recurring_convergents(terms)
    numerator = convergent.numerator
    return digit_sum(numerator)


if __name__ == '__main__':
    print(convergent_e(10))  # 17
    print(convergent_e(100))  # 272, 0.000s


'''
(1*)
To construct the nth convergent for a number given the terms of its continued
fraction, and if we consider the terms = [a0; a1, a2, a3, ...], we have:
            cn = a0 + 1/(a1 + 1/(a2 + 1/(a3 + 1/(a4 + 1/(a5 + ...)))))
and we keep repeat until we reach an.

We can do this recursively if we observe that we are doing:
            f(ak) = ak + 1/(f(a(k+1)))
until we reach an, where f(an) = an.
Then, f(a0) will precisely be the nth convergent.

Now that I think about it, this could be done in a loop from end to beginning
without the need for any recursive function. But this works, so I'm satisfied.
'''
