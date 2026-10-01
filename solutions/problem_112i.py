'''https://projecteuler.net/problem=112'''
# Working from left-to-right if no digit is exceeded by the digit to its
# left it is called an increasing number; for example, 134468.

# Similarly if no digit is exceeded by the digit to its right it is called a
# decreasing number; for example, 66420.

# We shall call a positive integer that is neither increasing nor decreasing
# a "bouncy" number; for example, 155349.

# Clearly there cannot be any bouncy numbers below one-hundred, but just
# over half of the numbers below one-thousand (525) are bouncy. In fact, the
# least number for which the proportion of bouncy numbers first reaches 50%
# is 538.

# Surprisingly, bouncy numbers become more and more common and by the time
# we reach 21780 the proportion of bouncy numbers is equal to 90%.

# Find the least number for which the proportion of bouncy numbers is
# exactly 99%.


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
    print(percentage_bouncy(0.5))  # 538
    print(percentage_bouncy(0.9))  # 21780
    print(percentage_bouncy(0.99))  # 1587000, 0.88s


if __name__ == '__main__':
    main()
