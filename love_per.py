#love percentage b/w couples

#importing modules
import random as r
import time as t
import os

#Enter lovers
c1 = input('Enter 1st couple: ')
c2 = input('Enter 2nd couple: ')

#heart connecting
for i in range(1, 15):
	print('heart connecting '+'.'*i, end = '', flush=True)
	t.sleep(.1)
	os.system('clear')

#Now printing love percentage
print('There is {} % love between {} & {}'.format(r.randint(1, 100), c1, c2))