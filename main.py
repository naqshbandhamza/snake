import turtle
import pygame
from functions import *
from classes import *
import time

pygame.init()
win = turtle.Screen()
win.title('Snake Game')
win.bgcolor('green')
win.setup(width = 800, height = 600)
win.tracer(0)
count = 0

no = pygame.mixer.Sound("ryu.wav")

no.play()

x,y = -330,250

box = turtle.Turtle()
box.shape('circle')
box.color('red')
box.penup()
box.goto(0,0)

s = Snake()
o = Box(x,y,'orange','square')
s.snake.append(o)
x-=20

for i in range(0,50):
    o = Box(x,y,'yellow','square')
    x-=20
    s.snake.append(o)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)

s.x,s.y = s.snake[0].obj.xcor(),s.snake[0].obj.ycor()
what = 3
loopcontrol = True

def func1():
    global what
    what = 1
def func2():
    global what
    what = 2
def func3():
    global what
    what = 3
def func4():
    global what
    what = 4
    
win.listen()
win.onkeyrelease(func1,'Up')
win.onkeyrelease(func2,'Down')
win.onkeyrelease(func3,'Right')
win.onkeyrelease(func4,'Left')

index = 0
score = 0
choice = 0

while loopcontrol:
    
    time.sleep(0.1)
    if what==1:
        s.snake[0].snake_up()
    elif what==2:
        s.snake[0].snake_down()
    elif what==3:
        s.snake[0].snake_right()
    elif what==4:
        s.snake[0].snake_left()

    
    for i in range(1,len(s.snake)):
        if ((s.snake[0].obj.xcor()<=s.snake[i].obj.xcor()and s.snake[0].obj.xcor()>=s.snake[i].obj.xcor()-5) and (s.snake[0].obj.ycor()<=s.snake[i].obj.ycor() and s.snake[0].obj.ycor()>=s.snake[i].obj.ycor()-5)):
            loopcontrol = False
            break
    if s.snake[0].obj.xcor()>=400:
       loopcontrol = False
    elif s.snake[0].obj.xcor()<=-400:
       loopcontrol = False
    elif s.snake[0].obj.ycor()>=300:
       loopcontrol = False
    elif s.snake[0].obj.ycor()<=-300:
       loopcontrol = False
    elif score>=500:
        loopcontrol = False
        
    if(s.x!=s.snake[0].obj.xcor() or s.y!=s.snake[0].obj.ycor()):
        motion(s,s.x,s.y)
    else:
        pass
   
    score = relocate(s.snake[0],box,score,s)
    pen.clear()
    
    if(loopcontrol==True):
        pen.write('Score: {}'.format(score), align='center',font = ('Arial',15,'bold'))
    elif score>=500:
        pen.write('YOU WIN Score: {}'.format(score),align='center',font = ('Arial',15,'bold'))
        no = pygame.mixer.Sound("win.wav")
        no.play()
    else:
        pen.write('GAME OVER Final Score: {}'.format(score),align='center',font = ('Arial',15,'bold'))
        no = pygame.mixer.Sound("gameover.wav")
        no.play()
    win.update()
