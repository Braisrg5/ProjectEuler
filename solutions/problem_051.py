'''https://projecteuler.net/problem=51
By replacing the 1^st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight prime
value family.
'''
from math import log10, floor
from itertools import combinations
from collections import Counter
from resources.useful_functions import is_prime, sieve_Eratosthenes
global primes, primes_set


def bit_strings(digits, subs):
    '''https://stackoverflow.com/a/63100745
    Generates all combinations with  strings of length n'''
    # List of the indexes of the digits to be replaced
    index_combinations = combinations(range(digits), subs)
    for indices in index_combinations:
        yield ''.join('*' if i in indices else 'X' for i in range(digits))


def replacements(code, xs):
    '''code is a string like 'X*X' or 'XX**X'
    xs is the number of X in the code
    digits is the length of the code
    Yields all possible replacements of 'X' with digits from 0 to 9 each
    and * with digits from 0 to 9
    '''
    if xs == 0:
        yield code
    limit, num = 10**xs - 1, 0
    if code[0] == 'X':
        num = 10**(xs - 1)
    if code[-1] == 'X':
        num += 1
    while num < limit:
        if num == 0:
            str_num = '0' * xs
        elif num < 10**(xs - 1):
            digs = floor(log10(num)) + 1
            str_num = '0' * (xs - digs) + str(num)
        else:
            str_num = str(num)

        i, new_code = 0, ''
        for el in code:
            if el == 'X':
                new_code = new_code + str_num[i]
                i += 1
            else:
                new_code = new_code + el
        yield new_code
        if code[-1] == 'X':
            num += 2
        else:
            num += 1


# This one is very flawed. It takes too long and isn't well programmed to
# always find the smallest solution.
def find_prime(x, max_digs):
    '''Finds the smallest prime which, by replacing part of the number
    with the same digit, is part of an x prime value family
    '''
    # Digits of the number
    for d in range(2, max_digs+1):
        # Number of digits to be replaced
        for subs in range(1, d):
            # All possible codes for the current digits and replacements
            for code in bit_strings(d, subs):
                # If the last digit has to be replaced, we won't have more than
                # 5 possible primes (the odd numbers)
                if x <= 5 or code[-1] != '*':
                    # If the code begins with '*', we exclude 0
                    end = (1 if code[0] == '*' else 0)
                    for initial in replacements(code, d - subs):
                        count = 0
                        # We substitute from 9 to 0 (or 1) and count the primes
                        for i in range(9, end-1, -1):
                            num = int(initial.replace('*', str(i)))
                            if is_prime(num):
                                count += 1
                        # If we find x primes, return the number and the mask
                        if count == x and initial != '*89':
                            return num, initial
    # Not enough digits to find the answer
    return -1


def create_masks(str_prime):
    set_prime = set(str_prime)
    for digit in set_prime:
        mask = ''
        for dig in str_prime:
            if dig == digit:
                mask += '*'
            else:
                mask += 'X'
        yield mask


def apply_mask_to_number(mask, num):
    '''mask is a string like 'X*X' or 'XX**X' with the same length as num
    num is a number converted to string
    returns the number of primes which result from substituting the index
    with '*' by the same digit in num
    '''
    # If the first digit has to be replaced, we exclude 0 or either we would
    # get results like 2011 turning into 0011, which would be wrong
    start = (1 if mask[0] == '*' else 0)

    count = 0
    for d in range(start, 10):
        for i in range(len(mask)):
            if mask[i] == '*':
                num = num[:i] + str(d) + num[i+1:]
        if int(num) in primes_set:
            count += 1
    return count


# We may be excluding masks, for example, in the prime 56003 we're only
# considering the mask 56**3 and NOT the masks 560*3 and 56*03. The problem
# statement isn't clear, but this approach gives the correct answer
# An edge case could be to consider x = 5: find_prime gives 11 as an answer
# and the mask *1 (11, 31, 41, 61, 71) find_prime_v2 gives 17 as an answer and
# the mask *7 (17, 37, 47, 67, 97) The solution by find_prime seems to be more
# correct, I may improve it in the future.
def find_prime_v2(x):
    '''Finds the smallest prime which, by replacing part of the number
    with the same digit, is part of an x prime value family
    '''
    for prime in primes:
        str_prime = str(prime)
        # We find all the masks that are possible for the current prime.
        masks = create_masks(str_prime)
        for mask in masks:
            if x <= 5 or mask[-1] != '*':
                count = apply_mask_to_number(mask, str_prime)
                if count == x:
                    return prime, mask
    # The limit for the prime generation is too small
    return -1


def create_masks_v2(str_prime):
    '''Creates all possible masks for a given prime number.'''
    digits = len(str_prime)
    # Masks if we replace just one digit:
    masks1 = bit_strings(digits, 1)
    for mask in masks1:
        yield mask

    count_digits = Counter(str_prime)
    # Masks if we replace more than one digit:
    if len(count_digits) > 1:
        for digit, count in count_digits.items():
            if count <= 1:
                continue
            for i in range(1, count+1):
                for temp_mask in bit_strings(count, i):
                    mask, temp_index = '', 0
                    for dig in str_prime:
                        if dig == digit:
                            mask += temp_mask[temp_index]
                            temp_index += 1
                        else:
                            mask += 'X'
                    yield mask


