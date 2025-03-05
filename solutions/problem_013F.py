'''https://projecteuler.net/problem=13
Work out the first ten digits of the sum of the one-hundred 50-digit
numbers from 13_numbers.txt.
'''


def load_numbers(path):
    '''Loads the numbers from path.'''
    with open(path, 'r') as file:
        numbers = [int(i.replace('\n', '')) for i in file.readlines()]
    return numbers


def sum_numbers():
    '''Sums the 100 50-digit numbers.'''
    # Computers are strong
    return sum(load_numbers('resources/13_numbers.txt'))


if __name__ == '__main__':
    print(str(sum_numbers())[:10])  # 5537376230, 0.0004s
