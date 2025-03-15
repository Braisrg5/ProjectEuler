'''https://projecteuler.net/problem=78'''
import numpy as np
from tqdm import tqdm


def ways_matrix(target, max_n=''):
    '''Returns a matrix of ways for writing n as sums of integers that are
    less than k'''
    if max_n == '':
        max_n = target - 1

    matrix = np.zeros((max_n+1, max_n+1), dtype=int)
    matrix[1, :] = [0] + [1]*max_n
    for n in tqdm(range(2, max_n+1)):
        for k in range(max_n+1):
            if k == 0:
                matrix[n, k] = 0
            elif k == 1:
                matrix[n, k] = 1
            elif 2 <= k <= n-1:
                matrix[n, k] = (matrix[n-k, k] + matrix[n, k-1]) % target
            else:
                ways_n = (matrix[n, n-1] + 1) % target
                matrix[n, k] = ways_n
        if ways_n == 0:
            return (n, matrix[n, n])
    # max_n not big enough
    return -1


if __name__ == '__main__':
    print(ways_matrix(100000, 100000))
