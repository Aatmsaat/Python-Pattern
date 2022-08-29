#Space ship
from os import system
from time import sleep as speed

#Dimensions
height = 9
width = 5
position = height

while True:
	if position==-1:
		position = height
	
	#bullet
	bullet = ' '*width+'*'
	for i in range(height+1):
		if position == i:
			print(bullet)
		else:
			print()
	
	#space ship
	size = width
	while size:
		print(' '*size+'*'+' '*(2*width-2*size)+'*')
		size -= 1
	
	#updating
	speed(.1)
	position -= 1
	system('cls') #'clear' for linux & 'cls' for windows