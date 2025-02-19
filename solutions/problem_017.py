"""If the numbers 1 to 5 are written out in words: one, two, three,
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with british usage.
"""



def num_to_letters(n):
    """Writes a number n out in British English.
    This function is actually never called, but I used it during
    development to make sure that I was counting properly.
    """
    nums_ref = {
        '0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '10': 'ten', '11': 'eleven', '12': 'twelve', '14': 'fourteen',
        '18': 'eighteen'
    }
    prefixes = {
        '2': 'twen', '3': 'thir', '4': 'for', '5': 'fif', '6': 'six',
        '7': 'seven', '8': 'eigh', '9': 'nine'
    }
    str_n = str(n)
    if str_n in nums_ref:
        return nums_ref[str_n]
    elif 13 <= n <= 19:
        return prefixes[str_n[1]] + "teen"
    elif 20 <= n <= 99:
        return prefixes[str_n[0]] + "ty " + nums_ref[str_n[1]]
    elif n == 1000:
        return "one thousand"
    elif n % 100 == 0:
        return nums_ref[str_n[0]] + " hundred"
    else:
        return (nums_ref[str_n[0]] + " hundred " + "and "
                + num_to_letters(int(str_n[1:])))


def num_to_letter_count(n):
    """Counts the number of letters in a number n written in British
    English.
    """
    nums_ref = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3,
                '7': 5, '8': 5, '9': 4, '10': 3, '11': 6, '12': 6, '14': 8,
                '18': 8}
    prefixes = {'2': 4, '3': 4, '4': 3, '5': 3, '6': 3, '7': 5, '8': 4, '9': 4}
    str_n = str(n)
    if str_n in nums_ref:
        return nums_ref[str_n]
    elif 13 <= n <= 19:
        return prefixes[str_n[1]] + 4
    elif 20 <= n <= 99:
        return prefixes[str_n[0]] + 2 + nums_ref[str_n[1]]
    elif n == 1000:
        return 11
    elif n % 100 == 0:
        return nums_ref[str_n[0]] + 7
    else:
        return (nums_ref[str_n[0]] + 10 + num_to_letter_count(int(str_n[1:])))


def sum_letters(n):
    '''Returns the sum of the letters in every number from 1 to n.'''
    return sum([num_to_letter_count(i) for i in range(1, n + 1)])


if __name__ == "__main__":
    print(sum_letters(5))  # 19
    print(sum_letters(1000))  # 21124, 0.002s
