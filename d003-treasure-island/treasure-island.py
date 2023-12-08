# Treasure Island

# Learn about conditional statements: if, if-else, and if-elif-else

print(r'''
         ____...------------...____
    _.-"` /o/__ ____ __ __  __ \o\_`"-._
  .'     / /                    \ \     '.
  |=====/o/======================\o\=====|
  |____/_/________..____..________\_\____|
  /   _/ \_     <_o#\__/#o_>     _/ \_   \
  \_________       \####/       _________/
   |===\!/========================\!/===|
   |   |=|          .---.         |=|   |
   |===|o|=========/     \========|o|===|
   |   | |         \() ()/        | |   |
   |===|o|======{'-.) A (.-'}=====|o|===|
   | __/ \__     '-.\uuu/.-'    __/ \__ |
   |====          .'.'^'.'.         ====|
   |  _\o/   __  {.' __  '.} _   _\o/  _|
   `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a cross road. Where do you want to go?" +
    "Type 'left' or 'right'\n").lower()

if direction == 'left':
    action = input("You come to a lake. There is an island in the " +
        "middle of the lake. Type 'wait' to wait for the boat. Type " +
        "'swim' to swim across.\n").lower()

    if action == 'wait':
        door = input("You arrive at the island unharmed. There is a " +
            "house with 3 doors. One red, one yellow and one blue. " +
            "Which color do you choose?\n").lower()

        if door == 'red':
            print("You are burned by fire. Game Over.")
        elif door == 'blue':
            print("You are eaten by beasts. Game Over.")
        elif door == 'yellow':
            print("You found the treasure. You Win!")
        else:
            print("A witch cursed you. Game Over.")
    else:
        print('You are attacked by a trout. Game Over.')
else:
    print("You fell into a hole. Game Over.")
