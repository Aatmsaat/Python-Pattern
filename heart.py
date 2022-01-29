#how to print heart with an arrow of any size

'''
Enter the size: 20
Enter 1st couple: alice
Enter 2nd couple: bob



          *                    *     ******
         * *                  * *        **
        *   *                *   *      * *
       *     *              *     *    *  *
      *       *            *       *  *   *
     *         *          *         **    *
    *           *        *           *
   *             *      *             *
  *               *    *               *
 *                 *  *                 *
*                   **                   *
*                                       *
 *             Alice❤️Bob              *
  *                                   *
   *                                 *
    *                               *
     *                             *
      *                           *
       *                         *
        *                       *
         *                     *
          *         *         *
           *       *         *
            *     *         *
             *   *         *
              * *         *
               *         *
              * *       *
             *   *     *
            *     *   *
           *       * *
          *         *

'''

#to define size of pattern
n = int(input('Enter the size: '))
c1= input('Enter 1st couple: ').title()
c2 = input('Enter 2nd couple: ').title()
print('\n'*2)

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

#Couples name
lp = '{}\u2764\uFE0F{}'.format(c1, c2)
l = len(lp)
k = (2*n-1-l)//2
st = 0	

#2nd V pattern
for i in range(n):
	for j in range(2*n-1):
		if (j in (a, b)) or ((i+j == tot2) and i>=h):
			print(pat, end='') 
		elif (l<2*n-2) and i==1 and j>=k and st<l:
			print(lp[st], end='')
			st+=1
		else:
			print(' ', end= '')
	a+=1; b-=1
	print()