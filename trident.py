#how to draw trident

size = int(input('Enter the size: '))
half = size//2
forty = int(size*.4)

for i in range(size):
	for j in range(size):
		symbol = ' '
		
		#3 spears
		if j == half or (i<=forty and (i==forty or j in (0, size-1))):
			symbol = '*'

		print(symbol, end='')
	print()