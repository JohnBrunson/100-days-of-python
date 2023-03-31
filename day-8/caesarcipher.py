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
# UI


def main_menu():
    direction = input('''Select an option: 
    1. Encode
    2. Decode
    3. Exit 
    ''')
    if direction == 1:
        text_functions()
        encrypt()
    if direction == 2:
        print("This function doesn't work yet.")
        main_menu()
    if direction == 3:
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


# Global Varibles
text = input('Enter the message: ').lower()
shift = int(input("Enter the shift number: "))
encrypted_alphabet = []
encrypt(plain_text=text, shift_amount=shift)
# Functions


# print(encrypted_alphabet)
# def encrypt(text, shift):
#    encrypted.alphabet = ""


# Temporary main


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
