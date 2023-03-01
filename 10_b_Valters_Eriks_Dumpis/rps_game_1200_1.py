import random

turns = ['Rock', 'Paper', 'Scissors']

while(True):
    human_turn = input('Enter your turn, or type exit: ')
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye!❤')
        break

    print(f'Human: {human_turn} vs. Computer: {computer_turn}')

    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'Rock' and computer_turn == 'Scissors':
        print('Human wins!')
    elif human_turn == 'Paper' and computer_turn == 'Rock':
        print('Human wins!')
    elif human_turn == 'Scissors' and computer_turn == 'Paper':
        print('Human wins!')
    else:
        print('Computer wins!')