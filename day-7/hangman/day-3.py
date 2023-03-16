import random
import logging

# initialization

word_list = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
logging.info(f'Chosen word is: {chosen_word}')
display = []
word_length = len(chosen_word)
end_of_game = False
# Extra Credit -- logging
logging.basicConfig(filename='hangman.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# display the blanks to the user
for _ in range(word_length):
    display += '_'
print(display)

# prompt the user for a guess
# initial answer:
# while '_' in display:
while not end_of_game:
    guess = input('Enter a letter: ').lower()

    logging.info(f'User input for guess was {guess}')

# evaluate guess and display result to user
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")
