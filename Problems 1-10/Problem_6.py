'''The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385.
The square of the sym of the first ten natural numbers is,
            (1 + 2 +... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

def diffSquares(n):
    '''Returns the difference between the sum of the squares and the
    square of the sum of the nth natural numbers using Faulhaber's
    formula in both cases.'''
    sumSquared = n**2*(n+1)**2//4
    sumOfSquares = (2*n**3 + 3*n**2 + n)//6
    return sumSquared - sumOfSquares

if __name__ == '__main__':
    print(diffSquares(10)) # 2640
    print(diffSquares(100)) # 25164150