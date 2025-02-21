'''https://projecteuler.net/problem=11
In the 20 x 20 grid in the file, four numbers along a diagonal line have
been marked in red. The product of these numbers is

            26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20 x 20 grid in 11_grid.txt?
'''
import numpy as np
from functools import reduce


def load_grid(path):
    '''Loads the 20x20 grid from path into a numpy array with proper format.'''
    with open(path, 'r') as file:
        grid = np.array([
            [int(j) for j in i.replace('\n', '').split(' ')]
            for i in file.readlines()
        ])
    return grid


def horizontal(grid, n):
    '''Given a numpy grid, returns the biggest product of n adjacent numbers
    in the horizontal direction (from left to right).'''
    (y, x) = np.shape(grid)
    # Total products for a single row
    totalProds = x - n + 1
    biggest = 0
    for i in range(y):
        # For every ro
        for j in range(totalProds):
            adj = grid[i, j:n+j]
            prod = reduce(lambda x, y: x * y, adj)
            if prod > biggest:
                biggest = prod
    return biggest


def diagonals_matrix(grid):
    '''Returns an array which consists of the diagonals of a given grid,
    starting at the bottom left and ending at the top right.'''
    (y, x) = np.shape(grid)
    # Max length and number of diagonals
    nx, ny = min(x, y), x + y - 1

    # Matrix of the diagonals in the original grid
    d_grid = np.zeros((ny, nx))

    # For each line in the new matrix
    for i in range(x + y - 1):
        # We take the diagonal
        diag_k = np.diag(grid, k=-y + 1 + i)
        # If it is shorter than nx, we add padding zeros to the end
        if len(diag_k) < nx:
            diag_k = np.pad(diag_k, (0, nx - len(diag_k) % nx))
        # We store the diagonal in the matrix
        d_grid[i,] = diag_k

    return d_grid


def big_prod(n):
    '''Returns the greatest product of n adjacent numbers in every direction
    in the 20 x 20 grid. (1*)
    '''
    grid = load_grid('resources/11_grid.txt')
    # Calculate the biggest horizontal product
    h_big = horizontal(grid, n)

    # To find the vertical product, we transpose the matrix
    v_big = horizontal(grid.transpose(), n)

    # The diagonals_matrix function finds a matrix where each row is a diagonal
    diag_neg = horizontal(diagonals_matrix(grid), n)

    # For the other diagonal, we flip the matrix first
    diag_pos = horizontal(diagonals_matrix(np.fliplr(grid)), n)
    return max(h_big, v_big, diag_neg, diag_pos)


if __name__ == '__main__':
    print(big_prod(4))  # 70600674, 0.006s


'''
#-------#
# Notes #
#-------#

(1*)
In order to consider every possible product of adjacent numbers, we need to
consider every possible direction to calculate them, and those would be:
horizontal, vertical, and both diagonals (top left to bottom right and top
right to bottom left).

Let's focus on the horizontal direction first. We will have a matrix of size
(y, x), where y is the number of rows and x is the number of columns.
For every row we need to calculate all possible products of n adjacent numbers,
so for row i, we will have (x - n + 1) products (similar to problem_008). So,
we calculate all products and find the maximum.

For the vertical direction, we can transpose the matrix and apply the previous
procedure.

For the diagonals, I first focus on the bottom left to top right one:
I create a new matrix where each row is a diagonal of the original (completed
by zeros if necessary). The matrix will have size (ny, nx), where ny is the
number of diagonals and nx is the maximum length they can have.
To create the matrix, I use the np.diag function with parameter k, going from
bottom left (k=-y + 1) to top right (k=x - 1). If any diagonal is shorter than
nx, it is completed by zeros.
After creating the matrix, we apply the previous procedure.

For the other diagonal, we can just flip the matrix first (np.fliplr) and
create the matrix as before.
'''
