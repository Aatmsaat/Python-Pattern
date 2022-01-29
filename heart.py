#how to print heart with an arrow of any size

'''
size: 15
       *              *   *****
      * *            * *     **
     *   *          *   *   * *
    *     *        *     * *  *
   *       *      *       *
  *         *    *         *
 *           *  *           *
*             **             *
*                           *
 *                         *
  *                       *
   *                     *
    *                   *
     *                 *
      *               *
       *      *      *
        *    *      *
         *  *      *
          **      *
          **     *
         *  *   *
        *    * *
       *      *

'''

#to define size of pattern
n = int(input('Enter the size: '))

#Increasing decreasing parameter
n+=int(n%2==0)
a = 0
b = 2*n-2
h = n//2 #half
q = h//2 #quad
e = f = h
c = d = n+e

#arrow parameter
tot1 = n+h+q
tot2 = n-1+e

#pattern
pat = '*'

#printing pattern


#1st 2 As pattern
for i in range(e+1):
	for j in range(2*n+1):
		print(pat if (j in (c, d, e, f)) or ((i+j == 2*n) and (j>tot1)) or (i==0 and j>tot1) or (j==2*n and i<=q) else ' ', end= '')
	c+=1; d-=1; e+=1; f-=1
	print()
	
#2nd V pattern
for i in range(n):
	for j in range(2*n-1):
		print(pat if (j in (a, b)) or ((i+j == tot2) and i>=h) else ' ', end= '')
	a+=1; b-=1
	print()