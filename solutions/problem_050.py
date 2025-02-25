'''https://projecteuler.net/problem=50
The prime 41, can be written as the sum of six consecutive primes:

            41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
'''
from resources.useful_functions import sieve_Eratosthenes
global primes


def consecutive_prime_sum(N):
    '''Finds the prime which is the result of the longest sum of consecutive
    primes, up to N.'''
    primes = sieve_Eratosthenes(N)
    primes_set = set(primes)

    # Starting at 2+3
    max_length, max_prime = 2, 5
    (count, suma) = max_length, max_prime
    # Explained in (1*)
    for j in range(2, len(primes)-1, 2):
        suma += primes[j] + primes[j+1]
        if suma > N:
            break
        count += 2
        if count > max_length and suma in primes_set:
            max_length, max_prime = count, suma

    # Starting at anything else
    for i in range(1, len(primes)):
        (suma, count) = primes[i], 1
        # Explained in (1*)
        for j in range(i+1, len(primes)-1, 2):
            suma += primes[j] + primes[j+1]
            count += 2
            if suma > N:
                break
            if count > max_length and suma in primes_set:
                max_length, max_prime = count, suma
    return max_prime


def consecutive_prime_sum_v2(N):
    '''Finds the longest sum of consecutive primes that adds to a prime below
    N. Uses prefix sums to optimize subsequence sum calculations. The
    optimization is more noticeable for bigger values of N.'''

    # Generate primes using the sieve
    primes = sieve_Eratosthenes(N)
    # Convert to set for O(1) lookups
    primes_set = set(primes)
    num_primes = len(primes)

    max_length, max_prime = 0, 0
    # Precompute prefix sums (2*)
    prefix_sums = [0] * (num_primes)
    prefix_sums[0] = 2  # Starting sum is 2 (the first prime)
    for i in range(num_primes-1):
        suma = prefix_sums[i] + primes[i+1]
        prefix_sums[i + 1] = suma
        if suma in primes_set:
            max_length = i + 2
            max_prime = suma

    for i in range(1, len(primes)):
        # We can add the max_length to the index j because the difference
        # between the indexes has to be greater than the current max_length
        for j in range(i + max_length, len(primes)):
            # Current sum
            suma = prefix_sums[j] - prefix_sums[i-1]

            # If the suma exceeds the limit, next i
            if suma > N:
                break

            # If the number of elements is greater than the current max length
            # and the suma is a prime number
            elif (j - i + 1) > max_length and suma in primes_set:
                # New max length and new max prime
                max_length, max_prime = j - i + 1, suma
    # Return the prime number that can be written as the sum of the most
    # consecutive primes
    return max_prime


if __name__ == '__main__':
    print(consecutive_prime_sum_v2(100))  # 41
    print(consecutive_prime_sum_v2(1000))  # 953
    # print(consecutive_prime_sum(1000000))  # 997651, 0.145 seconds
    print(consecutive_prime_sum_v2(1000000))  # 997651, 0.138 seconds


'''
#-------#
# Notes #
#-------#

(1*)
Prime numbers must necessarily be odd, so if the sum starts with the number 2,
it will only be prime if an odd number of primes are added to 2:

            2 + 3 = 5 (possible prime)
            2 + 3 + 5 = 10 (even, cannot be prime)
            2 + 3 + 5 + 7 = 17 (possible prime)

If we start with any other prime, the number of elements must also be odd, for
example:

            3 + 5 + 7 = 15 (possible prime)
            3 + 5 + 7 + 11 = 26 (even, cannot be prime)

This reduces the number of times we need to check whether the sum is prime.


(2*)
The element of index n in the list prefix_sums is the sum of the first n+1
primes. This way, the sum of the primes from index i to j, i < j, is:
            prefix_sums[j] - prefix_sums[i-1] =
            = 2 + 3 + ... + pj - (2 + 3 + ... + p(i-1))	= pi + ... + pj
'''
