'''https://projecteuler.net/problem=74'''
# The number 145 is well known for the property that the sum of the factorial
# of its digits is equal to 145:
#           1! + 4! + 5! = 1 + 24 + 120 = 145.

# Perhaps less well known is 169, in that it produces the longest chain of
# numbers that link back to 169; it turns out that there are only three such
# loops that exist:
#           169 -> 363601 -> 1454 -> 169
#           871 -> 45361 -> 871
#           872 -> 45362 -> 872
# It is not difficult to prove that EVERY starting number will eventually get
# stuck in a loop. For example,
#           69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
#           78 -> 45360 -> 871 -> 45361 (-> 871)
#           540 -> 145 (-> 145)

# Starting with 69 produces a chain of five non-repeating terms, but the
# longest non-repeating chain with a starting number below one million is sixty
# terms.

# How many chains, with a starting number below one million, contain exactly
# sixty non-repeating terms?
from math import factorial


def target_chain(bound, target):
    '''Finds how many numbers below bound produce a chain of len_chain by
    repeatedly adding the factorials of their digits.'''
    # List with values for fact[i], with i = 0...9
    factorials = [factorial(i) for i in range(0, 10)]
    # Add the length given by the statement and the numbers found on problem 34
    length_chain = {1: 1, 2: 1,
                    145: 1, 40585: 1,
                    169: 3, 363601: 3, 1454: 3,
                    871: 2, 872: 2, 45361: 2, 45362: 2}

    sum_digit_fact = {}
    for n in range(bound):
        s, num = 0, n
        while num:
            s += factorials[num % 10]
            num //= 10
        sum_digit_fact[n] = s

    # Initialize numbers for which the chain contain len_chain elements
    for n in range(1, bound):
        # Skip if already calculated
        if n in length_chain:
            continue
        current = n
        current_list = [current]
        count = 0
        while current not in length_chain:
            if current not in sum_digit_fact:
                s, num = 0, current
                while num not in sum_digit_fact:
                    s += factorials[num % 10]
                    num //= 10
                sum_digit_fact[current] = s + sum_digit_fact[num]
            current = sum_digit_fact[current]

            current_list.append(current)
            count += 1
        count += length_chain[current]
        for i, m in enumerate(current_list):
            length_chain[m] = count - i
    return sum(val == target for val in length_chain.values())


def main():
    '''Main code of module.'''
    print(target_chain(1000000, 60))  # 402, 1.01s


if __name__ == '__main__':
    main()
