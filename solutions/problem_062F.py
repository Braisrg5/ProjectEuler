'''https://projecteuler.net/problem=62'''
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are
# cube.


def cube_permutations(k):
    '''Finds the smallest cube for which exactly five permutations of its
    digits are also cube.'''
    # Initialize dictionary and n
    digit_cubes, n = {}, 1
    while True:
        # Generate cube for current n
        cube = n**3
        str_cube = str(cube)
        # Sort the digits for uniqueness
        digits = ''.join(sorted(str_cube))
        # Add cube to the dictionary for sorted digits
        digit_cubes[digits] = digit_cubes.get(digits, []) + [cube]
        # Break the loop if we have found the required number of permutations
        if len(digit_cubes[digits]) == k:
            return min(digit_cubes[digits])
        n += 1


if __name__ == '__main__':
    print(cube_permutations(3))  # 41063625
    print(cube_permutations(5))  # 1270350783, 0.010s
