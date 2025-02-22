"""Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle    Tn = n(n + 1)/2     1, 3, 6, 10, 15, ...
Pentagonal  Pn = n(3n - 1)/2    1, 5, 12, 22, 35, ...
Hexagonal   Hn = n(2n - 1)      1, 6, 15, 28, 45, ...

It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal."""
from resources.useful_functions import is_hexagonal, is_pentagonal


def tph(MIN, MAX):
    """Finds the next triangle number that is pentagonal and hexagonal."""
    for n in range(MIN, MAX):
        Tn = n*(n+1)//2
        if is_pentagonal(Tn) and is_hexagonal(Tn):
            return Tn


if __name__ == "__main__":
    print(tph(2, 286))  # 40755
    print(tph(286, 10**10))  # 1533776805, 0.057s
