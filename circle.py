#how to print a circle of any size

#Taking size
n = int(input('Entet the size : '))

#parameters
h = k = n-1 #centers
r = n-1 #radius

#printing circle using formula
for y in range(2*n):
	for x in range(2*n):
		if r == round(((x-h)**2 + (y-k)**2)**.5):
			print('*', end='')
		else:
			print(' ', end='')
	print()