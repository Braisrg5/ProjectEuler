'''2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any reminder.

What is the smallest positive number that is evenly divisible by all
the numbers from 1 to 20?
'''


from resources.useful_functions import prime_factors, counts


def factors_to_number(factors):
    '''Translates a dictionary of prime factors and exponents to a
    number.
    '''
    n = 1
    for key, value in factors.items():
        n *= key**value
    return n


def lcm(numbers):
    '''Finds the least common multiple of a list of numbers, following
    the method of multiplying the prime factors to the highest
    exponent. A method using the Euclidean algorithm is in the back of
    my mind.
    '''
    factors_list = [counts(prime_factors(n)) for n in numbers]
    new_factors = dict()
    for factors in factors_list:
        for key, value in factors.items():
            if key in new_factors.keys():
                if value > new_factors[key]:
                    new_factors[key] = value
            else:
                new_factors[key] = value
    return factors_to_number(new_factors)


if __name__ == '__main__':
    ten_first = list(range(1, 11))
    print(lcm(ten_first))  # 2520
    twenty_first = list(range(1, 21))
    print(lcm(twenty_first))  # 232792560, 0.0s
