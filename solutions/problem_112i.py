'''https://projecteuler.net/problem=112'''


def is_bouncy(n):
    '''Checks if a number is bouncy.'''
    increasing = False
    decreasing = False

    last_digit = n % 10
    n //= 10

    while n > 0:
        current_digit = n % 10
        if current_digit < last_digit:
            increasing = True
        elif current_digit > last_digit:
            decreasing = True
        if increasing and decreasing:
            return True
        last_digit = current_digit
        n //= 10
    return False


def percentage_bouncy(perc):
    '''Finds the first number for which the percentage of bouncy numbers is
    exactly the one given.'''
    bouncy, total = 0, 1
    while bouncy/total != perc:
        total += 1
        if is_bouncy(total):
            bouncy += 1
    return total


def main():
    '''Main code of module.'''
    print(percentage_bouncy(0.99))  # 1587000, 0.88s


if __name__ == '__main__':
    main()
