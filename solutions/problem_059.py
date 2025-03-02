'''https://projecteuler.net/problem=59
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using 0059_cipher.txt, a file containing the encrypted ASCII
codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
'''


def load_message(path):
    with open(path, 'r') as file:
        list_ascii = file.read().split(',')
    return [int(i) for i in list_ascii]


# Used for debugging purposes
def encrypt_message(text, password):
    '''Encrypts a text using XOR with a password, returns a list of the
    encrypted ASCII codes.'''
    # Initialize the password index to -1 to start from the first character
    encrypted, pass_index = [], -1
    for letter in text:
        # Cycle through the password
        pass_index = (pass_index + 1) % 3
        # XOR the ASCII code with the current character of the password
        encrypted_code = ord(letter) ^ password[pass_index]
        encrypted.append(encrypted_code)
    return encrypted


def decrypt_message(encrypted_message, password):
    '''Decrypts an encrypted message using XOR with a password, returns the
    decrypted text as a list of ASCII codes.
    https://theasciicode.com.ar/'''
    # Initialize the password index to -1 to start from the first character
    decrypted, pass_index = [], -1
    for encrypted_code in encrypted_message:
        # Cycle through the password
        pass_index = (pass_index + 1) % 3
        # XOR the ASCII code with the current character of the password
        ascii_code = encrypted_code ^ password[pass_index]
        # If the code is not from an expected character, skip the password
        # Codes 31-126 include space, punctuation marks, numbers, symbols and
        # letters. I added ASCII 127 (delete character?), didn't work otherwise
        if ascii_code < 32 or ascii_code > 127:
            return None
        decrypted.append(ascii_code)
    return decrypted


def find_password(path):
    # List of common English words to look for in the decrypted text.
    # Surprisingly, it is enough to consider ' the '. Not including the spaces
    # made the task much more complicated.
    common_words = [' the ']  # , 'be', 'to', 'and'
    # 'have','I', 'it', 'for', 'not', 'on']
    encrypted = load_message(path)
    # ASCII range for lowercase letters (ASCII 97-122)
    rang = range(97, 123)
    # Generate all possible 3-character lowercase passwords
    possible_passwords = [(i, j, k) for i in rang for j in rang for k in rang]
    for password in possible_passwords:
        # Decrypt the message with the current password
        decrypted = decrypt_message(encrypted, password)
        if decrypted:
            decrypted_text = ''.join(chr(c) for c in decrypted)
            # Check if the decrypted text contains common English words
            if all(word in decrypted_text.lower() for word in common_words):
                password_text = ''.join(chr(c) for c in password)
                print(f'A possible password is: {password_text}')
                print('Here is the decrypted text:')
                print('----------------------------------')
                print(decrypted_text)
                print('----------------------------------')
                # Request user confirmation before summing ASCII values
                print('Does this text look readable?')
                answer = input('Press "y" to confirm the password, ' +
                               'press any other key otherwise: ')
                if answer.lower() == 'y':
                    return sum(decrypted)
    # No password found
    return None


if __name__ == '__main__':
    print(find_password('resources/0059_cipher.txt'))  # 129448, 0.74s
