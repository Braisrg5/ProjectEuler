'''https://projecteuler.net/problem=50
The prime 41, can be written as the sum of six consecutive primes:

            41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

Los números primos necesariamente tienen que ser impares, así que si la suma
empieza por el número 2, sólo será prima si se suman una cantidad impar de
primos:

            2 + 3 = 5 (posible primo)
            2 + 3 + 5 = 10 (no puede ser primo)
            2 + 3 + 5 + 7 = 17 (posible primo)

En el caso de que empecemos por cualquier otro primo, la cantidad de elementos
tiene que ser también impar, por ejemplo:

            3 + 5 + 7 = 15 (posible primo)
            3 + 5 + 7 + 11 = 26 (no puede ser primo)

Reducimos así el número de veces que tenemos que comprobar si la suma es prima.
'''
from resources.useful_functions import sieve_Eratosthenes
global primes


def consecutive_prime_sum(N):
    '''Finds the prime which is the result of the longest sum of consecutive
    primes, up to N.
    '''
    primes = sieve_Eratosthenes(N)
    primes_set = set(primes)

    # Starting at 2+3
    max_length, max_prime = 2, 5
    (count, suma) = max_length, max_prime
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
    primes_set = set(primes)  # Convert to set for O(1) lookups
    num_primes = len(primes)

    max_length, max_prime = 0, 0
    # Precompute prefix sums
    prefix_sums = [0] * (num_primes)
    prefix_sums[0] = 2  # Starting sum is 2 (the first prime)
    for i in range(num_primes-1):
        suma = prefix_sums[i] + primes[i+1]
        prefix_sums[i + 1] = suma
        if suma in primes_set:
            max_length = i + 2
            max_prime = suma

    # For the rest of starting values, we can already add the max_length
    # to the end of the sequence
    for i in range(1, len(primes)):
        for j in range(i + max_length, len(primes)):
            suma = prefix_sums[j] - prefix_sums[i-1]
            if suma > N:
                break
            elif (j - i + 1) > max_length and suma in primes_set:
                max_length = j - i + 1
                max_prime = suma
    return max_prime


'''def consecutive_prime_sum_v3(N):
    '''Finds the longest sum of consecutive primes that adds to a prime below
    N. Uses prefix sums to optimize subsequence sum calculations. The
    optimization is more noticeable for bigger values of N.'''

    # Generate primes using the sieve
    primes = sieve_Eratosthenes(N)
    primes_set = set(primes)  # Convert to set for O(1) lookups
    num_primes = len(primes)

    max_length, max_prime = 0, 0
    # Precompute prefix sums
    prefix_sums = [0] * (num_primes)
    prefix_sums[0] = 2  # Starting sum is 2 (the first prime)
    for i in range(num_primes-1):
        suma = prefix_sums[i] + primes[i+1]
        prefix_sums[i + 1] = suma
        if i % 2 == 0 and suma in primes_set:
            max_length = i + 2
            max_prime = suma

    # For the rest of starting values, we can already add the max_length
    # to the end of the sequence
    for i in range(1, len(primes)):
        for j in range(i + max_length, len(primes)):
            length_k = j - i + 1
            if length_k % 2 != 0:
                suma = prefix_sums[j] - prefix_sums[i-1]
                if suma > N:
                    break
                elif length_k > max_length and suma in primes_set:
                    max_length = j - i + 1
                    max_prime = suma
    return max_prime'''


if __name__ == '__main__':
    print(consecutive_prime_sum_v2(100))  # 41
    print(consecutive_prime_sum_v2(1000))  # 953
    # print(consecutive_prime_sum(1000000))  # 997651, 0.145 seconds
    print(consecutive_prime_sum_v2(1000000))  # 997651, 0.138 seconds