def find_prime_v3(x):
    '''Finds the smallest prime which, by replacing part of the number
    with the same digit, is part of an x prime value family
    '''
    for prime in primes:
        str_prime = str(prime)
        # We find all the masks that are possible for the current prime.
        masks = create_masks_v2(str_prime)
        for mask in masks:
            # If the last digit has to be replaced, we won't have more than
            # 5 possible primes (the odd numbers)
            if x <= 5 or mask[-1] != '*':
                count = apply_mask_to_number(mask, str_prime)
                if count == x:
                    return prime, mask
    # The limit for the prime generation is too small
    return -1


# Optimized version for the case of x = 8
def find_prime_8():
    '''Finds the smallest prime which, by replacing part of the number with
    the same digit, is part of an 8 prime value family
    '''
    for prime in primes:
        # Prime as string and number of digits
        str_prime = str(prime)
        count_digits = Counter(str_prime)
        # Not interested if the prime only has one digit
        if len(count_digits) == 1:
            continue

        for digit, count in count_digits.items():
            num_primes = 0
            # Only replace digits that appear 3 times or more and digits 0, 1
            # or 2. If one of this things fail, there can't be 8 primes in the
            # family
            if count < 3 or digit not in '012' or str_prime[-1] == digit:
                continue
            elif count == 3:
                # Can't replace first digit with 0
                nums = ('0123456789' if str_prime[0] != digit else '123456789')
                for i in nums:
                    # Change old digit for new digit
                    new_prime = int(str_prime.replace(digit, i))
                    if new_prime in primes_set:
                        num_primes += 1
                # When we find a family of 8 primes, the prime we started with
                # has to be the smallest with the property
                if num_primes == 8:
                    return prime, str_prime.replace(digit, '*')

            # What this block basically does is to substitute 3 digits out of
            # whatever count there is in all possible combinations.
            # 211113 could be masked as 21***3, 2*1**3, 2**1*3 and 2***13
            # If the digit repeats 5 times, there are even more combinations
            else:
                # All possible groups of 3 of the digit to be replaced
                for mask in bit_strings(count, 3):

                    # Can't replace first digit with 0
                    nums = ('0123456789' if mask[0] != '*' else '123456789')
                    # Temporal mask and values for the mask index and primes
                    prime_mask, num_primes, mask_index = '', 0, 0
                    for dig in str_prime:
                        # If the digit in the number is to be replaced
                        if dig == digit:
                            # We first check what the mask tells and if the
                            # value is not '*', we keep the original digit
                            mask_value = mask[mask_index]
                            prime_mask += (
                                mask_value if mask_value == '*' else dig
                            )
                            mask_index += 1
                        # If the digit is not to be replaced, we just keep it
                        else:
                            prime_mask += dig

                    # Now, we are ready to substitute where we are supposed to
                    for i in nums:
                        new_prime = int(prime_mask.replace('*', i))
                        if new_prime in primes_set:
                            num_primes += 1
                    # When we find a family of 8 primes, the prime we started
                    # with has to be the smallest with the property
                    if num_primes == 8:
                        return prime, prime_mask
    # Limit too small
    return -1


if __name__ == '__main__':
    max_digs = 6
    limit = 10**max_digs  # 6 digits
    primes = sieve_Eratosthenes(limit)[4:]
    primes_set = set(primes)

    print(find_prime_v3(6))  # (13, '*X')
    print(find_prime_v3(7))  # (56003, 'XX**X')
    # print(find_prime(8, max_digs))  # (121313, '*X*X*X'), 6.9s
    # print(find_prime_v2(8))  # (121313, '*X*X*X'), 0.21s
    # A bit slower but correct for x = 5
    # print(find_prime_v3(8))  # (121313,'*X*X*X'), 0.51s
    # Optimization for the case x = 8
    print(find_prime_8())  # (121313, '*2*3*3'), 0.013s


'''
#-------#
# Notes #
#-------#

(1*)
For 2-digit numbers, we have the replacement patterns:
            *X or X*

For 3-digit numbers, we have the replacement patterns:
            Replacing 1 digit gives 3: *XX, X*X, XX*; or 3C1 combinations
            Replacing 2 gives 3: **X, *X*, X**; or 3C2 combinations

For 4-digit numbers, we have the replacement patterns:
            Replacing 1 digit gives 4: *XXX, X*XX, XX*X, XXX*; or 4C1
            Replacing 2 gives 6: **XX, *X*X, *XX*, X**X, X*X*, XX**; or 4C2
            Replacing 3 gives 4: ***X, **X*, *X**, X***; or 4C3

Generalizing for n-digit numbers, to replace k digits, we calculate nCk, and
since k = 1, ..., n-1, we can compute the total number of replacement patterns
as (sum(nCk) for k = 1, ..., n-1) = (sum(nCk) for k = 0, ..., n) - 2 = 2^n - 2

Considering that for each replacement, we can change X to any digit from 0 to
9, and * to the same digit, we can check them one by one.
'''
