#fibonacci candy

#Taking the size
size = int(input('Enter the size : '))

#Important parameters
series = [1, 1]
center = [0]*size
y_limit = [0]*size
x_limit = [0]*size
x_last = 0
y_last = 0
count = 0

#check circle using formula
circle = lambda center, axis, radius: round(((axis[0] - center[0])**2 + (axis[1] - center[1])**2)**.5) == radius

#Generating fibonacci series
for i in range(size-2):
	series.append(series[-1]+series[-2])

#Generating centers & limits
for i in range(size-1, -1, -1):
	val = series[i]
	if count==0:
		y_new = y_last+val
		x_new = y_last+val
		center[i] = [x_last, y_new]
		y_limit[i] = [y_last, y_new]
		x_limit[i] = [x_last, x_new]
		x_last, y_last = x_last+val, y_new
	elif count==1:
		y_new = y_last+val
		x_new = x_last-val
		center[i] = [x_new, y_last]
		y_limit[i] = [y_last, y_new]
		x_limit[i] = [x_new, x_last]
		x_last, y_last = x_new, y_last+val
	elif count==2:
		y_new = y_last-val
		x_new = x_last-val
		center[i] = [x_last, y_new]
		y_limit[i] = [y_new, y_last]
		x_limit[i] = [x_new, x_last]
		x_last, y_last = x_last-val, y_new
	else:
		y_new = y_last-val
		x_new = x_last+val
		center[i] = [x_new, y_last]
		y_limit[i] = [y_new, y_last]
		x_limit[i] = [x_last, x_new]
		x_last, y_last = x_new, y_last-val
	count = (count+1)%4
	
#printing pattern
for y in range(series[-1]+series[-2]+1):
	for x in range(series[-1]+1):
		symbol = ' '
		for i in range(size):
			if x_limit[i][0]<=x<=x_limit[i][1] and y_limit[i][0]<=y<=y_limit[i][1] and circle(center[i], [x, y], series[i]):
				symbol = '*'
				
		print(symbol, end='')
	print()
#Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1