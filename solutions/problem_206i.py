'''https://projecteuler.net/problem=206'''


def find_number_v2():
    '''Finds the only number that is a square and has the form
    1_2_3_4_5_6_7_8_9_0.'''

    possible_numbers = [0]

    for k in range(1, 5):
        new_possible_numbers = []
        for possible in possible_numbers:
            for i in range(100):
                num = i*10**(2*k - 1) + possible
                square = num*num % 10**(2*k + 1)
                if square // 10**(2*k) == 9 - k + 1:
                    new_possible_numbers.append(num)
        possible_numbers = new_possible_numbers

    for possible in possible_numbers:
        for i in range(10):
            num = i*10**9 + possible
            square = num*num
            if (square % 10**11 // 10**10 == 5
                    and square % 10**13 // 10**12 == 4
                    and square % 10**15 // 10**14 == 3
                    and square % 10**17 // 10**16 == 2
                    and square % 10**19 // 10**18 == 1):
                return num

    return -1


def main():
    '''Main code of module.'''
    print(find_number_v2())  # 1389019170, 0.104s


if __name__ == '__main__':
    main()
