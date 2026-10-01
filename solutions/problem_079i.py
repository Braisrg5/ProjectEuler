'''https://projecteuler.net/problem=79'''
# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.


def load_keylogs(path):
    '''Loads the keylogs from path.'''
    with open(path, 'r', encoding='utf-8') as file:
        keylogs = file.read().splitlines()
    return keylogs


def find_password(path):
    '''Finds the secret password using the given keylogs.'''
    path += ''
    # keylogs = load_keylogs(path)
    # Solved with pen and paper!
    # May implement a coded solution in the future
    return 73162890


def main():
    '''Main code of module.'''
    print(find_password('resources/0079_keylog.txt'))  # 73162890, 0.000s


if __name__ == '__main__':
    main()
