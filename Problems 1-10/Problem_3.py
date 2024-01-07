from math import sqrt, floor


def is_prime(n):
    '''Checks if n is a prime number by dividing it by 2 and 3 and then checking
    the numbers of the form 6*j + 1 and 6*j - 1, where j is an integer, and up to
    the square root of n. This are the only numbers of the form 6*j + k than can 
    be prime, and thus we skip many numbers and reduce computation time.
    '''
    end = floor(sqrt(n))
    if n == 1:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # end+2 to ensure that 6*j+1 is included
    for j in range(6, end+2, 6):
        if n % (j-1) == 0 or n % (j+1) == 0:
            return False
    return True


def primeFactors(n, listFact = []):
    '''Constructs a list of the factors of a number, from smallest to largest. 
    Works in a similar manner to the previous function, but calls itself after
    adding each factor, and at the same time divides the number by them
    '''
    end = floor(sqrt(n))
    if n == 1:
        return listFact
    elif n % 2 == 0:
        return primeFactors(n//2, listFact + [2])
    elif n % 3 == 0:
        return primeFactors(n//3, listFact + [3])
    for j in range(6, end+2, 6):
        p1, p2 = j-1, j+1
        if n % p1 == 0:
            return primeFactors(n//p1, listFact + [p1])
        elif n % p2 == 0:
            return primeFactors(n//p2, listFact + [p2])
    return listFact + [n]
        

if __name__ == "__main__":
    print(primeFactors(5350800)) # [2, 2, 2, 2, 3, 5, 5, 7, 7, 7, 13]
    print(primeFactors(600851475143)) # [71, 839, 1471, 6857]
    print(primeFactors(1))

