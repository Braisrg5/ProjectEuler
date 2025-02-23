'''https://projecteuler.net/problem=28
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:
                21 22 23 24 25
                20  7  8  9 10
                19  6  1  2 11
                18  5  4  3 12
                17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
'''


def sum_diags(n):
    '''Finds the sum of the diagonals of a square matrix of size n x n
    constructed by the method in (1*).
    Only works if n is odd. May implement it for n even in the future.
    '''
    # n can't be even
    if n % 2 == 0:
        return -1
    s, k = 1, 1
    for i in range(2, n+1, 2):
        for j in range(4):
            k += i
            s += k
    return s


def sum_diags_v2(n):
    '''Finds the sum of the diagonals of a square matrix of size
    n x n constructed by the methods in (1*), (2*).
    '''
    # Case where n is odd
    if n % 2 == 1:
        # Initialize sum and current number
        s, k = 1, 1
        # Max difference between numbers is n-1
        for i in range(2, n, 2):
            for j in range(4):
                # Next number and we add it to the sum
                k += i
                s += k

    # Case where n is even
    else:
        # Initialize sum and current number
        s, k = 0, 0
        # Max difference between numbers is n-1
        for i in range(1, n, 2):
            for j in range(4):  # Four values per square
                # Calculate next number present in the diagonal
                k += i
                # Add it to the sum
                s += k
    return s


if __name__ == '__main__':
    print(sum_diags_v2(4))
    print(sum_diags_v2(5))  # 101
    print(sum_diags_v2(1001))  # 669171001, 0.0004s


'''
#-------#
# Notes #
#-------#

(1*)
CASE n IS ODD
If we enumerate the numbers that we need to sum in increasing order, we have:
1, 3, 5, 7, 9, 13, 17, 21, 25.
By observing their properties, we can group them by the difference that there
is between them:
            Difference of 2: 1, 3, 5, 7, 9
            Difference of 4: 9, 13, 17, 21, 25
By creating a 7 x 7 spiral, we can confirm that the next numbers are:
            Difference of 6: 25, 31, 37, 43, 49
We need then to construct this list of numbers and then sum them:
                        01,
            03,  7,  5,  9, (Diff 2, 3x3)
            13, 17, 21, 25, (Diff 4, 5x5)
            31, 37, 43, 49, (Diff 6, 7x7)
            etc
And we stop when the number is n x n. Observe that when the square is n x n,
the last four numbers have a difference of n-1, so we can use that to stop.


(2*)
CASE n IS EVEN
Let's focus on the case where n is even:
The 2 x 2 matrix is:
            1 2
            4 3
The 6 x 6 matrix is:
            21 22 23 24 25 26
            20  7  8  9 10 27
            19  6  1  2 11 28
            18  5  4  3 12 29
            17 16 15 14 13 30
            36 35 34 33 32 31
If we enumerate the numbers that we need to sum in increasing order we have:
1, 2, 3, 4, 7, 10, 13, 16, 21, 26, 31, 36.
By observing their properties, we can group them by the difference that there
is between them:
            Difference of 1: 1, 2, 3, 4
            Difference of 3: 4, 7, 10, 13, 16
            Difference of 5: 16, 21, 26, 31, 36
By creating an 8 x 8 spiral, we can confirm that the next numbers are:
            Difference of 7: 36, 43, 50, 57, 64
We need then to construct this list of numbers and then sum them:
            01,  2,  3,  4, (Diff 1, 2x2)
            07, 10, 13, 16, (Diff 3, 4x4)
            21, 26, 31, 36, (Diff 5, 6x6)
            43, 50, 57, 64, (Diff 7, 8x8)
            etc
And we stop when the number is n x n. Observe that when the square is n x n,
the last four numbers have a difference of n-1, so we can use that to stop.
'''
