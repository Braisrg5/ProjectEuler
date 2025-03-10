"""By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.
               3
              7 4
             2 4 6
            8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in 68_triangle.txt, a 15K file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2^99 altogether! If you
could check one trillion (10^12) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
"""


def load_triangle(path):
    """Loads the triangle from the path and returns it as an array."""
    with open(path, "r") as file:
        triangle = [[int(j) for j in i.replace("\n", "").split(" ")]
                    for i in file.readlines()
                    ]
    return triangle


def max_route(triangle):
    """Finds the maximum sum from top to bottom of the triangle."""
    n = len(triangle)
    accumulated = triangle[n-1]
    for k in range(n-2, -1, -1):
        target = triangle[k]
        for i in range(k+1):
            target[i] += max(accumulated[i:i+2])
        accumulated = target
    return accumulated[0]


if __name__ == "__main__":
    triangle = load_triangle("resources/67_triangle.txt")
    print(max_route(triangle))  # 7273, 0.003s
