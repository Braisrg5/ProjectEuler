'''https://projecteuler.net/problem=39'''
# If p is the perimeter of a right angle triangle with integral length sides,
# {a, b, c}, there are exactly three solutions for p = 120.

# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}.

# For which value of p <= 1000, is the number of solutions maximized?
from math import isqrt, gcd


def generate_primitive_pythagorean_triples(p):
    '''Generates all primitive pythagorean triples with perimeter less than or
    equal to p.
    We find the primitive pythagorean triples as explained in (1*).'''
    half_p = p//2
    # Limit for the range of m
    limit = isqrt(half_p)
    ppt = []
    for m in range(2, limit + 1):
        # Ensure that m > n
        for n in range(1, m):
            # Exceeded bound, we can skip to the next m
            if m*(m+n) > half_p:
                break
            # Exactly one of them is even and they are coprime
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                ppt.append(set((a, b, c)))
    return ppt


def generate_pythagorean_triples(bound):
    '''Generates all pythagorean triples with perimeter less than or equal to
    bound.'''
    # Generate all primitive pythagorean triples for the specified bound
    ppt = generate_primitive_pythagorean_triples(bound)
    pt = []
    for triple in ppt:
        # All primitive triples can be included
        pt.append(triple)
        a, b, c = triple
        k = 2
        perimeter = a + b + c
        # Add multiples of primitive triples with perimeter not more than bound
        while k*perimeter <= bound:
            pt.append(set((k*a, k*b, k*c)))
            k += 1
    return pt


def count_pyth_triples(bound):
    '''Counts how many pythagorean triples create a triangle for each perimeter
    1 to bound.'''
    # Generate all pythagorean triples for the specified bound
    pt = generate_pythagorean_triples(bound)
    # Dictionary of perimeters to the number of triples for that perimeter
    num_pt = {}
    for triple in pt:
        # Calculate perimeter for each triple
        p = sum(triple)
        if p not in num_pt:
            # Create a new entry for the perimeter if not found
            num_pt[p] = 1
        else:
            # Increment the count for the perimeter if already found
            num_pt[p] += 1
    return num_pt


def max_pyth_triples(num_pt):
    '''Finds the value p <= bound such that the number of pythagorean triples
    that sum p is maximized.'''
    return max(num_pt, key=num_pt.get)


if __name__ == '__main__':
    triples_under_1000 = count_pyth_triples(1000)
    print(triples_under_1000[120])  # 3
    print(max_pyth_triples(triples_under_1000))  # 840, 0.0004s


# ----- #
# Notes #
# ----- #

# (1*)
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# If m > n are positive integers, then:
#             a = m^2 - n^2
#             b = 2mn
#             c = m^2 + n^2
# forms a Pythagorean triple.

# There is a bijection between primitive Pythagorean triples and positive
# integers m and n such that m > n, m and n are coprime, and only one is even.

# Since a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m(m + n), we need to compute
# for 2m(m+n) <= bound <=> m(m+n) <= bound/2.

# If we take n = 0, then m^2 <= bound/2, so m <= sqrt(bound/2).
