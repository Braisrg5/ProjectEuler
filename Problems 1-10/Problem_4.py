def is_palindrome(n):
    '''Checks if a number is a palindrome
    '''
    return n == int(str(n)[::-1])

def palindromes():
    '''Returns the largest palindromic number that is a product of two 3-digit 
    numbers.
    '''
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, i-1, -1):
            large = i*j
            if is_palindrome(large) and large > largest:
                largest = large
    return largest
    # One-liner alternative solution
    '''return max([i*j for i in range(999, 100, -1) 
                       for j in range(999, i-1, -1) 
                       if is_palindrome(i*j)])'''


if __name__ == '__main__':
    print(palindromes())