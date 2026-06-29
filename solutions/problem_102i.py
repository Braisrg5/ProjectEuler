'''https://projecteuler.net/problem='''


def check_same_side(line_1, line_2, opposite):
    '''For the line that goes through the points in line, we check if the point
    is on the same side as the origin.'''
    # For each side of the triangle, we need to check if the origin is on the
    # same side as the third vertex. (1*)
    a1, a2 = line_1
    b1, b2 = line_2
    c1, c2 = opposite

    if b1 == a1:
        # The line is vertical, so we check if the x coordinates are on the
        # same side of the line.
        return (c1 - a1) * (0 - a1) > 0
    else:
        m = (b2 - a2)/(b1 - a1)
        o_value = m*a1 - a2
        c_value = c2 - m*c1 + o_value
        # If the product is positive, the values are of the same sign!
        return o_value*c_value > 0


def contains_origin(A, B, C):
    '''Checks if the triangle ABC contains the origin.'''
    if (check_same_side(A, B, C) and check_same_side(B, C, A)
            and check_same_side(A, C, B)):
        return True
    return False


def load_points(path):
    '''Loads the points from the path and returns them as an array of lists of
    three tuples.'''
    with open(path, 'r', encoding='utf-8') as file:
        points = [
            [int(j) for j in i.replace('\n', '').split(',')]
            for i in file.readlines()
        ]
    return points


def count_triangles_with_origin(points):
    '''Counts the number of triangles that contain the origin.'''
    count = 0
    for triangle in points:
        A = (triangle[0], triangle[1])
        B = (triangle[2], triangle[3])
        C = (triangle[4], triangle[5])
        if contains_origin(A, B, C):
            count += 1
    return count


def main():
    '''Main code of module.'''
    print(contains_origin((-340, 495), (-153, -910), (835, -947)))  # True
    print(contains_origin((-175, 41), (-421, -714), (574, -645)))  # False
    point_list = load_points('resources/0102_triangles.txt')
    print(count_triangles_with_origin(point_list))  # 228, 0.0007s


if __name__ == '__main__':
    main()

# ----- #
# Notes #
# ----- #

# (1*)
# If we take the line through the points A and B, we can find the equation
# of the line:
#       y - a2 = m*(x - a1)
# where m = (b2 - a2)/(b1 - a1).

# We get, after reordering:
#       y - m*x + (m*a1 - a2) = 0.

# If we substitute here the coordinates of C, we get:
#       c2 - m*c1 + (m*a1 - a2)
# And for the origin, we get:
#       0 - m*0 + (m*a1 - a2) = m*a1 - a2
# If these results are of the same sign, then C and the origin are on the
# same side of the line.

# Then, we do the same for the lines through A and C, and B and C.
# If the origin is always on the same side as the third vertex, it is inside
# the triangle.
