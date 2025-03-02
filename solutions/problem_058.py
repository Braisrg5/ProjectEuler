'''https://projecteuler.net/problem=58
'''
from resources.useful_functions import is_prime


def elements_diags(n):
    '''Finds the prime elements in the diagonals of a square matrix of size
    n x n constructed by the methods in (1*).
    '''
    k = 1  # Initialize first element
    # Number of prime and not prime elements in the diagonals (start with x=1)
    primes_in_diags, nums_in_diags = 0, 1

    # Initialize dimension and ratio
    dim, ratio = 1, float('inf')
    while ratio > 0.1:
        # Next loop
        dim += 2
        for j in range(4):
            k += dim - 1
            if j!= 4 and is_prime(k):
                primes_in_diags += 1
        nums_in_diags += 4
        ratio = primes_in_diags/nums_in_diags


if __name__ == '__main__':
    print(list(elements_diags(7)))


'''
#-------#
# Notes #
#-------#

(1*) Inherited from Problem 28
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
'''
