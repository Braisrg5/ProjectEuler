"""The following iterative sequence is defined for the set of
positive integers:
                n -> n/2 (n is even)
                n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following
sequence:
                13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one
million.
"""


def Collatz_sequence(n):
    """Calculates the length of the Collatz sequence for n."""
    length = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def longest_chain(bound):
    """Calculates the number that produces the longest chain with the
    Collatz function between those smaller than the bound.
    """
    num, longest = 1, 1
    for n in range(1, bound):
        length = Collatz_sequence(n)
        if length > longest:
            longest = length
            num = n
    return num


def longest_chain_v2(bound):
    nums_len = dict()
    largest, index = 1, 1
    for n in range(1, bound):
        length = 1
        n_it = n
        while n_it > 1:
            if n_it in nums_len:
                length += nums_len[n_it]
                break
            elif n_it % 2 == 0:
                n_it = n_it // 2
            else:
                n_it = (3 * n_it + 1) // 2
            length += 1
        nums_len[n] = length
        if length > largest:
            largest = length
            index = n
    return index, largest


def longest_chain_v3(bound):
    lengths = []
    largest, index = 1, 1
    for n in range(1, bound):
        length = 1
        n_it = n
        while n_it > 1:
            if n_it <= len(lengths):
                length += lengths[n_it - 1]
                break
            elif n_it % 2 == 0:
                n_it = n_it // 2
                length += 1
            else:
                n_it = (3 * n_it + 1) // 2
                length += 2
        lengths.append(length)
        if length > largest:
            largest = length
            index = n
    return index, largest


def longest_chain_v4(bound):
    lengths = [0] * bound
    lengths[1] = 1
    largest, index = 1, 1
    for n in range(2, bound):
        length = 0
        n_it = n
        while n_it >= n:
            if n_it & 1 == 0:
                n_it >>= 1  # Bitwise for n_it // 2
                length += 1
            else:
                n_it = (3 * n_it + 1) >> 1
                length += 2
        length += lengths[n_it]
        lengths[n] = length
        if length > largest:
            largest, index = length, n
    return index  # , largest


if __name__ == "__main__":
    print(Collatz_sequence(13))  # 10
    # print(longest_chain(1000000))  # 837799, 16.306s
    # print(longest_chain_v2(1000000))  # 837799, 1.75s
    # print(longest_chain_v3(1000000))  # 837799, 0.60s
    print(longest_chain_v4(1000000))  # 837799, 0.40s
