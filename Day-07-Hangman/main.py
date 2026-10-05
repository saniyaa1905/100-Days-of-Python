import random

from hangman_words import word_list
from hangman_art import logo, stages


print(logo)

chosen_word = random.choice(word_list)

lives = 6
game_over = False
correct_letters = []
guessed_letters = []


# Create the placeholder
placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)


while not game_over:

    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")

    else:
        guessed_letters.append(guess)

        # Check if letter is in the word
        if guess in chosen_word:
            correct_letters.append(guess)

        else:
            lives -= 1
            print("Wrong guess!")
            print(stages[lives])

    # Create display
    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Check win
    if "_" not in display:
        game_over = True
        print("YOU WON!")

    # Check lose
    if lives == 0:
        game_over = True
        print("YOU LOSE!")
        print("The word was:", chosen_word)
