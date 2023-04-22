#rock paper scissors

import random


options = ['Rock', 'Paper', 'Scissors']
cHand = []
pHand = []


def computerHand(turn): #random choice from list for computer
    hand = random.choice(options)
    turn.append(hand)
    return hand
computerHand(cHand)


def player(turn):
    playerIn = True
    while playerIn: #loop to make sure input it correct
        playerHand = int(input('1: Rock \n2: Paper\n3: Scissors\n'))

        if playerHand == 1:
            playerHand = options[0]
            playerIn = False
        elif playerHand == 2:
            playerHand = options[1]
            playerIn = False
        elif playerHand == 3:
            playerHand = options[2]
            playerIn = False
        else:
            print('\nInvalid input\nPlease choose numbers 1, 2, or 3\n')
            
    turn.append(playerHand)  
    return playerHand
player(pHand)


print()


if pHand == ['Rock'] and cHand == ['Rock']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print("Tie!")
elif pHand == ['Paper'] and cHand == ['Paper']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print("Tie!")
elif pHand == ['Scissors'] and cHand == ['Scissors']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print("Tie!")
elif pHand == ['Rock'] and cHand == ['Paper']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Lose!')
elif pHand == ['Scissors'] and cHand == ['Rock']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Lose!')
elif pHand == ['Paper'] and cHand == ['Scissors']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Lose!')
elif pHand == ['Scissors'] and cHand == ['Paper']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Win!')
elif pHand == ['Rock'] and cHand == ['Scissors']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Win!')
elif pHand == ['Paper'] and cHand == ['Rock']:
    print(f'You chose {pHand}\nComputer chose {cHand}\n')
    print('You Win!')
else:
    print('error')
