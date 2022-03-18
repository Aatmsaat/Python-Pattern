import turtle
from time import sleep

col = ['violet', 'red', 'blue', 'green', 'yellow', 'orange']
colors = []

for i in range(6):
	obj = turtle.Turtle()
	obj.speed(0)
	obj.penup()
	obj.setpos(-200, -100)
	obj.pendown()
	obj.color(col[i])
	obj.pensize(5)
	obj.left(45)
	colors.append(obj)

for i in range(5):
	for j, obj in enumerate(colors):
		obj.right(j*2)
		obj.forward(50)
		
colors[2].write('Happy', font=('Aerial', '20', 'bold'))
colors[5].write('Holi', font=('Aerial', '20', 'bold'))
sleep(2)
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1