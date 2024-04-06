#initially, randomly distribute two cards each to house and player 
#if over 21, lose | if tie, house win | greater point wins otherwise
#house has less than 16 points, add one card
#player gets two cards, reveal
#ask player if want another card
#

import random 
card = ['A',
         2,
 #        3,
 #        4,
 #        5,
 #        6,
 #        7,
 #        8,
 #        9,
 #       10,
 #      'J',
 #      'Q',
       'K']
    
house_hand = []
player_hand = []
#random.shuffle(card)

house_hand.append(random.choice(card))
player_hand.append(random.choice(card))
house_hand.append(random.choice(card))
player_hand.append(random.choice(card))
#print(house_hand)
#print(player_hand)
#print(player_hand[0])

house_value = 0
player_value = 0

def Card_Value(card):
    if card == 'A':
        value = 11
    elif card == 'J' or card == 'Q' or card == 'K':
        value = 10
    else:
        value = card
    return value

def YesOrNo(user_choice):
    return user_choice.lower() == "yes" or user_choice.lower() == "no"

def AddCard(user_input, verify_input, invalid_input):
    additional_card = input(user_input)
    
    while not verify_input(additional_card):
        print(invalid_input)
        additional_card = input(user_input)
    return additional_card

def AceValue(user_hand, user_card_value):
    if ('A' in user_hand) and (user_card_value > 21):
        user_card_value -= 10
    return user_card_value

#print(house_hand[len(house_hand)-1])
house_value = Card_Value(house_hand[0]) + Card_Value(house_hand[len(house_hand)-1])
player_value = Card_Value(player_hand[0]) + Card_Value(player_hand[len(player_hand)-1])
player_value = AceValue(player_hand, player_value)
house_value = AceValue(house_hand, house_value)
#print(f"House: {house_hand} | {house_value}")
print(f"Player: {player_hand} | {player_value}")
   
while (player_value < 21):
    adding_card = AddCard("Do you want another card? 'yes' or 'no'\n", YesOrNo, "Invalid input, please try again.")
    player_hand.append(random.choice(card))
    player_value = player_value + Card_Value(player_hand[len(player_hand)-1])
    if player_hand[len(player_hand)-1] == 'A' and player_value > 21:
        player_value -= 10
    if player_value < 21:
        adding_card = adding_card.lower() == 'yes' 
    else:
        break
    print(f"player_hand:{player_hand} | {player_value}")
    
while (house_value <= 16):
    house_hand.append(random.choice(card))
    house_value += Card_Value(house_hand[len(house_hand)-1])
    if house_hand[len(house_hand)-1] == 'A' and house_value > 21:
        house_value -= 10
    print(f"House: {house_hand} | {house_value}")

    
    
    
print("-------------Game result-------------------")
if house_value == 21:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("House wins")
elif player_value == 21:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("Player wins")
elif player_value > 21:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("Player bust. House wins") 
elif house_value > 21:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("House bust. Player wins")
elif house_value == player_value:
    print("Game tie.")
elif house_value > player_value:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("House wins.")
else:
    print(f"House has {house_hand} of {house_value} points")
    print(f"Player has {player_hand} of {player_value} points")
    print("Player wins.")