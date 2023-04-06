# Libraries Imported
import string
import art

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
        # accounts for numbers larger than 26.
        shift = shift % 26
        # encrypt(plain_text=text, shift_amount=shift)
        caesar(input_text=text, shift_amount=shift, direction=cipher_direction)
    elif cipher_direction == '2':
        text = input('Enter the message: ').lower()
        shift = int(input("Enter the shift number: "))
        # accounts for numbers larger than 26.
        shift = shift % 26
        caesar(input_text=text, shift_amount=shift, direction=cipher_direction)
    elif cipher_direction == '3':
        quit()
    else:
        print("That is an invalid selection. Please try again.")
        main_menu()


def caesar(input_text, shift_amount, direction):
    print('Please note, all input will be converted to lower case. All non alphabetic input will not be encoded.')
    calculated_alphabet = ''
    for letter in input_text:
        if letter not in alphabet:
            calculated_alphabet += letter
        # get the letter shifted by the shift number
        elif direction == '1' and letter in alphabet:
            calculated_letter = (shift_amount + (alphabet.index(letter)))
            calculated_alphabet += (alphabet[int(calculated_letter)])
        elif direction == '2' and letter in alphabet:
            calculated_letter = ((alphabet.index(letter)) - shift_amount)
            calculated_alphabet += (alphabet[int(calculated_letter)])

    if direction == '1':
        print(f'The encoded text is: {calculated_alphabet}')
    elif direction == '2':
        print(f'The decoded text is: {calculated_alphabet}')
    # cleanup
    calculated_letter = ''
    calculated_alphabet = ''
    # restart the program?
    cipher_restart()


def cipher_restart():
    answer = input(
        "Do you want to restart the cipher program (y or n)?").lower()
    if answer == 'y':
        main_menu()
    elif answer == 'n':
        print('Thank you for using Caesar Cipher!')
        quit()
    else:
        print('You have used invalid input. Please try again.')
        cipher_restart()


print(art.logo)
main_menu()
