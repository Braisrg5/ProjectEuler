'''https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words?


Como tn = ½n(n+1), entonces n = (-1 + sqrt(1 + 8tn))/2. De hecho, un número es
triangular si y sólo si 8n + 1 es un cuadrado perfecto.
De esta forma, es fácil determinar si una palabra es triangular o no.
'''
from resources.useful_functions import is_triangle


def load_words(path):
    '''Loads a list of words from a file.
    '''
    f = open(path, 'r')
    text = f.read()
    f.close()
    return [word.replace(''', '') for word in text.split(',')]


def transform_to_num(words):
    '''Transforms a list of words into a list of numbers.
    '''
    nums = []
    for word in words:
        num = 0
        for letter in word:
            num += ord(letter) - 64
        nums.append(num)
    return nums


def sum_triangle_words():
    '''Returns the number of triangle words in the list of words.
    '''
    words = load_words('resources/0042_words.txt')
    nums = transform_to_num(words)
    return sum([is_triangle(num) for num in nums])


if __name__ == '__main__':
    value = transform_to_num(['SKY'])[0]
    print(value)  # 55
    print(is_triangle(value))  # True
    print(sum_triangle_words())  # 162, 0.001s
