'''https://projecteuler.net/problem=66
Consider quadratic Diophantine equations of the form:
            x^2 - D*y^2 = 1

For example, when D = 13, the minimal solution in x is 649^2 - 13*180^2 = 1.
It can be assumed that there are no solutions in positive integers when
D is square.

By finding the minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:
            3^2 - 2*2^2 = 1
            2^2 - 3*1^2 = 1
            9^2 - 5*4^2 = 1
            5^2 - 6*2^2 = 1
            8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D = 5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
'''
from math import sqrt
from tqdm import tqdm
from problem_065F import recurring_convergents


def minimal_value(D):
    '''Finds the minimal solution in x for the Diophantine equation
    x^2 - D*y^2 = 1.'''
    # D can't be a square
    if sqrt(D).is_integer():
        return float('-inf')

    y = 1
    while not sqrt(1 + D*y**2).is_integer():
        y += 1
    return int(sqrt(1 + D*y**2))


def max_x_minimal_solutions(bound):
    '''Finds the value of D <= bound in minimal solutions of x for which
    the largest value of x is obtained.'''
    max_x = float('-inf')
    max_D = 0
    for D in tqdm(range(2, bound+1)):
        x = minimal_value(D)
        if x > max_x:
            max_x = x
            max_D = D
    return max_D


if __name__ == '__main__':
    # print(minimal_value(13))  # 649
    # print(max_x_minimal_solutions(7))  # 5
    # Not viable, some D do NOT give a solution
    # print(max_x_minimal_solutions(1000))

    terms = [2, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    for i in range(len(terms)):
        print(recurring_convergents(terms[:i+1]))


'''
#-------#
# Notes #
#-------#

(1*)
I first tried to do this by brute force



'''
