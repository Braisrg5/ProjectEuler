'''https://projecteuler.net/problem=97'''


def calc_massive_prime():
    '''Calculates the last 10 digits of the massive prime number.'''
    # The last 10 digits of a number is equal to the number modulo 10**10
    return (28433 * pow(2, 7830457, 10**10) + 1) % 10**10


def main():
    '''Main code of module.'''
    print(calc_massive_prime())  # 8739992577, 0.001s


if __name__ == '__main__':
    main()
