"""The Fibonacci sequence is defined by the recurrence relation:
                Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
                F1 = 1
                F2 = 1
                F3 = 2
                F4 = 3
                F5 = 5
                F6 = 8
                F7 = 13
                F8 = 21
                F9 = 34
                F10 = 55
                F11 = 89
                F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to
contain 1000 digits?
"""


from math import log10, ceil


def fibonacci_digits(d):
    """Finds the index of the first term in the Fibonacci sequence to
    contain d digits."""
    a0, a1 = 1, 1
    c = 2
    digs = ceil(log10(a1))
    while digs < d:
        a0, a1 = a1, a0 + a1
        digs = ceil(log10(a1))
        c += 1
    return c


if __name__ == "__main__":
    print(fibonacci_digits(3))  # 12
    print(fibonacci_digits(1000))  # 4782, 0.002s
