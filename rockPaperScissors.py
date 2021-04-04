# Rock, Paper, Scissors Game!
from random import randint

rock = '🪨'
paper = '📄'
scissors = '✂️'

print('\nWelcome to the 🪨, 📄, ✂️  game!')
player = input('\nChoose 🪨, 📄 or ✂️ ? ').capitalize()
random_number = randint(0,2)

if player == 'Rock':
	player = rock
elif player == 'Paper':
	player = paper
else: 
	player = scissors
print(f'\nPlayer chose {player}')

if random_number == 0:
	computer = rock
elif random_number == 1:
	computer = paper
else: 
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
