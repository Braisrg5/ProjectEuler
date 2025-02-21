'''https://projecteuler.net/problem=15
Starting in the top left corner of a 2 x 2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20x20 grid?


In an n x n grid, all paths have size 2 x n (right n positions and
down n positions). We can identify every path by a string of 1s and
0s, where 0s are rights and 1s are downs. For example: 0011, 0101,
1001, etc.
So, how many different string of size 2 x n, of n 0s and n 1s, are
there?
This is a (simple?) combinatorics problem. The answer is:
            (2n)!/(n! x n!)
'''


from math import factorial


def paths(n):
    n_fact = factorial(n)
    return factorial(2 * n) // (n_fact * n_fact)


if __name__ == '__main__':
    print(paths(2))  # 6
    print(paths(20))  # 137846528820, 0.0s
