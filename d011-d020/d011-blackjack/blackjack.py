# Blackjack

# Create the game of blackjack:
# - randomly distribute two cards, to both house and player
# - if over 21, lose | if game is tie, house win | otherwise, greater point wins
# - player gets two open cards, then decide if he wants more
# - if the house has less than 16 points, add more cards
#
# - practice about Random function
# - A list is capable to hold both integers and string values

import random


def card_value(card):
    if card == 'A':
        value = 11
    elif card == 'J' or card == 'Q' or card == 'K':
        value = 10
    else:
        value = card

    return value


def yes_or_no(user_choice):
    return user_choice.lower() == "yes" or user_choice.lower() == "no"


def add_card(user_input, verify_input, invalid_input):
    additional_card = input(user_input)

    while not verify_input(additional_card):
        print(invalid_input)
        additional_card = input(user_input)

    return additional_card


def total_value(card_hand):
    sum_value = 0
    ace_count = 0

    for card in card_hand:
        sum_value += card_value(card)

        if card == 'A':
            ace_count += 1

    while ace_count > 0 and sum_value > 21:
        sum_value -= 10
        ace_count -= 1

    return sum_value


CARDS = [
    2, 3, 4, 5, 6, 7, 8, 9, 10,
    'J', 'Q', 'K', 'A'
]

house_hand = []
player_hand = []

house_hand.append(random.choice(CARDS))
player_hand.append(random.choice(CARDS))
house_hand.append(random.choice(CARDS))
player_hand.append(random.choice(CARDS))

player_value = total_value(player_hand)
house_value = total_value(house_hand)

print(f"Player: {player_hand} | {player_value}")
print(f"House: [{house_hand[0]}, x]")

while player_value < 21:
    adding_card = add_card(
        "Do you want another card? 'yes' or 'no'\n",
        yes_or_no,
        "Invalid input, please try again.")

    if adding_card == adding_card.lower() == 'yes':
        player_hand.append(random.choice(CARDS))
        player_value = total_value(player_hand)
    else:
        break

    print(f"player_hand:{player_hand} | {player_value}")

while house_value <= 16:
    house_hand.append(random.choice(CARDS))
    house_value = total_value(house_hand)
    print(f"House: {house_hand} | {house_value}")

print("-------------Game result-------------------")
print(f"House has {house_hand} of {house_value} points")
print(f"Player has {player_hand} of {player_value} points")

if house_value == 21:
    print("House wins")
elif player_value == 21:
    print("Player wins")
elif player_value > 21:
    print("Player bust. House wins")
elif house_value > 21:
    print("House bust. Player wins")
elif house_value == player_value:
    print("Game tie.")
elif house_value > player_value:
    print("House wins.")
else:
    print("Player wins.")
