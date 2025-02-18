'''The arithmetic sequence, 1487, 4817, 8147, which each of the terms increases
by 3300, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''
from itertools import permutations
from resources.useful_functions import sieve_Eratosthenes
global primes


def possible_combinations():
    '''Returns a dictionary where the key is digits ordered and the value is
    all of the possible prime combinations.
    '''
    possible = {}
    for p in primes:
        # Sorted string and
        digitsp = tuple(sorted(str(p)))
        if digitsp not in possible.keys():
            # The set of all the possible permutations of the prime digits.
            possible_prime_permutations = set([
                int(''.join(perm)) for perm in list(permutations(digitsp))
                ])
            prime_permutations = sorted([
                n for n in possible_prime_permutations
                if n > 1000 and n in primes
                ])
            if len(prime_permutations) >= 3:
                possible[digitsp] = prime_permutations
    return possible


def find_sequence():
    possible = possible_combinations()
    # We remove the solution already given by the problem.
    del possible[('1', '4', '7', '8')]
    for primes in possible.values():
        diff_dict = {}
        num_values = len(primes)
        for i in range(num_values-1):
            for j in range(i+1, num_values):
                (pi, pj) = primes[i], primes[j]
                diff = pj - pi
                if diff not in diff_dict.keys():
                    diff_dict[diff] = (pi, pj)
                elif pi in diff_dict[diff] or pj in diff_dict[diff]:
                    return int(str(diff_dict[diff][0]) + str(pi) + str(pj))
    return -1


if __name__ == '__main__':
    primes = [p for p in sieve_Eratosthenes(10000) if p > 1000]
    print(find_sequence())  # 296962999629, 0.1s
