'''https://projecteuler.net/problem=9
A pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
            a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
'''


# We find the triplet using the logic in (1*)
def find_triplet(N):
    '''Finds the Pythagorean triplet for which a + b + c = N.'''
    half_n_squared = N**2//2
    for i in range(1, N//2):
        for j in range(1, N//2):
            if N*(i + j) - i*j == half_n_squared:
                return i, j, N - i - j
    # No Pythagorean triplet exists for N
    return -1


if __name__ == '__main__':
    a, b, c = find_triplet(1000)  # (200, 375, 425)
    print(a * b * c)  # 31875000, 0.015s


'''
#-------#
# Notes #
#-------#

(1*)
The crux of the problem resides in finding the numbers a, b and c.
With a bit of mathematical reasoning, we can simplify the problem:
            a^2 + b^2 = c^2  =>  c = sqrt(a^2 + b^2)
            a + b + c = N  =>  c = N - a - b.
So,
            sqrt(a^2 + b^2) = N - a - b
            a^2 + b^2 = (N - a - b)^2
and thus,
            a^2 + b^2 = a^2 + b^2 + N^2 + 2ab - 2N*a - 2N*b
which reduces to:
            N*(a + b) - a*b = N^2/2
If we make b = 0, we get:
            N*a = N^2/2 => a = N/2
So, a, b < N/2 (because of symmetry).
'''
