#memorise table in python

#importing modules
from threading import Timer
from time import sleep
from random import choice
from os import system

#Taking input 
n = int(input('Enter the no. to practise the table : '))
system('clear')

#parameters
score = 0
table = [*range(1, 11)]
practice_ques = 3 #must be in range 1-10
timeout = 1.5 #control seconds

for i in range(practice_ques):
	print(f'you have {timeout} seconds', flush=True)
	t = Timer(timeout, print, ['\nTimeout, press "Enter" to continue'])
	rand_num = random.choice(table)
	#timer
	t.start()
	inp = input(f'{n}*{rand_num} = ')
	if inp.isdigit() and t.is_alive():
		score += int(inp) == (n*rand_num)	
	t.cancel(); table.remove(rand_num); os.system('clear')

#Result
print('Your score:\t{}/{}\nPercentage:\t{}%'.format(score, practice_ques, score/practice_ques*100))