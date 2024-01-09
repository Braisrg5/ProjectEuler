'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


from math import sqrt, floor
from time import time


def sieveEratosthenes_v2_1(n):
    '''Basic implementation of the sieve of Eratosthenes.
    Twice as fast compared with v2_0.
    '''
    nums = list(range(3, n + 1, 2))
    numsDict = {num:True for num in nums}
    for num in numsDict:
        if num*num > n:
            break
        if numsDict[num] == True:
            for k in range(num, floor(n/num)+1, 2):
                numsDict[num*k] = False
    return sum([k for k, v in numsDict.items() if v]) + 2
   

if __name__ == "__main__":
    # print(sumPrimesUpTo(10)) # 17
    print(sieveEratosthenes_v2_1(2000000)) # 142913828922, 0.43s
