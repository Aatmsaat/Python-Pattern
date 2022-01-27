#How to print running down snake

#importing time
import time

#size deflection
n = int(input('Enter the size for side movement: '))

#deflection control
a = 0
add = 1

#pattern
pat = '*'

#for infinity
while True:
	if a==n: add = -1
	if a==0:  add = 1
	print(' '*a+pat)
	#movement time
	time.sleep(.05)
	a += add