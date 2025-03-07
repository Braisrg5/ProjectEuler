'''https://projecteuler.net/problem=51'''
# By replacing the 1^st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3^rd and 4^th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.
from itertools import combinations
from collections import Counter
from sympy import sieve
from tqdm import tqdm
from resources.useful_functions import sieve_Eratosthenes


def bit_strings(digits, subs):
    '''https://stackoverflow.com/a/63100745
    Generates all combinations with  strings of length n'''
    # List of the indexes of the digits to be replaced
    index_combinations = combinations(range(digits), subs)
    for indices in index_combinations:
        yield ''.join('*' if i in indices else 'X' for i in range(digits))


def apply_mask_to_number(mask, num, primes_set):
    '''mask is a string like 'X*X' or 'XX**X' with the same length as num
    num is a number converted to string
    returns the number of primes which result from substituting the indexes for
    '*' by the same digit in num'''
    # If the first digit has to be replaced, we exclude 0 or either we would
    # get results like 2011 turning into 0011, which would be wrong
    start = (1 if mask[0] == '*' else 0)

    count = 0
    for d in range(start, 10):
        for i, el in enumerate(mask):
            if el == '*':
                num = num[:i] + str(d) + num[i+1:]
        if int(num) in primes_set:
            count += 1
    return count


def create_masks_v2(str_prime):
    '''Creates all possible masks for a given prime number.'''
    digits = len(str_prime)
    # Masks if we replace just one digit:
    masks1 = bit_strings(digits, 1)
    yield from masks1

    count_digits = Counter(str_prime)
    # Masks if we replace more than one digit:
    if len(count_digits) == 1:
        return
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


def find_prime_v3(x, max_digs):
    '''Finds the smallest prime which, by replacing part of the number with the
    same digit, is part of an x prime value family.'''
    limit = 10**max_digs
    primes = sieve_Eratosthenes(limit)[4:]
    primes_set = set(primes)

    for prime in primes:
        str_prime = str(prime)
        # We find all the masks that are possible for the current prime.
        masks = create_masks_v2(str_prime)
        for mask in masks:
            # If the last digit has to be replaced, we won't have more than
            # 5 possible primes (the odd numbers)
            if x <= 5 or mask[-1] != '*':
                count = apply_mask_to_number(mask, str_prime, primes_set)
                if count == x:
                    return prime, mask
    # The limit for the prime generation is too small
    return -1


# Optimized version for the case of x = 8
def find_prime_8(max_digs):
    '''Finds the smallest prime which, by replacing part of the number with
    the same digit, is part of an 8 prime value family.'''
    limit = 10**max_digs
    primes = sieve_Eratosthenes(limit)[4:]
    primes_set = set(primes)
    for prime in primes:
        # Prime as string and number of digits
        str_prime = str(prime)
        count_digits = Counter(str_prime)
        # Not interested if the prime only has one digit
        if len(count_digits) == 1:
            continue
        for digit, count in count_digits.items():
            # Only replace digits that appear 3 times or more and digits 0, 1
            # or 2. If one of this things fail, there can't be 8 primes in the
            # family
            if count < 3 or digit not in '012' or str_prime[-1] == digit:
                continue

            num_primes = 0
            if count == 3:
                # Can't replace first digit with 0
                nums = ('0123456789' if str_prime[0] != digit else '123456789')
                for i in nums:
                    # Change old digit for new digit
                    new_prime = int(str_prime.replace(digit, i))
                    num_primes += new_prime in primes_set
                # When we find a family of 8 primes, the prime we started with
                # has to be the smallest with the property
                if num_primes == 8:
                    return prime, str_prime.replace(digit, '*')

            # What this block basically does is to substitute 3 digits out of
            # whatever count there is in all possible combinations.
            # 211113 could be masked as 21***3, 2*1**3, 2**1*3 and 2***13
            # If the digit repeats 5 times, there are even more combinations
            else:
                #
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


