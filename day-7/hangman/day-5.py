# module imports
import random
import logging
import hangmanart
import hangman_words

# TO DO List
# Clear screen after every guess
# Give user opportunity to start the game again
# Give user opportunity to append the list of words. (User input list?)
# SFX?
# Categories?


# initialization
lives = 6
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
logging.info(f'Chosen word is: {chosen_word}')
display = []
word_length = len(chosen_word)
end_of_game = False

# Extra Credit -- logging
logging.basicConfig(filename='hangman.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

print(hangmanart.logo)
# display the blanks to the user
for _ in range(word_length):
    display += '_'
print(display)
# Easier Debugging, remove when done.
print(f"The chosen word is {chosen_word}")
# prompt the user for a guess
# initial answer:
# while '_' in display:
while not end_of_game:
    print(hangmanart.stages[lives])
    guess = input('Enter a letter: ').lower()

    logging.info(f'User input for guess was {guess}')
    if guess in display:
        print(f"You've already guessed {guess}")
# evaluate guess and display result to user

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(
            f"There is no {guess} in this word. You have {lives} attempts remaining.")

    if lives == 0:
        print(hangmanart.stages[lives])
        end_of_game = True
        print("Sorry! You lose!")

    if "_" not in display:
        end_of_game = True
        print("You win!")
