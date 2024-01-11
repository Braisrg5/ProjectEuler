"""In the 20 x 20 grid in the file, four numbers along a diagonal line
have been marked in red. The product of these numbers is
26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20 x 20 grid?
"""

import numpy as np
from functools import reduce


def load_grid():
    """Loads the 20x20 grid into a numpy array with proper format."""
    file = open("resources/11_grid.txt", "r")
    grid = np.array(
        [[int(j) for j in i.replace("\n", "").split(" ")]
         for i in file.readlines()]
    )
    file.close()
    return grid


def horizontal(grid, n):
    """Given a numpy grid, returns the biggest product of n adjacent
    numbers in the horizontal direction (i.e. from left to right).
    """
    (y, x) = np.shape(grid)
    totalProds = x - n + 1
    biggest = 0
    for i in range(y):
        for j in range(totalProds):
            adj = grid[i, j:n+j]
            prod = reduce(lambda x, y: x * y, adj)
            if prod > biggest:
                biggest = prod
    return biggest


def diagonals_matrix(grid):
    """Returns an array which consists of the diagonals of a given
    grid, starting at the bottom left and ending at the top right.
    """
    (y, x) = np.shape(grid)
    nx, ny = min(x, y), x + y - 1
    d_grid = np.zeros((ny, nx))
    for i in range(x + y - 1):
        diag_k = np.diag(grid, k=-y + 1 + i)
        if len(diag_k) < nx:
            diag_k = np.pad(diag_k, (0, nx - len(diag_k) % nx))
        d_grid[i,] = diag_k
    return d_grid


def big_prod(n):
    """Returns the greatest product of n adjacent numbers in every
    direction in the 20 x 20 grid.
    """
    grid = load_grid()
    h_big = horizontal(grid, n)
    # To find the vertical product, we transpose the matrix
    v_big = horizontal(grid.transpose(), n)
    # For the diagonals, we create a specific function
    diag_neg = horizontal(diagonals_matrix(grid), n)
    # For the other diagonals, we flip the matrix first
    diag_pos = horizontal(diagonals_matrix(np.fliplr(grid)), n)
    return max(h_big, v_big, diag_neg, diag_pos)


if __name__ == "__main__":
    print(big_prod(4))  # 70600674, 0.006s
