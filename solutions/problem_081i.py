'''https://projecteuler.net/problem=81'''
from pathlib import Path
import numpy as np


def load_matrix(path):
    '''Loads the matrix from the given path.'''
    file_path = Path(__file__).parent / path
    with open(file_path, 'r', encoding='utf-8') as file:
        matrix = np.array([
            [int(num) for num in line.strip().split(',')]
            for line in file if line.strip()
        ])
    return matrix


def find_min_path(m):
    '''For a given nxn matrix, find the minimum path sum from the top left to
    the bottom right by only moving to the right and down.'''
    n = m.shape[0]
    # Similar to problem 67
    flipped = np.fliplr(m)
    sum_diags = {}

    # All diagonals except for the central one
    for sign in (-1, 1):
        current = flipped.diagonal(sign*(n-1)).tolist()
        for d in range(n-2, 0, -1):
            big = flipped.diagonal(sign*d).tolist()
            for i, _ in enumerate(big):
                if i == 0:
                    big[i] += current[i]
                elif i == n-d-1:
                    big[i] += current[i-1]
                else:
                    big[i] += min(current[i-1:i+1])
            current = big[:]
        sum_diags[sign] = current[:]
    lower = sum_diags[-1]
    upper = sum_diags[1]

    # Central diagonal
    central = flipped.diagonal().tolist()
    for i, _ in enumerate(central):
        if i == 0:
            central[i] += upper[i] + lower[i]
        elif i == n-1:
            central[i] += upper[i-1] + lower[i-1]
        else:
            central[i] += min(upper[i-1:i+1]) + min(lower[i-1:i+1])

    return min(central)


def main():
    '''Main code of module.'''
    small_matrix = np.array((
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]
    ))
    print(find_min_path(small_matrix))  # 2427

    big_matrix = load_matrix("resources/0081_matrix.txt")  # 427337, 0.004s
    print(find_min_path(big_matrix))


if __name__ == '__main__':
    main()
