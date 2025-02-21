'''If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum35(n):
    '''Returns the sum of the numbers divisible by 3 and 5 less than n.'''
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


if __name__ == '__main__':
    print(sum35(10))  # 23
    print(sum35(1000))  # 233168, 0.0s
