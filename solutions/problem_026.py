'''https://projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal
representation of the unit fractions with denominators 2 to 10 are
given:
                1/2 = 0.5
                1/3 = 0.(3)
                1/4 = 0.25
                1/5 = 0.2
                1/6 = 0.1(6)
                1/7 = 0.(142857)
                1/8 = 0.125
                1/9 = 0.(1)
                1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
'''


from resources.useful_functions import is_prime


def recurring_cycle(d):
    '''Finds the length of the repitend of 1/d'''
    remainders = [1]
    D = 10
    for i in range(d):
        r = D % d
        if r == 0:
            return 0
        elif r not in remainders:
            remainders.append(r)
        else:
            start = remainders.index(r)
            return len(remainders[start:])
        D = r * 10
    # Should not be executed
    return -1


def longest_recurring_cycle(bound):
    '''Finds the largest repitend of 1/d where d < bound.'''
    primes = {i for i in range(2, bound) if is_prime(i)}
    d_cycle = dict()
    for d in primes:
        d_cycle[d] = recurring_cycle(d)
    return max(d_cycle, key=d_cycle.get)


if __name__ == '__main__':
    print(longest_recurring_cycle(11))  # 7
    print(longest_recurring_cycle(1000))  # 983, 0.12s
