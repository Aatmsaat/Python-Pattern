#playing rock paper scissors against AI

#importing modules
from random import randint

#paramters
signs = {"rock": u"\U0001F44A", "paper": u"\u270B\uFE0F", "scissors": u"\u270C\uFE0F"}
names = ["rock", "paper", "scissors"]
ai = you = 0

#series game of 3 play
for _ in range(3):
	
	#taking answers from ai and player
	your_ans = int(input('Choose\n1 for {0}\n2 for {1}\n3 for {2}\n\n'.format(signs['rock'], signs['paper'], signs['scissors'] )))-1
	ai_ans = randint(0, 2)
	
	#checking who won
	if ai_ans==your_ans:
		print('\nDraw')
	elif (your_ans==0 and ai_ans==1) or (your_ans==1 and ai_ans==2) or (your_ans==2 and ai_ans==0):
		print('\nAI won this round')
		ai += 1
	else:
		print('\nYOU won this round')
		you += 1
	
	#printing this round and score
	print('\nYOU\t\tAI\n{}\t\t{}\n{}\t\t{}\n'.format(signs[names[your_ans]], signs[names[ai_ans]], you, ai))

#final score of series
if ai==you:
	print('Series Draw')
elif you>ai:
	print('You won the series')
else:
	print('AI won the series')