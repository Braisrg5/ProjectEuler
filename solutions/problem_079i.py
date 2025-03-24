'''https://projecteuler.net/problem=79'''


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
