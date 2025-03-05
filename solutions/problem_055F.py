'''https://projecteuler.net/problem=55
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes on reverse and addition. For example,
            349 + 943 = 1292,
            1292 + 2921 = 4213,
            4213 + 3124 = 7337.
That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number. Due to the theoretical
nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition you are given that
for every number below ten-thousand, it will either (i) become a palindrome in
less than fifty iterations, or, (ii) no one, with all the computing power that
exists, has managed so far to map it to a palindrome. In fact, 10677 is the
first number to be shown to require over fifty iterations before producing a
palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel
numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?'''
from resources.useful_functions import is_palindrome, flip_number


def is_Lychrel(n, its):
    '''Finds if a number n does not becomes palindrome after repeatedly doing
    reverse and addition in its tries.'''
    for _ in range(its):
        n += flip_number(n)
        # Reverse and addition until we reach a palindrome
        if is_palindrome(n):
            return False
    # After its tries, we consider the number to be Lychrel
    return True


def num_Lychrels(bound, its):
    '''Finds the amount of Lychrel numbers below the given bound and with the
    given max iterations.'''
    return len([i for i in range(bound) if is_Lychrel(i, its)])


if __name__ == '__main__':
    print(is_Lychrel(196, 50))  # True
    print(is_Lychrel(4994, 50))  # True
    print(num_Lychrels(10000, 50))  # 249, 0.02s
