import random

rock = ('''
     ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')

paper = ('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
''')

scissor = ('''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''')

game_images = [rock, paper, scissor]

choice_1 = int(input(
    "What do you choose? Type 0 for rock, 1 for paper or 2 for scissor: "
))

if choice_1 >= 0 and choice_1 <= 2:
    print(game_images[choice_1])

comp_choice = random.randint(0, 2)

print("Computer chose:")
print(game_images[comp_choice])

if choice_1 >= 3 or choice_1 < 0:
    print("You typed an invalid number. You lose.")

elif choice_1 == 0 and comp_choice == 2:
    print("YOU WIN!")

elif comp_choice == 0 and choice_1 == 2:
    print("YOU LOSE!")

elif comp_choice > choice_1:
    print("YOU LOSE!")

elif choice_1 > comp_choice:
    print("YOU WIN!")

elif comp_choice == choice_1:
    print("It's a draw!")
