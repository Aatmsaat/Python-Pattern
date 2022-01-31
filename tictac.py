#tic tac toe against AI

#import modules and globals
from random import choice
from time import sleep
positions = list(' '*9)
lookup = [*range(9)]

#board function 
def PrintBoard():
	print('\n'*2)
	for i in range(0, 7, 3):
		print('\t', positions[i]+'|'+positions[i+1]+'|'+positions[i+2])
		print('\t', '-'*5 if i<6 else '\n'*2, flush=True)

#winner check
def is_win(player):
	return [player]*3 in (positions[:3], positions[3:6], positions[6:9], positions[0:9:3], positions[1:9:3], positions[2:9:3], positions[0:9:4], positions[2:7:2])

you, ai = 'X', 'O'
if int(input('Type 1 for X & 2 for O : ')) == 2:
	you, ai = 'O', 'X'

winner = False
YourTurn = False
while not winner:
	PrintBoard()
	pos = None
	if YourTurn:
		while True:
			pos = int(input('Your Turn : '))-1
			if pos in lookup: break
			print('Already filled')
		positions[pos] = you
		if is_win(you):
			PrintBoard()
			print('You won')
			break
	else:
		pos = choice(lookup)
		print("AI's Turn : {}".format(pos+1))
		sleep(1)
		positions[pos] = ai
		if is_win(you):
			PrintBoard()
			print('AI won')
			break
	lookup.remove(pos)
	if not lookup:
		print('Draw')
		break
	YourTurn = not YourTurn