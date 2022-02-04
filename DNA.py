#How to print DNA

#importing time
import time

#taking the size
size = int(input('Enter the size for dna strand '))

#for infinity
while True:
	for i in range(size):
		for j in range(size):
			symbol = ' '
			
			#one strand
			if i==j or (size-1) in (i+j, i):
				symbol = '*'
				
			print(symbol, end = '')
		time.sleep(.05)
		print()