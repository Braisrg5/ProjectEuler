'''2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any reminder.
What is the smallest positive number that is evenly divisible by all the 
numbers from 1 to 20?
'''


from math import sqrt, floor

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

def counts(l):
    '''Counts the number of times an element appears on a list.
    '''
    counts = dict()
    for i in l:
        counts[i] = counts.get(i, 0) + 1
    return counts


def factorsToNumber(factors):
    '''Translates a dictionary of prime factors to a number.
    '''
    n = 1
    for key, value in factors.items():
        n *= key**value
    return n

def lcm(numbers):
    '''Finds the least common multiple of a list of numbers, following the
    method of multiplying the prime factors to the highest exponent.
    A method using the Euclidean algorithm is in the back of my mind.
    '''
    factorsList = [counts(primeFactors(n)) for n in numbers]
    newFactors = dict()
    for factors in factorsList:
        for key, value in factors.items():
            if key in newFactors.keys():
                if value > newFactors[key]:
                    newFactors[key] = value
            else:
                newFactors[key] = value
    return factorsToNumber(newFactors)


if __name__ == '__main__':
    tenFirst = list(range(1,11))
    print(lcm(tenFirst)) # 2520
    twentyFirst = list(range(1,21))
    print(lcm(twentyFirst)) # 232792560