'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


from math import sqrt, floor
from time import time
from numpy import unique

def primesUpTo(n, primeList):
    '''Returns the list of primes up to the square root of n.
    '''
    end = floor(sqrt(n))
    l = []
    for i in primeList:
        if i > end:
            break
        l.append(i)
    return l


def sumPrimesUpTo(n):
    '''Sums the primes below n.
    Variation of the nthPrime function of problem 7.
    '''
    primeList = [2, 3, 5, 7]
    if n <= 11:
        s = 0
        for i in primeList:
            if i < n:
                s += i
        return s
    # Not needed to divide by 2 or 3, we take numbers of the form 6*j +- 1
    primeList = primeList[2:]
    for j in range(12, n+1, 6):
        for k in (j-1, j+1):
            for p in primesUpTo(k, primeList):
                if k % p == 0:
                    break
            else:
                primeList.append(k)
    if primeList[-1] >= n: del primeList[-1]
    return sum(primeList) + 5


def sieveEratosthenes(n):
    '''Basic implementation of the sieve of Eratosthenes.
    Very unoptimized but much faster than previously.
    '''
    nums = list(range(2, n + 1))
    numsDict = {num:0 for num in nums}
    for num in numsDict:
        if num*num > n:
            break
        if numsDict[num] == 0:
            for k in range(num, floor(n/num)+1):
                numsDict[num*k] = 1
    return sum([k for k, v in numsDict.items() if v == 0])
   

if __name__ == "__main__":
    # print(sumPrimesUpTo(10)) # 17
    # print(sumPrimesUpTo(2000000)) # 142913828922, 6.8s
    start = time()
    print(sumPrimesUpTo(2000000)) # 6.8s
    print(time() - start, "seconds")
    start = time()
    print(sieveEratosthenes(2000000)) # 0.92s
    print(time() - start, "seconds")