#how to print following pattern in one line

'''
size: 20
              *
             * *
            *   *
           *     *
          *       *
*****************************
 *      *           *      *
  *    *             *    *
   *  *               *  *
    **                 **
    **                 **
   *  *               *  *
  *    *             *    *
 *      *           *      *
*****************************
          *       *
           *     *
            *   *
             * *
              *
'''
#Taking size of star
n = int(input('Enter the size of star: '))+8

#pattern
pat = '*'

#one fourth / quad
h = n//4

#parameters
up = n-h-1

#printing pattern
for i in  range(n):
	for j in range(2*up+1):
		print('*' if (i in (h, up)) or ((i+j) in (up, up+n-1)) or ((j-i) in (up, -h)) else ' ' , end='')
	print()
