#how to print the flower of any size

#Taking the size
size = int(input('Enter the size : '))

#check circle using formula
circle = lambda center, axis, radius: round(((axis[0] - center[0])**2 + (axis[1] - center[1])**2)**.5) == radius

#printing flower
for y in range(4*size+1):
	for x in range(4*size+1):
		symbol = ' '
		
		TOP = circle([2*size, size], [x, y], size) and y<=size
		
		BOTTOM = circle([2*size, 3*size], [x, y], size) and y>=3*size
		
		LEFT = circle([size, 2*size], [x, y], size) and x<=size
		
		RIGHT = circle([3*size, 2*size], [x, y], size) and x>=3*size
		
		if  TOP or BOTTOM or LEFT or RIGHT:
			symbol = '*'
			
		print(symbol, end='')
	print()