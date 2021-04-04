# Rock, Paper, Scissors Game!
from random import randint

rock = '🪨'
paper = '📄'
scissors = '✂️'
no_response = 'no response'
unable_to_play = 'no item since player didn\'t chose either'

print('\nWelcome to the 🪨, 📄, ✂️  game!')
player = input('\nChoose 🪨, 📄 or ✂️ ? ').capitalize()
random_number = randint(0,2)

if player == 'Rock':
	player = rock
elif player == 'Paper':
	player = paper
elif player == 'Scissors':
	player = scissors
elif player != 'Rock' or 'Paper' or 'Scissors':
	player = no_response
print(f'\nPlayer chose {player}')

if random_number == 0 or random_number == 1 or random_number == 2 and player != 'Rock' or 'Paper' or 'Scissors':
	computer = unable_to_play
elif random_number == 0:
	computer = rock
elif random_number == 1:
	computer = paper
elif random_number == 2:
	computer = scissors

print(f'Computer chose {computer}\n')

if player == computer:
	print('It\'s a tie\n')
elif player == rock:
	if computer == paper:
		print('Player wins!\n')
	else:
		print('Computer wins!\n')
elif player == paper:
	if computer == rock:
		print('Player wins!\n')
	else:
		print('Computer wins!\n')
elif player == scissors:
	if computer == paper:
		print('Player wins!\n')
	else:
		print('Computer wins!\n')
else:
	print('Please write a valid item\n')
