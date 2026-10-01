'''https://projecteuler.net/problem=82'''
# NOTE: This problem is a more challenging version of Problem 81.

# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
# the left column and finishing in any cell in the right column, and only
# moving up, down, and right, is indicated in red and bold; the sum is equal
# to 994.

#   131  673  234* 103*  18*
#   201*  96* 342* 965  150
#   630  803  746  422  111
#   537  699  497  121  956
#   805  732  524   37  331

# Find the minimal path sum from the left column to the right column in
# matrix.txt, a 31K text file containing an 80 by 80 matrix.
from pathlib import Path
import numpy as np


def load_matrix(path):
    '''Loads the matrix from the given path.'''
    file_path = Path(__file__).parent / path
    with open(file_path, 'r', encoding='utf-8') as file:
        matrix = np.array([
            [int(num) for num in line.strip().split(',')]
            for line in file if line.strip()
        ])
    return matrix


def h(cell, n):
    '''Heuristic function that calculates the horizontal distance from the
    current cell (x, y) to the right column, in a matrix of size n x n.'''
    return 1*(abs(n - 1 - cell[1]))


def d(cell, matrix):
    '''Calculates the value of cell in the matrix (edge).'''
    x, y = cell
    return matrix[(x, y)]


def reconstruct_path(came_from, current):
    '''Reconstructs the path to get from the start to the goal.'''
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]


def neighbors(cell, n):
    '''Gives the neighboring cells of the current cell (4 directions).'''
    x, y = cell
    neighbor_list = []
    # The initial cell communicates with all of the left column
    if cell == ('Initial', 'Cell'):
        for i in range(n):
            neighbor_list.append((i, 0))
        return neighbor_list
    # Right
    if y < n - 1:
        neighbor_list.append((x, y + 1))
    # Up
    if x > 0:
        neighbor_list.append((x - 1, y))
    # Down
    if x < n - 1:
        neighbor_list.append((x + 1, y))
    return neighbor_list


def a_start_algorithm(matrix):
    '''Application of the A* algorithm to find the minimal path sum from top
    left to bottom right for a given matrix.
    The code is based on the pseudocode in the Wikipedia page of the algorithm
    https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode'''
    n = matrix.shape[0]
    goal = n - 1
    # Create a node at the beginning that is neighbor of all the nodes in the
    # first column
    start = ('Initial', 'Cell')
    open_set = set([start])
    came_from = {}

    # The first node in this case has 0 weight
    g_score = {start: 0}
    f_score = {}
    f_score[start] = 0
    while len(open_set) != 0:
        current = min(open_set, key=f_score.get)
        if current[1] == goal:
            return g_score[current]  # , reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbor in neighbors(current, n):
            pos_g_score = g_score[current] + d(neighbor, matrix)
            if neighbor not in g_score or pos_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = pos_g_score
                f_score[neighbor] = pos_g_score + h(neighbor, n)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return 'fail'


def main():
    '''Main code of module.'''
    small_matrix = np.array((
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331]
        ))
    print(a_start_algorithm(small_matrix))

    big_matrix = load_matrix("resources/0082_matrix.txt")  # 427337, 0.004s
    print(a_start_algorithm(big_matrix))  # 260324, 0.034s


if __name__ == '__main__':
    main()
