'''By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see
that the 6th prime is 13.
What is the 10001st prime number?
'''


from math import log, ceil, sqrt, floor

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


def nthPrime(n):
    '''Returns the nth prime number. Creates a list progressively of primes in
    order to do the checking in an easier manner. The list could be stored in
    a file to further use, but I didn't feel like it was neccesary.
    I may implement it in the future.
    '''
    primeList = [2, 3, 5, 7, 11, 13]
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
    print(nthPrime(6)) # 13
    print(nthPrime(10001)) # 104743
