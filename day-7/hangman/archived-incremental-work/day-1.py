import random
import logging

word_list = ['aardvark', 'baboon', 'camel']
# Extra Credit -- logging
logging.basicConfig(filename='hangman.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# TODO -- Make all words lower case, just in case the dev does something stupid.
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# random_int = random.randint(0, len(word_list))
# logging.info(f'Random Integer Chosen was {random_int}')
# chosen_word = word_list[random_int - 1]
# logging.info(f'Random word chosen was {chosen_word}')

# A Better Solution
chosen_word = random.choice(word_list)
logging.info(f'Chosen word is: {chosen_word}')


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Enter a letter: ').lower()
# guess = guess.lower()
logging.info(f'User input for guess was {guess}')

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO: Move this to logs later.

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')
