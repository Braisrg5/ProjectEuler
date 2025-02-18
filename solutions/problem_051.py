'''By replacing the 1^st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.


Para números de 2 dígitos, tenemos los patrones de reemplazo:

            *X o X*

Para números de 3 dígitos, tenemos los patrones de reemplazo:

        Reemplazando 1 son 3: *XX, X*X, XX*; o 3C1
        Reemplazando 2 son 3: **X, *X*, XX*; o 3C2

Para números de 4 dígitos, tenemos los patrones de reemplazo:

        Reemplazando 1 son 4: *XXX, X*XX, XX*X, XXX*; o 4C1
        Reemplazando 2 son 6: **XX, *X*X, *XX*, X**X, X*X*, XX**; o 4C2
        Reemplazando 3 son 4: ***X, **X*, *X**, X***; o 4C3

Generalizando para n dígitos, para reemplazar k dígitos calculamos nCk y como
k = 1, ..., n-1, podemos calcular la cantidad total de patrones de reemplazo:

    (sum(nCk) for k = 1, ..., n-1) = (sum(nCk) for k = 0, ..., n) - 2 = 2^n - 2

Teniendo en cuenta que para cada reemplazo, podemos cambiar X por cualquier
dígito del 0 al 9, y * por el mismo dígito, podemos ir una por una comprobando
'''
from itertools import combinations
from math import log10, floor


def bit_strings(digits, subs):
    '''https://stackoverflow.com/a/63100745
    Generates all combinations with  strings of length n'''
    # List of the indexes of the digits to be replaced
    index_combinations = combinations(range(digits), subs)
    for indices in index_combinations:
        yield ''.join('*' if i in indices else 'X' for i in range(digits))


def replacements(code, xs, digits):
    '''code is a string like 'X*X' or 'XX**X'
    xs is the number of X in the code
    digits is the length of the code
    Yields all possible replacements of 'X' with digits from 0 to 9 each
    and * with digits from 0 to 9
    '''
    limit, num = 10**digits - 1, 0
    set_nums = set()
    while num < limit:
        if num == 0:
            str_num = '0' * digits
        elif num < 10**(digits - 1):
            digs = floor(log10(num)) + 1
            str_num = '0' * (digits - digs) + str(num)
        else:
            str_num = str(num)
        print(str_num)

        i, new_code = 0, ''
        for el in code:
            if el == 'X':
                new_code += str_num[i]
                i += 1
            else:
                new_code += el
        code = new_code

        for i in range(10):
            set_nums.add(int(code.replace('*', str(i))))
        num += 1
    return set_nums


if __name__ == '__main__':
    print(replacements('X*X', 2, 3))
    pass
