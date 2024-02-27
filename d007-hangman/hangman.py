# Hangman Game

# Use the previous knowledge about for and while loops, if-else
# conditionals, variables, modules, and other things to create a
# simple text game.

import random
from art import images, logo
from word_pool import word_pool

end_of_game = False
display = []
previous_guesses = []
lives = 6

secret_word = random.choice(word_pool)
word_len = len(secret_word)

for _ in secret_word:
    display += '_'

print(logo)

while not end_of_game:
    print(" ".join(display))
    guess = input("Guess a letter: ")

    if guess in previous_guesses:
        print("You used that letter before, try another one.")
        continue

    previous_guesses += guess

    for index in range(word_len):
        if secret_word[index] == guess:
            display[index] = guess

    if guess not in secret_word:
        lives -= 1

    if '_' not in display:
        print(f"You Won! The secret word was {secret_word}")
        end_of_game = True

    print(images[lives])

    if lives <= 0:
        print(f"The secret word was {secret_word}. You lose.")
        end_of_game = True
