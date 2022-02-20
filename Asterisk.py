#asterisk of any size

size = int(input('Enter the size: '))
half = size//2

for i in range(size):
	for j in range(size):
		symbol = ' '
		
		#cross
		if (i+j == size-1) or (i==j):
			symbol = '*'
		
		#plus
		if half in (i, j):
			symbol = '*'
		
		print(symbol, end='')
	print()