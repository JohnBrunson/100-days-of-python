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
calculated_alphabet = []
# UI


def main_menu():
    cipher_direction = input('''Select an option: 
    1. Encode
    2. Decode
    3. Exit 
    ''')
    if cipher_direction == '1':
        text = input('Enter the message: ').lower()
        shift = int(input("Enter the shift number: "))
        # encrypt(plain_text=text, shift_amount=shift)
        caesar(input_text=text, shift_amount=shift, direction=cipher_direction)
    if cipher_direction == '2':
        text = input('Enter the message: ').lower()
        shift = int(input("Enter the shift number: "))
        # decrypt(cipher_text=text, shift_amount=shift)
        caesar(input_text=text, shift_amount=shift, direction=cipher_direction)
    if cipher_direction == '3':
        quit()


def caesar(input_text, shift_amount, direction):
    for letter in input_text:
        # get the letter shifted by the shift number
        if direction == '1':
            calculated_letter = (shift_amount + (alphabet.index(letter)))
        elif direction == '2':
            calculated_letter = ((alphabet.index(letter)) - shift_amount)
        # append the letter to the encrypted alphabet
        calculated_alphabet.append(alphabet[int(calculated_letter)])
        # take the list and join into one string
        calculated_text = ''.join(calculated_alphabet)
    if direction == '1':
        print(f'The encoded text is: {calculated_text}')
    elif direction == '2':
        print(f'The decoded text is: {calculated_text}')


main_menu()
