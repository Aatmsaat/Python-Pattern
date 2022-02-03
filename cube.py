#cube of any size 

#taking the size
size = int(input('Enter the size: '))

size += size%2==0 #change even to odd
half = size//2

for i in range(size+half):
	for j in range(size+half):
		symbol = ' '
		
		#bottom left square
		if i>=half and ((i in [half, size+half-1] and j<size) or (j in [0, size-1])):
			symbol = '*'
		
		#top right square
		if i<size and j>=half and (i in [0, size-1] or j in [half, half+size-1]):
			symbol = '*'
		
		#upper diagonals
		if i<=half and ((i+j) in [half, size+half-1]):
			symbol = '*'
		
		#lower diagonals
		if (i>=size-1 and ((i+j) in [size+half-1, 2*size+half-2])):
			symbol = '*'
			
		print(symbol, end = '')
	print()