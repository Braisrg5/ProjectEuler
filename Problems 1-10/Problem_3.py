from math import sqrt, floor


def is_prime(n):
    '''Checks if n is a prime number by dividing it by 2 and 3 and
    then checking '''
    end = floor(sqrt(n))
    if n == 1:
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for j in range(6, end+2, 6):
        if n % (j-1) == 0 or n % (j+1) == 0:
            return False
        j += 6
    return True


def primeFactors(n, listFact = []):
    '''Checks '''
    if n == 1:
        return listFact
    elif n % 2 == 0:
        return primeFactors(n/2, listFact + [2])
    elif n % 3 == 0:
        return primeFactors(n/3, listFact + [3])
    for j in range(6, int(n)+2, 6):
        p1, p2 = j-1, j+1
        if is_prime(p1) and n % p1 == 0:
            return primeFactors(n/p1, listFact + [p1])
        elif is_prime(p2) and n % p2 == 0:
            return primeFactors(n/p2, listFact + [p2])
    return -1
        

def largePrimeFact(n):
    return primeFactors(n)
    
    
if __name__ == "__main__":
    print(is_prime(25))
