from turtle import *
while True:
	side = int(textinput('','Enter no. of sides : '))
	angle = 360//side
	for _ in range(side):
		forward(90)
		right(angle)
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1