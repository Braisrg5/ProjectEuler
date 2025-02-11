"""By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
               3
              7 4
             2 4 6
            8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle in
18_triangle.txt.

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)


I originally brute-forced this problem, and reading the thread I got
spoiled the "clever" method, so Imma do it that way.
"""


def load_triangle(path):
    """Loads the triangle from the path and returns it as an array."""
    file = open(path, "r")
    triangle = [
        [int(j) for j in i.replace("\n", "").split(" ")]
        for i in file.readlines()
    ]
    file.close()
    return triangle


def max_route(triangle):
    """Finds the maximum sum top to bottom in the triangle."""
    n = len(triangle)
    accumulated = triangle[n-1]
    for k in range(n-2, -1, -1):
        target = triangle[k]
        for i in range(len(target)):
            target[i] += max(accumulated[i:i+2])
        accumulated = target
    return accumulated[0]


if __name__ == "__main__":
    small_triangle = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3]
    ]
    print(max_route(small_triangle))  # 23
    triangle = load_triangle("resources/18_triangle.txt")
    print(max_route(triangle))  # 1074, 0.0002s
