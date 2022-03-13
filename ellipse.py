#ellipse
#Equation :- [ (y-h)^2/a^2 + (x-k)^2/b^2 = 1]

a = int(input('Enter Major axis(a) : '))
b = int(input('Enter Minor axis(b) : '))

#Let Centers be Major & Minor parameter
h = a;  k = b

for x in range(2*b+1):
	for y in range(2*a+1):
		symbol = ' '
		#using equation
		if .9<(y-h)**2/a**2 + (x-k)**2/b**2<=1:
			symbol = '*'
		print(symbol, end='')
	print()
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1