#how to print Swastik pattern of any size

'''
Enter the size: 7
*               *
 *             *
  *     *******
  *     *
  *     *
  *     *
  *     *
  *     *
  *************
        *     *
        *     *
        *     *
        *     *
        *     *
  *******     *
 *             *
*               *

[Program finished]
'''

#taking input
n = int(input('Enter the size: '))+5

#parameters
n += int(n%2==0) #correcting even
df = n//5 #division factor
n += 2*df #correcting df
mid = n//2 #middle
l = n-df-1 #last
pat = '*' #pattern

for i in range(n):
	for j in range(n):
		if ((i>l or i<df) and (i==j or (i+j)==(n-1))) or ((df<=j<=l) and (i==mid)) or ((df<=i<=l) and (j==mid)) or ((i==df) and (mid<=j<=l)) or ((i==l) and (df<=j<=mid)) or ((j==df) and (df<=i<=mid)) or ((j==l) and (mid<=i<=l)):
			print('*', end='')
		else: print(' ', end='')
	print()