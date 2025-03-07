'''https://projecteuler.net/problem=14'''
# The following iterative sequence is defined for the set of positive integers:
#                 n -> n/2 (n is even)
#                 n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following
# sequence:
#                 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
# It can seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is
# thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_sequence(n):
    '''Calculates the length of the Collatz sequence for n.'''
    length = 1
    # This just calculates the sequence until n becomes 1.
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def longest_chain_v4(bound):
    '''Finds the number less than bound which produces the longest collatz
    chain.'''
    # The lengths list is initialized with 0s and the length of 1 is set to 1.
    lengths = [0] * bound
    lengths[1] = 1

    # The largest chain length and the corresponding number are initialized.
    largest, index = 1, 1
    for n in range(2, bound):
        length, n_it = 0, n  # Parameters for the loop.
        # When n_it is smaller than n, the chain length is already stored.
        while n_it >= n:
            if n_it & 1 == 0:
                n_it >>= 1  # Bitwise for n_it // 2
                length += 1
            else:
                n_it = (3*n_it + 1) >> 1
                length += 2
        # We add to the current chain length the length of the stored chain.
        length += lengths[n_it]
        # And add it to the lengths list.
        lengths[n] = length

        # If the new length is larger than the current, it is updated.
        if length > largest:
            largest, index = length, n
    return index  # , largest


if __name__ == '__main__':
    print(collatz_sequence(13))  # 10
    print(longest_chain_v4(1000000))  # 837799, 0.40s