def find_prime_9(max_digs):
    '''Finds the smallest prime which, by replacing part of the number with
    the same digit, is part of a 9 prime value family.'''
    limit = 10**max_digs
    primes = sieve_Eratosthenes(limit)[4:]
    primes_set = set(primes)
    for prime in tqdm(primes):
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
            if count < 3 or digit not in '01' or str_prime[-1] == digit:
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
                if num_primes == 9:
                    return prime, str_prime.replace(digit, '*')

            # What this block basically does is to substitute 3 digits out of
            # whatever count there is in all possible combinations.
            # 211113 could be masked as 21***3, 2*1**3, 2**1*3 and 2***13
            # If the digit repeats 5 times, there are even more combinations
            else:
                # All possible groups of 3 of the digit to be replaced
                for mask in bit_strings(count, 3):
                    # Can't replace first digit with 0
                    if mask[0] == '*' and str_prime[0] == digit:
                        nums = '123456789'
                    else:
                        nums = '0123456789'
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
                    if num_primes == 9:
                        return prime, prime_mask
    # Limit too small
    return -1


def find_prime_10(max_digs):
    '''Finds the smallest prime which, by replacing part of the number with
    the same digit, is part of a 10 prime value family.'''
    limit = 10**max_digs
    for prime in sieve.primerange(limit//10, limit):
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
            if count < 3 or digit != '0' or str_prime[-1] == digit:
                continue
            elif count == 3:
                nums = '0123456789'
                for i in nums:
                    # Change old digit for new digit
                    new_prime = int(str_prime.replace(digit, i))
                    if new_prime in sieve:
                        num_primes += 1
                # When we find a family of 8 primes, the prime we started with
                # has to be the smallest with the property
                if num_primes == 10:
                    return prime, str_prime.replace(digit, '*')

            # What this block basically does is to substitute 3 digits out of
            # whatever count there is in all possible combinations.
            # 211113 could be masked as 21***3, 2*1**3, 2**1*3 and 2***13
            # If the digit repeats 5 times, there are even more combinations
            else:
                # All possible groups of 3 of the digit to be replaced
                for mask in bit_strings(count, 3):
                    nums = '0123456789'
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
                        if new_prime in sieve:
                            num_primes += 1
                    # When we find a family of 8 primes, the prime we started
                    # with has to be the smallest with the property
                    if num_primes == 10:
                        return prime, prime_mask
                if count >= 6:
                    # All possible groups of 3 of the digit to be replaced
                    for mask in bit_strings(count, 6):
                        nums = '0123456789'
                        # Temp mask and values for the mask index and primes
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
                            # If the digit is not to be replaced, we keep it
                            else:
                                prime_mask += dig
                        # Now, we are ready to substitute
                        for i in nums:
                            new_prime = int(prime_mask.replace('*', i))
                            if new_prime in sieve:
                                num_primes += 1
                        # When we find a family of 8 primes, the prime we
                        # started with has to be the smallest with the property
                        if num_primes == 10:
                            return prime, prime_mask
    # Limit too small
    return -1


if __name__ == '__main__':
    print(find_prime_v3(6, max_digs=6))  # (13, '*X')
    print(find_prime_v3(7, max_digs=6))  # (56003, 'XX**X')
    # Optimization for the case x = 8
    print(find_prime_8(max_digs=6))  # (121313, '*2*3*3'), 0.013s
    print(find_prime_9(max_digs=8))  # (38000201, '38*0*2*1'), 10.21s

    # Can't use sieve, need different approach
    # print('Test with x = 10')
    # print(find_prime_10(max_digs=11))


# ----- #
# Notes #
# ----- #

# (1*)
# For 2-digit numbers, we have the replacement patterns:
#             *X or X*

# For 3-digit numbers, we have the replacement patterns:
#             Replacing 1 digit gives 3: *XX, X*X, XX*; or 3C1 combinations
#             Replacing 2 gives 3: **X, *X*, X**; or 3C2 combinations

# For 4-digit numbers, we have the replacement patterns:
#             Replacing 1 digit gives 4: *XXX, X*XX, XX*X, XXX*; or 4C1
#             Replacing 2 gives 6: **XX, *X*X, *XX*, X**X, X*X*, XX**; or 4C2
#             Replacing 3 gives 4: ***X, **X*, *X**, X***; or 4C3

# Generalizing for n-digit numbers, to replace k digits, we calculate nCk, and
# since k = 1, ..., n-1, we can compute the total number of replacement
# patterns as:
#   (sum(nCk) for k = 1, ..., n-1) = (sum(nCk) for k = 0, ..., n) - 2 = 2^n - 2

# Considering that for each replacement, we can change X to any digit from 0 to
# 9, and * to the same digit, we can check them one by one.
