'''https://projecteuler.net/problem=40
An irrational decimal fraction is created by concatenating the positive
integers:

            0.123456789101112131415161718192021...

It can be seen that the 12^th digit of the fractional part is 1.

If d[n] represents the n^th digit of the fractional part, find the value
of the following expression.

            d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]

¿Cuál es el índice del primer dígito del número 10?
D = 9*1 = 9

¿Cuál es el índice del primer dígito del número 100?
D = 9*1 + (99-10+1)*2 = 189

¿Cuál es el índice del primer dígito del número 1000?
D = 9*1 + (99-10+1)*2 + (999-100+1)*3 + 1 = 2889

¿Cuál es el índice del primer dígito del número 10^x?
D = 9*1 + 9*10*2 + 9*100*3 + ... + 9*10^(x-1)*x =
= sum(9*10^(i-1)*i for i in range(1, x+1))
'''
from math import prod


def calc_start(nth):
    '''Calculates the index for the first power of 10 that is less than n
    '''
    index, exp = 0, 1
    while True:
        new_index = index + 9*10**(exp-1)*exp
        if new_index >= nth:
            break
        exp += 1
        index = new_index
    digits = exp
    return index, digits


def find_digit(nth):
    '''Finds the nth digit in the decimal fraction 0.12345678910111213141516...
    '''
    nth -= 1  # Adjust for 0-based indexing
    start, digits = calc_start(nth)
    current_num = 10**(digits-1)
    current_index = start
    while current_index <= nth:
        current_index += digits
        current_num += 1
    diff = nth - (current_index - digits)
    digit = str(current_num - 1)[diff]
    return int(digit)


def digit_prod():
    '''Calculates the value of the expression d[1] * d[10] * ... * d[1000000]
    '''
    return prod(find_digit(10**i) for i in range(7))


if __name__ == '__main__':
    print(digit_prod())  # 210, 0.005
