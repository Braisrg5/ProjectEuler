"""A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of
the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
                012  021  102  120  201  210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?


The number of possible permutations is the factorial of the number of
(different) objects we have. In this case, 10! = 3628800.
By ordering the permutations lexicographically, we can observe that the
first 10!/10 = 362880 permutations start with 0, and the next 362880
start with 1 and so on. Also, the first 362880/9 = 40320 start with 01,
and permutations from 362881 to 362881 + 40320 start with 10, etc.

We can work out the first number of the millionth permutation by seeing
how many times 362880 "fits" behind 1000000, i.e. 2. Then, we can
calculate how many times 40320 fits between 362880*2 and 1000000,
i.e. 6. So, the first two numbers would be 27 (6th position of the
remaining numbers). We can continue this process until we run out of
numbers, and by construction, arrive to a solution.

I programmed the generalized function but that's just because I
practiced with a smaller set.
"""


from math import factorial, floor


def pth_permutation(p, objects):
    """Finds the pth permutation by lexicographic order within the set
    of permutations of the given objects (expected to be different)."""
    n = len(objects)
    total = factorial(n)
    perm = ""
    for k in range(n, 1, -1):
        total = floor(total / k)
        pos = floor((p - 1) / total)
        perm += str(objects.pop(pos))
        p -= total * pos
    return perm + str(objects.pop())


if __name__ == "__main__":
    print(pth_permutation(3, list(range(3))))  # 102
    print(pth_permutation(1000000, list(range(10))))  # 2783915460, 0.0s
