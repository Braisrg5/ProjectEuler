'''https://projecteuler.net/problem=77'''
from resources.useful_functions import sieve_Eratosthenes


def prime_ways_matrix(target, max_n=''):
    '''Returns a matrix of ways for writing n as sums of integers that are
    less than k'''
    if max_n == '':
        max_n = target

    primes = sieve_Eratosthenes(max_n + 1)
    primes_set = set(primes)

    # Create empty matrix
    matrix = [[0] * (max_n+1) for _ in range(max_n+1)]

    # Rows for 0 and 1 are filled with zeros
    for n in range(2, max_n+1):
        for k in range(max_n+1):
            if k <= 1:
                matrix[n][k] = 0
            elif 2 <= k <= n-1:
                if k in primes_set:
                    matrix[n][k] = matrix[n-k][k]
                matrix[n][k] += matrix[n][k-1]
            else:
                max_row = matrix[n][n-1] + (n in primes_set)
                matrix[n][k] = max_row
        if matrix[n][n] > target:
            return (n, matrix[n][n] - (n in primes_set))
    # max_n not big enough
    return -1


def main():
    '''Main code of module.'''
    print(prime_ways_matrix(5000, 1000))  # 71 (5006 ways), 0.001s


if __name__ == '__main__':
    main()
