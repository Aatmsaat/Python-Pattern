#how to print the following pattern of any size

'''
size: 10
         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*                 *
 *               *
  *             *
   *           *
    *         *
     *       *
      *     *
       *   *
        * *
         *
'''

#to define size of pattern
n = int(input('Enter the size: '))

#Increasing decreasing parameter
a = 0
b = 2*n-2
c = d = n-1

#pattern
pat = '*'

#printing pattern

#1st A pattern
for i in range(n-1):
	for j in range(2*n-1):
		print(pat if j in (c, d) else ' ', end= '')
	c+=1; d-=1
	print()
	
#2nd V pattern
for i in range(n):
	for j in range(2*n-1):
		print(pat if j in (a, b) else ' ', end= '')
	a+=1; b-=1
	print()