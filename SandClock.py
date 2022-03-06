#Sand Clock Mini Project

from time import sleep
from os import system
from math import ceil, sqrt

seconds = int(input('Enter seconds: '))

def print_glass(size, tot, seconds_up, seconds_down):
	width = 2*size
	count_up = count_down = 0
	print('_'*width)
	for i in range(1, 2*size+1):
		diag1 = diag2 = 2*size+1
		for j in range(1, 2*size+1):
			symbol = ' '
			
			#left diagonal
			if i==j:
				symbol, diag1 = '\\', j
			
			#right diagonal
			elif i+j == 2*size+1:
				symbol, diag2 = '/', j
				
			#sand	
			elif diag1<j<diag2:
				count_up += 1
				if count_up>(tot-seconds_up):
					symbol = '*'
			elif diag2<j<diag1:
				count_down += 1
				if count_down>(tot-seconds_down):
					symbol = '*'
					
			print(symbol, end = '')
		print()
	print('_'*width)
	return count_up

#calculating size and total space
size = ceil(sqrt(seconds))+1
total = print_glass(size, 3*size, seconds, 8)
system('clear')

#updating sand clock
for sec in range(seconds):
	print_glass(size, total, seconds-sec, sec)
	sleep(1)
	system('clear')
print_glass(size, total, 0, seconds)
#Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1
