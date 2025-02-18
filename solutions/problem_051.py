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
from resources.useful_functions import is_prime, sieve_Eratosthenes
from collections import Counter
from math import log10, floor
from time import perf_counter


def bit_strings(digits, subs):
    '''https://stackoverflow.com/a/63100745
    Generates all combinations with  strings of length n'''
    # List of the indexes of the digits to be replaced
    index_combinations = combinations(range(digits), subs)
    for indices in index_combinations:
        yield ''.join('*' if i in indices else 'X' for i in range(digits))


def replacements(code, xs):
    '''code is a string like 'X*X' or 'XX**X'
    xs is the number of X in the code
    digits is the length of the code
    Yields all possible replacements of 'X' with digits from 0 to 9 each
    and * with digits from 0 to 9
    '''
    limit, num = 10**xs - 1, 0
    if code[0] == 'X':
        num = 10**(xs - 1)
    if code[-1] == 'X':
        num += 1
    while num < limit:
        if num == 0:
            str_num = '0' * xs
        elif num < 10**(xs - 1):
            digs = floor(log10(num)) + 1
            str_num = '0' * (xs - digs) + str(num)
        else:
            str_num = str(num)

        i, new_code = 0, ''
        for el in code:
            if el == 'X':
                new_code = new_code + str_num[i]
                i += 1
            else:
                new_code = new_code + el
        yield new_code
        if code[-1] == 'X':
            num += 2


def find_prime(x, max_digs):
    '''Finds the smallest prime with x primes among the ten generated numbers
    '''
    # Digits of the number
    for d in range(2, max_digs+1):
        # Number of digits to be replaces
        for subs in range(1, d):
            # All possible codes for the current digits and replacements
            for code in bit_strings(d, subs):
                # If the last digit has to be replaced, we won't have more than
                # 5 possible primes (the odd numbers)
                if x <= 5 or code[-1] != '*':
                    # If the code begins with '*', we exclude 0
                    end = (1 if code[0] == '*' else 0)
                    for initial in replacements(code, d - subs):
                        count = 0
                        # We substitute from 9 to 0 (or 1) and count the primes
                        for i in range(9, end-1, -1):
                            num = int(initial.replace('*', str(i)))
                            if is_prime(num):
                                count += 1
                        # If we found x primes, return the number and the mask
                        if count == x:
                            return num, initial
    # Not enough digits
    return -1


def find_prime_v2(x, limit):
    primes = sieve_Eratosthenes(limit)[4:]
    primes_set = set(primes)
    for prime in primes:
        str_prime = str(prime)
        digits = len(str_prime)
        repeats = Counter(str_prime)
    return


if __name__ == '__main__':
    start = perf_counter()
    print(find_prime(5, 6))
    print(f'Execution time: {perf_counter() - start} seconds')
    start = perf_counter()
    print(find_prime_v2(5, 1000000))
    print(f'Execution time: {perf_counter() - start} seconds')
    start = perf_counter()
    print(sieve_Eratosthenes(1000000)[0])
    print(f'Execution time: {perf_counter() - start} seconds')
