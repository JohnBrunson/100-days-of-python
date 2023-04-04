# Libraries Imported
import string

# Function to generate the alphabet using ASCII characters.
# def generate_alphabet():
#    alphabet = list(string.ascii_lowercase)
#    return (alphabet)

# I confess, I don't like this solution. But I'm not sure about how to get a better one yet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Global Variables
encrypted_alphabet = []
# UI


def main_menu():
    direction = input('''Select an option: 
    1. Encode
    2. Decode
    3. Exit 
    ''')
    if direction == '1':
        text = input('Enter the message: ').lower()
        shift = int(input("Enter the shift number: "))
        encrypt(plain_text=text, shift_amount=shift)
    if direction == '2':
        text = input('Enter the message: ').lower()
        shift = int(input("Enter the shift number: "))
        decrypt(cipher_text=text, shift_amount=shift)
    if direction == '3':
        quit()


def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        # get the letter shifted by the shift number
        encrypted_letter = (shift_amount + (alphabet.index(letter)))
        # append the letter to the encrypted alphabet
        encrypted_alphabet.append(alphabet[int(encrypted_letter)])
        # take the list and join into one string
        encrypted_text = ''.join(encrypted_alphabet)
    print(encrypted_text)


def decrypt(cipher_text, shift_amount):
    for letter in cipher_text:
        # get the letter shifted by the shift number
        encrypted_letter = ((alphabet.index(letter)) - 5)
        # append the letter to the encrypted alphabet
        encrypted_alphabet.append(alphabet[int(encrypted_letter)])
        # take the list and join into one string
        encrypted_text = ''.join(encrypted_alphabet)
    print(encrypted_text)
    encrypted_text = ''


main_menu()
