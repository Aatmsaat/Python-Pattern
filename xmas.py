#x mas tree of any size

#Taking the size
size = int(input('Enter the size :- '))

#parameters
size += size%2==0 #change even to odd
half = size//2
quad = half//2

#print the tree
for i in range(size+quad):
	for j in range(size):
		symbol = ' '
		
		#Crown = 3 Triangles
		if (i+j==half or j-i==half or i==half) or (i>=half and (i+j==half+quad or j-i==half-quad or i==half+quad)) or (i>=half+quad and (i+j==2*half or j-i==0 or i==size-1)):
			symbol = '*'
			
		#Trunk = 1 vertical rectangle
		if (i>=size and j in [quad, quad+half]) or (quad<=j<=quad+half and i==size+quad-1):
			symbol = '*'
			
		print(symbol, end = '')
	print()