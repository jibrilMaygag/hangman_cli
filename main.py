import random
import os
#for clearing the terminal
def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS/Linux
    else:
        os.system('clear')

from hungman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
from hungman_art import logo,stages
print(logo)
##Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear_console()

    if guess in display:
        print(f"you've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You gussed {guess}, that's not in the word. You lose a life. ")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])