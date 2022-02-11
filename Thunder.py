#Thunder lightning in python

#importing modules
from time import sleep

size = int(input('Enter the size: '))
stripe_num = int(input('Enter the number of stripes: '))
decr = size

while True:
	print(' '*decr+'*'+('  '*size+'*')*(stripe_num-1))
	if decr==1:
		decr=size
		print(('*'*size+' '+' '*size)*stripe_num)
	sleep(.05)
	decr -= 1