'''https://projecteuler.net/problem=15
Starting in the top left corner of a 2 x 2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
from math import factorial


def paths(n):
    '''Calculates the number of unique paths through a nxn grid.'''
    # Details can be found in (1*)
    n_fact = factorial(n)
    return factorial(2*n)//(n_fact*n_fact)


if __name__ == '__main__':
    print(paths(2))  # 6
    print(paths(20))  # 137846528820, 0.0s


'''
#-------#
# Notes #
#-------#

(1*)
In an n x n grid, all paths have size 2n (n right positions and n down
positions). We can identify every path by a string of 1s and 0s, where 0s are
rights and 1s are downs, for example:
In a 3x3 grid, every path is of length 6:
            000111, 010110, 011010, 111000

So, how many different string of size 2n, of n 0s and n 1s, are there? This is
a (simple?) combinatorics problem. The answer is:
            (2n)!/(n! * n!)
'''
