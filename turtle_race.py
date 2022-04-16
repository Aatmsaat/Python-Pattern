import turtle
from time import sleep
from random import randint

#parameters
def set_pos(obj, pos):
	obj.penup()
	obj.setpos(pos)
	obj.pendown()
col = ['red', 'green', 'blue', 'yellow']
pos = [[-200, -100]]
for i in range(3):
	pos.append([-200, pos[-1][1]+50])

#screen initializing and turtle objects
turtles = []
for i in range(4):
	turtles.append(turtle.Turtle())
	turtles[i].color(col[i])
	turtles[i].shape('turtle')
	set_pos(turtles[i], tuple(pos[i]))
screen = turtle.Screen()
screen.tracer(0)
end = turtle.Turtle()
red_green = turtle.Turtle()

def finish_line():
		set_pos(end, (200, -250))
		end.left(90)
		end.forward(500)
		
def green_red_initialize():
	red_green.color('green')
	red_green.width(50)
	red_green.left(90)
	set_pos(red_green, (-150, 400))

#main program
finish_line()	
green_red_initialize()
red = True
count = 0
maximum = -200
while maximum < 200:
	for i in range(4):
		speed = randint(1, 6)
		turtles[i].forward(speed)
		maximum = max(maximum, turtles[i].pos()[0])
	screen.update()
	count += 1
	if count<randint(4, 6):
		continue
	count = 0
	if red:
		wait = randint(1, 10)
		sleep(wait/10)
		red_green.color('green')
		red_green.forward(20)
		red = False
	else:
		red = True
		red_green.color('red')
		red_green.backward(20)
	#sleep(.5)
		
sleep(1)	