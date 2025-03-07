'''https://projecteuler.net/problem=48'''
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
MOD = 10**10


def power_mod1010(n):
    '''Calculates n^n mod 10^10.'''
    val = n
    for _ in range(2, n+1):
        val *= n
        val %= MOD
    return val


def calc_sum_last_ten_digits(bound, builtin=False):
    '''Calculates the last ten digits of the series 1^n +... + bound^bound.'''
    series = 0
    for n in range(1, bound+1):
        if n % 10 != 0:
            if builtin:
                nth = pow(n, n, MOD)  # built-in function
            nth = power_mod1010(n)
            series += nth
            series %= MOD
    return series


if __name__ == '__main__':
    # Compensate for the MOD
    print(calc_sum_last_ten_digits(10)+10**10)  # 10405071317
    print(calc_sum_last_ten_digits(1000))  # 9110846700, 0.04s
