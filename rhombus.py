#super easy rhombus pattern of any size

#Taking size
size = int(input('Enter the size: '))

#printing rhombus
for y in range(size):
	for x in range(2*size-1):
		symbol = ' '
		
		#Top & Bottom line respectively
		if (y==0 and x>=size-1) or (y==size-1 and x<=size-1):
			symbol = '*'
		
		#diags, left=size-1, right=2*(size-1)
		if x+y in (size-1, 2*(size-1)):
			symbol = '*'
		
		print(symbol, end='')
	print()