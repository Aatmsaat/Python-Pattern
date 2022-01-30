#how to print a rectangle

#paramters
length = int(input('Enter the length : '))
breadth = int(input('Enter the breadth : '))
symbol = '*'

for i in range(length):
	for j in range(breadth):
		print(symbol if 0 in (i, j) or i==(length-1) or j==(breadth-1) else ' ', end='')
	print()