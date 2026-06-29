'''https://projecteuler.net/problem=92'''
from tqdm import tqdm


def end_at_89(bound):
    '''Finds how many numbers below bound end the chain created by adding the
    square of their digits at 89.'''
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    end_at = {1: 1, 89: 89}

    # Initialize numbers for which the chain contain len_chain elements
    for n in tqdm(range(1, bound)):
        # Skip if already calculated
        if n in end_at:
            continue
        current = n
        current_list = []
        while current not in end_at:
            current_list.append(current)
            total = 0
            while current > 0:
                total += squares[current % 10]
                current //= 10
            current = total

        for el in current_list:
            end_at[el] = end_at[current]
    return sum(1 for k, v in end_at.items() if v == 89 and k < bound)


def end_at_89_v2(bound):
    '''Finds how many numbers below bound end the chain created by adding the
    square of their digits at 89.'''
    squares = [i*i for i in range(10)]

    end_at = {1: 1, 89: 89}
    lex_end_at = {'1': 1, '89': 89}

    # Initialize numbers for which the chain contain len_chain elements
    for n in tqdm(range(1, bound)):
        sorted_n = ''.join(sorted(str(n)))
        # Skip if already calculated
        if sorted_n in lex_end_at:
            if n not in end_at:
                end_at[n] = lex_end_at[sorted_n]
            continue

        current = sorted_n
        current_list = []
        while current not in lex_end_at:
            current_list.append(current)

            int_current = int(current)
            total = 0
            while int_current > 0:
                total += squares[int_current % 10]
                int_current //= 10
            int_current = total
            current = ''.join(sorted(str(int_current)))

        for el in current_list:
            lex_end_at[el] = lex_end_at[current]
        end_at[n] = lex_end_at[current]
    return sum(1 for k, v in end_at.items() if v == 89 and k < bound)


def end_at_89_v3(bound):
    '''Finds how many numbers below bound end the chain created by adding the
    square of their digits at 89.'''
    # Precompute squares of digits 0-9
    squares = [i*i for i in range(10)]
    # Precompute the maximum square sum for the given bound
    max_square_sum = 9*9*len(str(bound))

    # Cache of all possible sums
    cache = [0] * (max_square_sum + 1)
    cache[1], cache[89] = 1, 89

    for i in range(2, max_square_sum + 1):
        if cache[i] != 0:
            continue

        current_list = []
        current = i
        while True:
            current_list.append(current)
            # Compute digit square sum
            total = 0
            while current > 0:
                total += squares[current % 10]
                current //= 10
            current = total

            if current < len(cache) and cache[current] != 0:
                end = cache[current]
                break

        for num in current_list:
            if num < len(cache):
                cache[num] = end

    count = 0
    for n in tqdm(range(1, bound)):
        # Compute digit square sum for n
        total = 0
        m = n
        while m > 0:
            total += squares[m % 10]
            m //= 10
        if cache[total] == 89:
            count += 1
    return count


def main():
    '''Main code of module.'''
    from time import perf_counter
    # print(end_at_89(10**7))  # 8581146, 8.24s

    start = perf_counter()
    print(end_at_89_v2(10**7))  # 8581146, 8.24s
    print(perf_counter() - start)

    start = perf_counter()
    print(end_at_89_v3(10**7))  # 8581146, 8.24s
    print(perf_counter() - start)


if __name__ == '__main__':
    main()
