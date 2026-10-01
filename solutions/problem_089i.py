'''https://projecteuler.net/problem=89'''
# For a number written in Roman numerals to be considered valid there are basic
# rules which must be followed. Even though the rules allow some numbers to be
# expressed in more than one way there is always a "best" way of writing a
# particular number.

# For example, it would appear that there are at least six ways of writing the
# number sixteen:

#   IIIIIIIIIIIIIIII
#   VIIIIIIIIIII
#   VVIIIIII
#   XIIIIII
#   VVVI
#   XVI

# However, according to the rules only XIIIIII and XVI are valid, and the last
# example is considered to be the most efficient, as it uses the least number
# of numerals.

# The 11K text file, roman.txt, contains one thousand numbers written in valid,
# but not necessarily minimal, Roman numerals; see
# https://projecteuler.net/about=roman_numerals for the definitive rules for
# this problem.

# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.
from pathlib import Path
VALUES = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
CAN_SUBTRACT = {'I': ('V', 'X'), 'X': ('L', 'C'), 'C': ('D', 'M')}
GROUPS = {'hundreds': ('C', 'D', 'M'),
          'tens': ('X', 'L', 'C'),
          'units': ('I', 'V', 'X')}


def load_roman_numerals(path):
    '''Loads the roman numerals from the given path.'''
    file_path = Path(__file__).parent / path
    with open(file_path, 'r', encoding='utf-8') as file:
        nums = [str(line.strip()) for line in file if line.strip()]
    return nums


def decimal_to_roman(n):
    '''Passes a number from decimal to minimal roman numerals.'''
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100)//10
    units = n % 10
    zipped = zip(('hundreds', 'tens', 'units'), (hundreds, tens, units))
    # Thousands
    roman = '' + 'M'*thousands
    # Hundreds, tens and units work all the same
    for label, value in zipped:
        if value == 9:
            roman += GROUPS[label][0] + GROUPS[label][2]
        else:
            if value >= 5:
                roman += GROUPS[label][1]
                value -= 5
            if value <= 3:
                roman += GROUPS[label][0]*value
            elif value == 4:
                roman += GROUPS[label][0] + GROUPS[label][1]
    return roman


def roman_to_decimal(roman):
    '''Passes a number from valid roman numerals to decimal.'''
    num, i = 0, 0
    total_chars = len(roman)
    while i < total_chars - 1:
        char = roman[i]
        if char in ('M', 'D', 'L', 'V'):
            num += VALUES[char]
        elif char in ('C', 'X', 'I'):
            next_char = roman[i+1]
            if next_char in CAN_SUBTRACT[char]:
                num -= VALUES[char]
            else:
                num += VALUES[char]
        i += 1
    num += VALUES[roman[-1]]
    return num


def minimal_roman_numerals(bound=1000):
    '''Creates a dict of the minimal way to write each number up to bound in
    roman numerals.'''
    return {n: decimal_to_roman(n) for n in range(bound)}


def saved_characters(romans):
    '''Calculates how many characters can be saved in total if we write the
    roman numerals in romans in minimal form.'''
    minimal = minimal_roman_numerals(5000)
    saved = 0
    for roman in romans:
        decimal = roman_to_decimal(roman)
        saved += len(roman) - len(minimal[decimal])
    return saved


def main():
    '''Main code of module.'''
    romans = load_roman_numerals("resources/0089_roman.txt")
    print(saved_characters(romans))  # 743, 0.004s


if __name__ == '__main__':
    main()
