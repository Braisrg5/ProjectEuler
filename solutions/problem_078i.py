'''https://projecteuler.net/problem=78'''
from time import perf_counter


def pentagonal(n):
    '''Calculates the nth pentagonal number.'''
    return n*(3*n-1)//2


def compute_partitions_v2(max_n):
    '''Finds the number of integer partitions of max_n.'''
    parts = [1]
    pent_vals = [(0, 0)]
    for n in range(1, max_n+1):
        parts.append(0)
        for k in range(1, n+1):
            coef = (-1)**(k+1)
            if k < len(pent_vals):
                t1, t2 = pent_vals[k]
            else:
                t1, t2 = pentagonal(k), pentagonal(-k)
                pent_vals.append((t1, t2))
            if t1 <= n:
                parts[n] += coef * parts[n-t1]
            else:
                break
            if t2 <= n:
                parts[n] += coef * parts[n-t2]
    return parts[max_n]


def compute_partitions_div_v2(div):
    '''Computes the partition function until the number of partitions is
    divisible by div.'''
    # count = perf_counter()
    parts = [1]
    pent_vals = [(0, 0)]
    n = 0
    while parts[n] != 0:
        n += 1
        parts.append(0)
        for k in range(1, n+1):
            coef = 1 if k % 2 else -1
            if k < len(pent_vals):
                t1, t2 = pent_vals[k]
            else:
                t1, t2 = pentagonal(k), pentagonal(-k)
                pent_vals.append((t1, t2))
            if t1 > n:
                break

            # No more elements will be less than
            parts[n] += coef * parts[n-t1]
            if t2 > n:
                break
            parts[n] += coef * parts[n-t2]

        parts[n] %= div
    return n


if __name__ == '__main__':
    DIV = 1000000
    MAX_N = 10000
    start = perf_counter()
    print(compute_partitions_div_v2(DIV))  # 55374, 1.701s
    print(f'Calculation completed in {perf_counter()-start} seconds')
