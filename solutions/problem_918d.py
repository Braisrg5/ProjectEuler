'''https://projecteuler.net/problem=918'''


def sum_recursive_sequence(bound):
    '''Finds the sum of the recursive sequence up to n=bound.'''
    new_bound = bound
    if new_bound % 2 == 0:
        new_bound += 1
    seq = [0] * (new_bound + 1)

    seq[1] = 1
    for i in range(1, (new_bound-1)//2 + 1):
        seq[2*i] = 2*seq[i]
        seq[2*i + 1] = seq[i] - 3*seq[i+1]
    return sum(seq[:bound+1])


def main():
    '''Main code of module.'''
    print(sum_recursive_sequence(10**8))


if __name__ == '__main__':
    main()
