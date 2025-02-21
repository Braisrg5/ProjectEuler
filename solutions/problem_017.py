'''https://projecteuler.net/problem=17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of 'and' when writing out numbers is in compliance with
British usage.
'''


def num_to_letters(n):
    '''Writes a number n out in British English.
    This function is actually never called, but I used it during development to
    make sure that I was counting properly.
    Only works for numbers up to 1000.
    '''
    # Dictionary for the letters of every number from 1 to 12
    # I later added fourteen because its prefix is different than forty
    nums_ref = {
        '0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '10': 'ten', '11': 'eleven', '12': 'twelve', '14': 'fourteen'
    }
    # Prefixes for the teens and multiples of 10
    prefixes = {
        '2': 'twen', '3': 'thir', '4': 'for', '5': 'fif', '6': 'six',
        '7': 'seven', '8': 'eigh', '9': 'nine'
    }
    str_n = str(n)
    # If the number is in the dictionary, return the corresponding word
    if str_n in nums_ref:
        return nums_ref[str_n]
    # If it's a teen, return the prefix followed by 'teen'
    elif 13 <= n <= 19:
        return prefixes[str_n[1]]+'teen'
    # If is between 20 and 99, return the prefix for the first digit followed
    # by 'ty' and the name of the second digit
    elif 20 <= n <= 99:
        return prefixes[str_n[0]]+'ty ' + nums_ref[str_n[1]]
    # If it's 1000, return 'one thousand'
    elif n == 1000:
        return 'one thousand'
    # If it's a multiple of 100, return the name of the first digit followed by
    # 'hundred'
    elif n % 100 == 0:
        return nums_ref[str_n[0]] + ' hundred'
    # If it's a number between 101 and 999, return the name of the first digit
    # followed by 'hundred and ' and call the function for the other 2 digits
    else:
        return (nums_ref[str_n[0]] + ' hundred and '
                + num_to_letters(int(str_n[1:])))


def num_to_letter_count(n):
    '''Counts the number of letters in a number n written in British English.
    '''
    nums_ref = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3,
                '7': 5, '8': 5, '9': 4, '10': 3, '11': 6, '12': 6, '14': 8
                }
    prefixes = {'2': 4, '3': 4, '4': 3, '5': 3, '6': 3, '7': 5, '8': 4, '9': 4}
    str_n = str(n)
    # If the number is in the dictionary, return the corresponding count
    if str_n in nums_ref:
        return nums_ref[str_n]
    # If it's a teen, return the prefix count plus 4 ('teen')
    elif 13 <= n <= 19:
        return prefixes[str_n[1]]+4
    # If it's between 20 and 99, return the prefix count for the first digit
    # plus 2 ('ty') plus the count for the second digit
    elif 20 <= n <= 99:
        return prefixes[str_n[0]]+2 + nums_ref[str_n[1]]
    # one thousand has 11 letters
    elif n == 1000:
        return 11
    # Multiples of 100 has the count for the first digit plus 7 ('hundred')
    elif n % 100 == 0:
        return nums_ref[str_n[0]] + 7
    # If it's a number between 101 and 999, return the count for the first
    # digit plus 10 ('hundred and') plus the count for the other 2 digits
    else:
        return (nums_ref[str_n[0]] + 10 + num_to_letter_count(int(str_n[1:])))


def sum_letters(n):
    '''Returns the sum of the letters in every number from 1 to n.'''
    return sum([num_to_letter_count(i) for i in range(1, n + 1)])


if __name__ == '__main__':
    print(sum_letters(5))  # 19
    print(sum_letters(1000))  # 21124, 0.002s
