from turtle import *
def up():
    setheading(90)
    fd(100)

def down():
    setheading(270)
    fd(100)

def left():
    setheading(180)
    fd(100)

def right():
    setheading(0)
    fd(100)

def Exit():
    write("End of the program")
    delay(1000)
    bye()#/done()

def clickleft(x,y):
    if pencolor()=='blue':
        pencolor('red')
    else:
        pencolor('blue')

def clickright(x,y):
    print('location:',x,y)
    stamp()

listen()
onkey(up,'Up')
onkey(down,'Down')
onkey(left,'Left')
onkey(right,'Right')
onkey(Exit,'a')
onscreenclick(clickleft,1)
onscreenclick(clickright,3)
# Mouse clicks- Left_click-1, Scroll_Button-2, Right_click-3
mainloop()

