'''https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides,
{a, b, c}, there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}.

For which value of p <= 1000, is the number of solutions maximized?


Si m > n son enteros positivos, entonces:

a = m^2 - n^2
b = 2mn
c = m^2 + n^2

es una terna pitagórica.

Existe una biyección entre las ternas pitagóricas primitivas y los enteros
positivos m y n tales que m > n, m y n son coprimos y sólo uno de ellos es par.

Como a + b + c = m^2 - n^2 + 2mn + m^2 + n^2 = 2m(m + n), entonces tenemos que
calcular para 2m(m+n) <= 1000 <=> m(m+n) <= 500.

Podemos tomar n = 0 y entonces m^2 <= 500 <=> m <= floor(sqrt(500))
'''
from math import floor, sqrt


def generate_primitive_pythagorean_triples(p):
    '''Generates all primitive pythagorean triples with perimeter less than or
    equal to p.
    '''
    limit = floor(sqrt(p/2))
    ppt = []
    for m in range(2, limit + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and m*(m + n) <= p/2:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                ppt.append(set((a, b, c)))
    return ppt


def generate_pythagorean_triples(bound):
    '''Generates all pythagorean triples with perimeter less than or equal
    to bound.
    '''
    ppt = generate_primitive_pythagorean_triples(bound)
    pt = []
    for triple in ppt:
        pt.append(triple)
        a, b, c = triple
        k = 2
        while True:
            if k*(a + b + c) > bound:
                break
            pt.append(set((k*a, k*b, k*c)))
            k += 1
    return pt


def count_pyth_triples(bound):
    '''Counts how many pythagorean triples create a triangle for each
    perimeter 1 to bound.
    '''
    pt = generate_pythagorean_triples(bound)
    num_pt = {}
    for triple in pt:
        p = sum(triple)
        if p in num_pt:
            num_pt[p] += 1
        else:
            num_pt[p] = 1
    return num_pt


if __name__ == '__main__':
    num_pt = count_pyth_triples(1000)
    print(num_pt[120])  # 3
    print(max(num_pt, key=num_pt.get))  # 840, 0.0004s
