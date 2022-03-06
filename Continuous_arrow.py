#Up ward arrow
from time import sleep

size = int(input('Enter the size: '))
space = size

#infinity
while True:
	if space==0:
		space=size
		print('*'*(2*size+2))
	print(' '*space+'*'+' '*(2*size-2*space)+'*')
	sleep(.07)
	space-=1
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1