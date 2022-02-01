#how to print the butterfly with asterisk

#Taking the size
n = int(input('Enter the size : '))

#check circle using formula
circle = lambda center, axis, radius: round(((axis[0] - center[0])**2 + (axis[1] - center[1])**2)**.5) == radius

#printing butterfly
for y in range(4*n+1):
	for x in range(4*n+1):
		symbol = ' '
		
		# antennas
		if y<=n and ((n<=x<=2*n and x-y==n) or (2*n<=x<=4*n and x+y==3*n)):
			symbol = '*'
		
		#head
		if circle([2*n, n], [x, y], n//4):
			symbol = '*'
		
		#wings
		if (n<=x<=3*n) and (n<=y<=3*n) and (circle([2*n, n], [x, y], n) or circle([2*n, 3*n], [x, y], n) or circle([n, 2*n], [x, y], n) or circle([3*n, 2*n], [x, y], n)):
			symbol = '*'
			
		print(symbol, end='')
	print()