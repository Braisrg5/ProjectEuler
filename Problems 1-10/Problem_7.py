from math import log, ceil, sqrt, floor

def primesUpTo(n, primeList):
    '''Returns the list of primes up to n.
    '''
    end = floor(sqrt(n))
    l = []
    for i in primeList:
        if i > end:
            break
        l.append(i)
    return l


def nthPrime(n):
    '''Returns the nth prime number.
    '''
    current, primeList = 6, [2, 3, 5, 7, 11, 13]
    if n <= 6:
        return primeList[n-1]
    # Not needed to divide by 2 or 3, we take numbers of the form 6*j +- 1
    primeList = primeList[2:]
    # upper bound derived from Rosser's theorem (found in Wikipedia)
    # only valid for n >= 6
    upperBound = ceil(n*(log(n) + log(log(n))))
    for j in range(18, upperBound+2, 6):
        for k in (j-1, j+1):
            for p in primesUpTo(k, primeList):
                if k % p == 0:
                    break
            else:
                primeList.append(k)
        if len(primeList) >= n-2:
            break
    return primeList[n-3]

if __name__ == "__main__":
    print(nthPrime(10001))