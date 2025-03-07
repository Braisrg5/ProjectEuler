'''https://projecteuler.net/problem=22'''
# Using 22_names.txt, a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a name score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?


def load_names(path):
    '''Loads the names from path into a list.'''
    with open(path, 'r', encoding='utf-8') as file:
        names = file.read().split(',')
    names = [name.strip('"') for name in names]  # Remove quotes
    return names


def alphabetic_score_v2(name):
    '''Returns the alphabetic score of a name.'''
    # ord function is faster
    return sum(ord(letter)-64 for letter in name)


def total_name_score_v2():
    '''Returns the total score of all the names in the file.'''
    names = load_names('resources/22_names.txt')
    i, s = 1, 0
    for name in sorted(names):
        s += i*alphabetic_score_v2(name)
        i += 1
    return s


if __name__ == '__main__':
    print(alphabetic_score_v2('COLIN'))  # 53
    print(total_name_score_v2())  # 871198282, 0.009s
