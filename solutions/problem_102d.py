'''https://projecteuler.net/problem='''


def contains_origin(A, B, C):
    '''Checks if the triangle ABC contains the origin.'''
    # If we take the line through the points A and B, we can find the equation
    # of the line:
    # y - a2 = m*(x - a1)
    # where m = (b2 - a2)/(b1 - a1)
    # We need to check if c and the origin are on the same side of the line.
    # This is done by checking the sign of the determinant:
    # | a1 b1 1 |
    # | a2 b2 1 |
    # | 0  0  1 |
    # If the determinant is positive, the origin is on the same side of the line
    return True


def main():
    '''Main code of module.'''


if __name__ == '__main__':
    main()