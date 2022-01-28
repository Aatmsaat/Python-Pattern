#How to print right triangle pattern in one line

#break down Explaination

'''
size: 6
*
**
***
****
*****
******
'''

#first input
n = int(input('Enter size: '))

#generator for pattern in each line
g = ('*'*i for i in range(1, n+1))

#Now print using seperator of new line '\n'
print(*g, sep='\n')