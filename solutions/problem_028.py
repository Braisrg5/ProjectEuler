"""Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:
                21 22 23 24 25
                20  7  8  9 10
                19  6  1  2 11
                18  5  4  3 12
                17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?


If we enumerate the numbers that we need to sum in increasing order, we
have: 1, 3, 5, 7, 9, 13, 17, 21, 25.
By observing their properties, we can group them by the difference that
there is between them:
            Difference of 2: 1, 3, 5, 7, 9
            Difference of 4: 9, 13, 17, 21, 25
By creating a 7 x 7 spiral, we can confirm that the next numbers are:
            Difference of 6: 25, 31, 37, 43, 49
We need then to construct this list of numbers and then sum them:
                         1,
             3,  7,  5,  9,
            13, 17, 21, 25,
            31, 37, 43, 49, etc
And we stop when the number is n x n.

In the actual program, I implement two counters and calculate the
number of steps previously.
"""


def sum_diags(n):
    """Finds the sum of the diagonals of a square matrix of size
    n x n constructed by the previously described method.
    """
    s, k = 1, 1
    for i in range(2, n+1, 2):
        for j in range(4):
            k += i
            s += k
    return s


if __name__ == "__main__":
    print(sum_diags(5))  # 101
    print(sum_diags(1001))  # 669171001, 0.0004s
