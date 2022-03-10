# import turtle package
import turtle


# function to draw paper fan 
def paper_fan(easy):
    
    for count in range(0, 200, 2):
    	easy.color(colors[count%3])
    	easy.right(60)
    	if count%2==0:
    		easy.backward(count//2)
    	easy.forward(count)
    	count+=2
 
if __name__ == "__main__" :
    #initialize screen for motion
    screen = turtle.Screen() 
    screen.bgcolor('black')
    screen.tracer(0)           

    #initialize Turtle object 
    turtal = turtle.Turtle()
    turtal.width(5)
    colors = ['yellow', 'white', 'cyan']

    #Real motion for infinity
    while True :
        turtal.clear()  
        paper_fan(turtal)   
        screen.update() 
        turtal.goto(0, 0)
        colors[0], colors[1], colors[2] = colors[2], colors[0], colors[1]
        turtal.left(10)
# Subscribe please https://m.youtube.com/channel/UCuVa4ZaUMGxYpuWfa1AOmSQ?sub_confirmation=1