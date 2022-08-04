#bit of a work in progress, but I'll stop here for the night. The example code I think can be simplified more (e.g. use choice as opposed to retrieving from a list, etc.) This doesn't feel very "pythonic"
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for letter in range (0, nr_letters):
  retriever = random.randint(0, len(letters)-1)
  password += letters[retriever]
for number in range (0, nr_numbers):
  retriever = random.randint(0, len(numbers)-1)
  password += numbers[retriever]
for symbol in range (0, nr_symbols):
  retriever = random.randint(0, len(symbols)-1)
  password += symbols[retriever]

print("Easy level Generated password: " + password)
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#password = ""
#randomized_password = ""
r_password = list(password)
random.shuffle(r_password)
password = ''.join(r_password)



print("Hard level Generated password: " + password)

#counter = 0
# while counter != len(r_password):
#   for char in range (0, len(password)):
#     retriever = random.randint (0, len(password)-1)
#     randomized_password += r_password.pop(retriever-1)
#     counter+=1
#could possibly also use push/pop here and that might be simpler.