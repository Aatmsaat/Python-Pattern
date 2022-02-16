#hyperbola using formula

#Taking input
size = int(input('Enter the size: '))

for y in range(2*size+1):
	for x in range(2*size+1):
		symbol = ' '
		
		#check forumla
		if round(((x-size)**2)/size - ((y-size)**2)/size) == 1:
			symbol = '*'
			
		print(symbol, end='')
	print()