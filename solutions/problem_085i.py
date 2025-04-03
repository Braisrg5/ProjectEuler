'''https://projecteuler.net/problem=85'''
from math import sqrt


def calculate_rectangles(n, m):
    '''Calculates the number of rectangles in a n x m rectangle.'''
    return (n*(n+1)//2)*(m*(m+1)//2)


def find_closest_rectangle(target):
    '''Finds the area of the rectangle which has the number of rectangles that
    is closest to the target.'''
    min_diff = float('inf')
    n_lim = int((-1+sqrt(1+8*target))/2)
    obj_area = 0
    for n in range(1, n_lim+1):
        # Calculate m that is close to given target
        m_close = int(-1/2 + sqrt(1/4 + 4*target/(n*(n+1))))
        diff = target - calculate_rectangles(n, m_close)
        if diff < min_diff:
            min_diff = diff
            obj_area = (n * m_close, (n, m_close))
        diff = calculate_rectangles(n, m_close+1) - target
        if diff < min_diff:
            min_diff = diff
            obj_area = (n * (m_close+1), (n, m_close+1))

    return obj_area


def main():
    '''Main code of module.'''
    print(calculate_rectangles(3, 2))  # 18
    print(find_closest_rectangle(2000000))  # 2772, (36, 77), 0.0011s


if __name__ == '__main__':
    main()
