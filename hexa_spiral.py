from turtle import *

#turtle parameters
easy = Turtle()
easy.speed(1000)
easy.pensize(5)
bgcolor('black')

colors = ['yellow', 'white', 'cyan']
count=0

while True:
	#count%3 = 0, 1, 2 -> indices of colors
	easy.color(colors[count%3])
	easy.right(61)
	easy.forward(count)
	count+=2
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1