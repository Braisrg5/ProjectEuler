'''https://projecteuler.net/problem=52'''
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


def have_same_digits(numbers):
    '''Checks if a list of numbers have the same digits.'''
    # First number (x, in this case)
    original = sorted(str(numbers[0]))
    for num in numbers[1:]:
        # For each other number, we check if it has different digits than x
        if sorted(str(num)) != original:
            return False
    # If all the tests fail, all have the same digits
    return True


def smallest_same_digits(multiple):
    '''Finds the smallest positive integer, x, such that x, 2x, ..., multiple*x
    contain the same digits.'''
    # First value for the digits
    d = 1
    while True:
        # Interval as calculated in (1*)
        digit_range = range(10**(d-1), (10**d - 1)//multiple + 1)
        for x in digit_range:
            # Calculate the sequence x, ..., multiple*x
            numbers = [x*i for i in range(1, multiple+1)]
            # If all numbers have the same digits, we've found our answer
            if have_same_digits(numbers):
                return x
        # Next value for the digits
        d += 1


if __name__ == '__main__':
    print(smallest_same_digits(6))  # 142857, 0.05s


# ----- #
# Notes #
# ----- #

# (1*)
# If x has one digit, then:
#             x ∈ [1, 9] -> 6x ∈ [6, 54]
# But 6x has to have one digit as well, so
#             6x ∈ [6, 9] -> x ∈ [1, 9/6]

# If x has two digits, then:
#             x ∈ [10, 99] -> 6x ∈ [60, 594] -> 6x ∈ [60, 99] -> x ∈ [10, 99/6]

# if x has three digits, then:
#             x ∈ [100, 999/6]

# If x has d digits, then:
#             x ∈ [10^(d-1), (10^d - 1)/6]

# To check optimally, for each number of digits, we check if 2x has the same
# digits, then 3x, then 4x, etc.
