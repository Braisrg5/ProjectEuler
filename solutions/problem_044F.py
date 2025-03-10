'''https://projecteuler.net/problem=44
Pentagonal numbers are generated by the formula, Pn = n(3n-1)/2. The first
ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk-Pj| is minimized; what is the value of D?
'''
from resources.useful_functions import is_pentagonal
from tqdm import tqdm


def pent_pair(MAX):
    pentagonals = [i*(3*i-1)//2 for i in range(1, MAX+3)]
    min_D = float('inf')
    # We go through all pairs of pentagonal numbers for i, j < MAX
    # If I had to prove that there isn't another pair with a smaller
    # difference, I would have to execute the program for the range(1, 1827554)
    # Update: thanks ChatGPT
    for k in tqdm(range(MAX+2)):
        Pk = pentagonals[k]
        # Backwards search to minimize the difference
        for j in range(k-1, 0, -1):
            Pj = pentagonals[j]
            D = Pk - Pj
            if D > min_D:
                # If j = k - 1, we have proven the difference is minimal
                if (k - j) == 1:
                    return 'SOLVED'
                break
            # Sum and difference are pentagonals
            if is_pentagonal(Pk + Pj) and is_pentagonal(D):
                min_D = D
                print('Pj = {}, Pk = {}, D = {}'.format(Pj, Pk, Pk - Pj))
    # If the MAX isn't large enough to prove the minimum
    return -1


if __name__ == '__main__':
    print(pent_pair(1827553))  # 5482660, 5.85s

'''
#-------#
# Notes #
#-------#

(1*)
The first thing I'm going to do is find a pair of numbers that satisfy the
property to have an upper bound for the difference.

Since P = n(3n-1)/2, if we write it in quadratic form, we get:
            3n^2 - n - 2P = 0,
and solving for n, we get:
            n = (1 + sqrt(1 + 24P))/6
Thus, P is pentagonal when n is an integer.

I created the program without a known upper bound, and the first candidate that
I found was 5482660, which happens to be the PE solution, but I wondered how to
prove that it is in fact the smallest. After some thought, I concluded that we
need to compute up to an k such that P(k+1) - P(k) > 5482660, because beyond
that index, it's impossible for the difference to be smaller.

The formula to calculate P(k+1) - P(k) is:
            P(k+1) - P(k) = (k+1)*(3*(k+1) - 1)/2 - k*(3*k - 1)/2 =
            = [(k+1)*(3k + 2) - 3k^2 + k]/2 =
            = [3k^2 + 2k + 3k + 2 - 3k^2 + k]/2 = [6k + 2]/2 = 3k + 1
So, we need that 3k + 1 > 5482660, so:
            k > (5482660 - 1)/3 -> k > 1827553

In other words, if we check up to kMAX = 1827553, we will necessarily find the
minimum difference.

In the program it is implemented in another way:
I start with k = 1...kMAX and I run through j = k-1...1 (backwards).
When Pk - P(k-1) is greater than the currently known solution, I consider the
known difference proven to be minimal.
Actually, if I do pent_pair(1827552), the program returns -1, and if I do
pent_pair(1827553), the program returns "SOLVED".
'''
