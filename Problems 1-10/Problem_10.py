'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


from math import sqrt, floor
from time import time

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
    i, p = 0, 2
    while True:
        if p*p > n:
            break
        for k in range(p, floor(n/p)+1):
            if p*k in nums: nums.remove(p*k)
        i += 1
        p = nums[i]
    return sum(nums)
   

if __name__ == "__main__":
    # print(sumPrimesUpTo(10)) # 17
    # print(sumPrimesUpTo(2000000)) # 142913828922, 6.8s
    start = time()
    print(sumPrimesUpTo(10000)) # 0.006s
    print(time() - start, "seconds")
    start = time()
    print(sieveEratosthenes(10000)) # 0.5s
    print(time() - start, "seconds")
