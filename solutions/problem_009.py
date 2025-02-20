"""A pythagorean triplet is a set of three natural numbers, a < b < c,
for which,
            a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which
a + b + c = 1000.

Find the product abc.


The crux of the problem resides in finding the numbers a, b and c.
With a bit of mathematical reasoning, we can simplify the problem:
            a^2 + b^2 = c^2  =>  c = sqrt(a^2 + b^2)
            a + b + c = 1000  =>  c = 1000 - a - b.
So,
            sqrt(a^2 + b^2) = 1000 - a - b
            a^2 + b^2 = (1000 - a - b)^2
and thus,
            a^2 + b^2 = a^2 + b^2 + 2*a*b + 10^6 - 2000*a - 2000*b
which reduces to:
            1000*(a + b) - a*b = 5*10^5
And we also observe that a and b must be less than 500.
"""


def check_op(a, b):
    """Checks the aforementioned operation for a and b."""
    return 1000 * (a + b) - a * b == 5 * 10**5


def find_triplet():
    """Finds the Pythagorean triplet for which a + b + c = 1000."""
    for i in range(1, 500):
        for j in range(1, 500):
            if check_op(i, j):
                return i, j, 1000 - i - j
    # This should never be reached
    return None


if __name__ == "__main__":
    a, b, c = find_triplet()  # (200, 375, 425)
    print(a * b * c)  # 31875000, 0.015s
