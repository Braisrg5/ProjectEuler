'''https://projecteuler.net/problem=76'''
from tqdm import tqdm


def ways(n, k=''):
    '''Returns the ways of writing the number n as sums of integers that are
    less than k'''
    if k == '':
        k = n - 1
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k >= n:
        return ways(n, n-1) + 1
    total_ways = 0
    if n == 100:
        for i in tqdm(range(1, k+1)):
            total_ways += ways(n - i, i)
    else:
        for i in range(1, k+1):
            total_ways += ways(n - i, i)
    return total_ways


def ways_matrix(max_n, max_k=''):
    '''Returns a matrix of ways for writing n as sums of integers that are
    less than k'''
    if max_k == '':
        max_k = max_n - 1
    matrix = [[0] * (max_n+1) for _ in range(max_n+1)]
    matrix[1] = [0] + [1]*max_n
    for n in range(max_n+1):
        for k in range(max_n+1):
            if k == 0:
                matrix[n][k] = 0
            elif k == 1:
                matrix[n][k] = 1
            elif 2 <= k <= n-1:
                matrix[n][k] = matrix[n-k][k] + matrix[n][k-1]
            else:
                matrix[n][k] = matrix[n][n-1] + 1
    return matrix[max_n][max_k]


if __name__ == '__main__':
    print(ways_matrix(5))  # 6
    print(ways_matrix(100))  # 190569291, 0.011s
    print(ways_matrix(449))
