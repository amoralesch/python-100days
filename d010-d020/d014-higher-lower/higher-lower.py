# Higher of Lower

# Create a game from scratch, trying to see if the user can guess
# correctly which celebrity has more or less followers than other.

# Nothing new to learn on this day, but a practice to do something
# on our own.

def valid_input(input):
    input = input.strip()

    return input == 'A' or input == 'B'

import art
import data
import random
import helpers
import os

info = data.data
random.shuffle(info)

slot_1 = info[0]
slot_2 = info[1]
index = 1

score = 0
message = None
continue_game = True
while continue_game:
    print(art.logo)

    if message:
        print(message)

    print(f'Compare A: {slot_1['name']}, {slot_1['description']}, from {slot_1['country']}')
    print(art.vs)
    print(f'Against B: {slot_2['name']}, {slot_2['description']}, from {slot_2['country']}')

    guess = helpers.ask_input("Who has more followers? Type 'A' or 'B': ", valid_input)

    if (guess == 'A' and slot_1['follower_count'] > slot_2['follower_count']) or \
        (guess == 'B' and slot_2['follower_count'] > slot_1['follower_count']):
        score += 1
        message = f"You're right! Current score {score}."

        index +=1

        if index >= len(info):
            message = f"Amazing! You answered all the questions correctly. Final score {score}."
            continue_game = False
        else:
            slot_1 = slot_1 if guess == 'A' else slot_2
            slot_2 = info[index]
    else:
        message = f"Sorry, that's wrong. Final score {score}."
        continue_game = False

    os.system('clear')

print(art.logo)
print(message)
