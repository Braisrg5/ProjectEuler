'''https://projecteuler.net/problem=81'''
# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold red
# and is equal to 2427.

#   131* 673  234  103   18
#   201*  96* 342* 965  150
#   630  803  746* 422* 111
#   537  699  497  121* 956
#   805  732  524   37* 331*

# Find the minimal path sum from the top left to the bottom right by only
# moving right and down in matrix.txt, a 31K text file containing an
# 80 by 80 matrix.
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
    '''Heuristic function that calculates the taxicab distance from the current
    cell (x, y) to the bottom right cell, in a matrix of size n x n.'''
    x, y = cell
    return 1*(abs(n - 1 - x) + abs(n - 1 - y))


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
    # Right
    if y < n - 1:
        neighbor_list.append((x, y + 1))
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
    goal = (n - 1, n - 1)
    open_set = set([(0, 0)])
    came_from = {}

    # The first node has weight in this matrix
    g_score = {(0, 0): d((0, 0), matrix)}
    f_score = {}
    f_score[(0, 0)] = g_score[(0, 0)] + h((0, 0), n)
    while len(open_set) != 0:
        current = min(open_set, key=f_score.get)
        if current == goal:
            return g_score[goal]  # reconstruct_path(came_from, current)

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

    big_matrix = load_matrix("resources/0081_matrix.txt")
    print(a_start_algorithm(big_matrix))  # 427337, 0.0318s


if __name__ == '__main__':
    main()
