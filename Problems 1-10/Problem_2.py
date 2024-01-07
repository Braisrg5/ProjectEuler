def sumEvenFibonacci(n):
    '''Sums the even numbers in the Fibonacci sequence up to n.
    '''
    a0, a1 = 1, 1
    suma = 0
    while a1 <= n:
        if a1 % 2 == 0:
            suma += a1
        a0, a1 = a1, a0 + a1
    return suma


if __name__ == "__main__":
    print(sumEvenFibonacci(10)) # 10
    print(sumEvenFibonacci(34)) # 44
    print(sumEvenFibonacci(4000000))