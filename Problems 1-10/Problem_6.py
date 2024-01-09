def diffSquares(n):
    '''Returns the difference between the sum of the squares and the
    square of the sum of the nth natural numbers using Faulhaber's
    formula in both cases.'''
    sumSquared = n**2*(n+1)**2//4
    sumOfSquares = (2*n**3 + 3*n**2 + n)//6
    return sumSquared - sumOfSquares

if __name__ == '__main__':
    print(diffSquares(10))