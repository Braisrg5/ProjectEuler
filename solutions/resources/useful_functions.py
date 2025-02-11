from math import floor, sqrt, ceil, isqrt


def is_palindrome(n):
    """Checks if a number n is a palindrome"""
    return n == int(str(n)[::-1])


def is_prime(n):
    """Checks if n is a prime number by dividing it by 2 and 3 and then
    checking the numbers of the form 6*j + 1 and 6*j - 1, where j is an
    integer, and up to the square root of n. This are the only numbers
    of the form 6*j + k than can be prime, and thus we skip many
    numbers and reduce computation time.
    """
    end = isqrt(n)
    if n == 1:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # end+2 to ensure that 6*j+1 is included
    for j in range(6, end + 2, 6):
        if n % (j - 1) == 0 or n % (j + 1) == 0:
            return False
    return True


def prime_factors(n, list_fact=[]):
    """Constructs a list of the factors of a number n, from smallest to
    largest. Works in a similar manner to the previous function, but
    calls itself after adding each factor, and at the same time divides
    the number by them
    """
    end = isqrt(n)
    if n == 1:
        return list_fact
    elif n % 2 == 0:
        return prime_factors(n // 2, list_fact + [2])
    elif n % 3 == 0:
        return prime_factors(n // 3, list_fact + [3])
    for j in range(6, end + 2, 6):
        p1, p2 = j - 1, j + 1
        if n % p1 == 0:
            return prime_factors(n // p1, list_fact + [p1])
        elif n % p2 == 0:
            return prime_factors(n // p2, list_fact + [p2])
    return list_fact + [n]


def counts(ls):
    """Counts the number of times an element appears on a list."""
    counts = dict()
    for i in ls:
        counts[i] = counts.get(i, 0) + 1
    return counts


def digit_sum(n):
    """Sums the digits in base 10 of a number n."""
    return sum([int(i) for i in str(n)])


def find_divisors(n):
    """Finds the proper divisors of a number n."""
    if n == 1:
        return []
    divisors = [1]
    bound = ceil(sqrt(n)) + 1
    for d in range(2, bound):
        if n / d == d:
            divisors.append(d)
        elif n % d == 0:
            divisors.append(d)
            divisors.append(n // d)
    return divisors


def sum_divisors(n):
    """Sums the proper divisors of a number n."""
    divisors_set = {1}
    bound = isqrt(n) + 1
    for d in range(2, bound):
        if n % d == 0:
            divisors_set.update((d, n // d))
    return sum(divisors_set)


def sieve_Eratosthenes(n):
    """Basic implementation of the sieve of Eratosthenes."""
    nums = list(range(3, n + 1, 2))
    nums_dict = {num: True for num in nums}
    for num in nums_dict:
        if num * num > n:
            break
        if nums_dict[num]:
            for k in range(num, floor(n / num) + 1, 2):
                nums_dict[num * k] = False
    return [2] + [k for k, v in nums_dict.items() if v]


def digits_odd(n):
    """Returns True if all the digits of a number n are odd."""
    n = str(n)
    return sum([int(i) % 2 for i in n]) == len(n)
