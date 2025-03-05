'''https://projecteuler.net/problem=33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''
from fractions import Fraction
from functools import reduce


def check_fraction(str_n, str_d, s):
    '''Checks if a fraction has the property.'''
    # Cancel out the common digit in the numerator and denominator
    str_d_rp = str_d.replace(s, '', 1)
    str_n_rp = str_n.replace(s, '', 1)
    # Check if the replaced fraction is the same as the original fraction
    if int(str_n)/int(str_d) == int(str_n_rp)/int(str_d_rp):
        return True
    return False


def find_fractions():
    '''Finds the previously described fractions.'''
    for d in range(12, 99):
        # This are considered trivial, thus they are skipped
        if d % 10 == 0:
            continue
        for n in range(11, d):
            # This are considered trivial, thus they are skipped
            if n % 10 == 0:
                continue
            str_d, str_n = str(d), str(n)
            for s in str_n:
                # If both numerator and denominator contain the same digit,
                # and fulfill the condition, yield the fraction
                if s in str_d and check_fraction(str_n, str_d, s):
                    yield str_n + '/' + str_d


def denominator_product():
    '''Returns the denominator of the product of the fractions which can be
    simplified as explained in the statement.'''
    fractions = list(find_fractions())  # {'49/98', '19/95', '16/64', '26/65'}
    # Concert the solutions from str to Fraction
    fractions = [Fraction(f) for f in fractions]
    # Find out the product of the fractions
    prod = reduce(lambda x, y: x*y, fractions)
    # Return the denominator
    return prod.denominator


if __name__ == '__main__':
    print(check_fraction('49', '98', '9'))  # True
    print(denominator_product())  # 100, 0.002s
