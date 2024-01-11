"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from math import floor


def sieve_Eratosthenes_v2_1(n):
    """Basic implementation of the sieve of Eratosthenes.
    Twice as fast compared with v2_0.
    """
    nums = list(range(3, n + 1, 2))
    nums_dict = {num: True for num in nums}
    for num in nums_dict:
        if num * num > n:
            break
        if nums_dict[num]:
            for k in range(num, floor(n / num) + 1, 2):
                nums_dict[num * k] = False
    return sum([k for k, v in nums_dict.items() if v]) + 2


if __name__ == "__main__":
    print(sieve_Eratosthenes_v2_1(10))  # 17
    print(sieve_Eratosthenes_v2_1(2000000))  # 142913828922, 0.43s
