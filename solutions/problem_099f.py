'''https://projecteuler.net/problem=99'''
# Comparing two numbers written in index form like 2^11 and 3^7 is not
# difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

# However, confirming that 632382^518061 > 519432^525806 would be much more
# difficult, as both numbers contain over three million digits.

# Using base_exp.txt, a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the greatest
# numerical value.
from math import log10


def load_nums(path):
    '''Loads the numbers from the given path.'''
    with open(path, 'r', encoding='utf-8') as file:
        nums = file.read().split('\n')
        nums = [tuple(int(num) for num in pair.split(',')) for pair in nums]
    return nums


def find_biggest(path):
    '''Finds the index of the biggest number in the given path.'''
    nums = load_nums(path)

    # Init biggest and target row
    biggest, target = 0, -1
    for i, pair in enumerate(nums):
        a, b = pair
        # If a > 0, then a < b <-> log(a) < log(b)
        # Also, log(n^m) = m*log(n)
        len_num = b * log10(a)
        if len_num > biggest:
            biggest = len_num
            target = i + 1
    # Adjust for index
    return target


if __name__ == '__main__':
    print(find_biggest('resources/0099_base_exp.txt'))  # 709, 0.001s
