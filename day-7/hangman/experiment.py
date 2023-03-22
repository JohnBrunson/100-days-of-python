# module imports
import os
import random
import logging
import hangmanart
import hangman_words
from time import sleep

# TO DO List
# Fix logging
# Clear screen after every guess -- Done 3/21/2023
# If the user has already guessed a letter that is already guessed and has been determined to not be in the word, don't penalize the user again.
# Give user opportunity to start the game again
# Give user opportunity to append the list of words. (User input list?)
# SFX?
# Categories?
# Scoring system?

# screen clearing function


def screen_clear():
    # for Mac/Linux
    if os.name == 'posix':
        _ = os.system('clear')
    # for Windows
    else:
        _ = os.system('cls')


# initialization
lives = 6
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
logging.info(f'Chosen word is: {chosen_word}')
display = []
guessed_letters = []
word_length = len(chosen_word)
end_of_game = False

# Extra Credit -- logging
logging.basicConfig(filename='hangman.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
screen_clear()
print(hangmanart.logo)
# display the blanks to the user
for _ in range(word_length):
    display += "_"
print(display)

# Easier Debugging, remove when done.
print(f"The chosen word is {chosen_word}")

# prompt the user for a guess
while not end_of_game:
    print(hangmanart.stages[lives])
    guess = input('Enter a letter: ').lower()

    logging.info(f'User input for guess was {guess}')
    # Check if the guess was already made previously
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        sleep(3)
    else:
        guessed_letters.append(guess)
        print(f'Guessed letters are: {guessed_letters}')
        logging.info(f'{guess} was appended to guessed letters')
# evaluate guess and display result to user
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  #  screen_clear()
    print(display)

    if guess not in chosen_word:
        print(
            f"There is no {guess} in this word. You have {lives} attempts remaining.")
    # Why isn't this working?
    if guess not in guessed_letters:
        print(f'guessed letters are: {guessed_letters}')
        lives -= 1

    if lives == 0:
        print(hangmanart.stages[lives])
        end_of_game = True
        print("Sorry! You lose!")

    if "_" not in display:
        end_of_game = True
        print("You win!")
