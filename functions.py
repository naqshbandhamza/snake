#the checkoverlap() function starts the snake from the other side
#if the screen if it crosses one side of the screen
import pygame
from random import *
from classes import Box



def overlap(s,win):
    if s.snake[0].obj.xcor()>=400:
       pass
    elif s.snake[0].obj.xcor()<=-400:
       pass
    elif s.snake[0].obj.ycor()>=300:
       pass
    elif s.snake[0].obj.ycor()<=-300:
       pass

def relocate(o4,box,score,s):
    temp1,temp2 = box.xcor(), box.ycor()
    
    if ((o4.obj.xcor()<=box.xcor()and o4.obj.xcor()>=box.xcor()-25) and (o4.obj.ycor()<=box.ycor() and o4.obj.ycor()>=box.ycor()-25)):
        y,x =0,0
        while(x==temp1):
            x = randrange(-390,390,100)
        while(y==temp2):
            y = randrange(-290,290,100)
        score+=5
        box.color('red')
        no = pygame.mixer.Sound("coin2.wav")
        no.play()
        box.goto(x,y)
        if s.snake[-1].obj.xcor()==s.snake[-2].obj.xcor() and s.snake[-1].obj.ycor()!=s.snake[-2].obj.ycor():
            if s.snake[-2].obj.ycor()>s.snake[-1].obj.ycor():
                x = s.snake[-1].obj.xcor()
                y = s.snake[-1].obj.ycor()-20
            elif s.snake[-2].obj.ycor()<s.snake[-1].obj.ycor():
                x = s.snake[-1].obj.xcor()
                y = s.snake[-1].obj.ycor()+20
        elif s.snake[-1].obj.xcor()!=s.snake[-2].obj.xcor() and s.snake[-1].obj.ycor()==s.snake[-2].obj.ycor():
            if s.snake[-2].obj.xcor()>s.snake[-1].obj.xcor():
                x = s.snake[-1].obj.xcor()-20
                y = s.snake[-1].obj.ycor()
            elif s.snake[-2].obj.xcor()<s.snake[-1].obj.xcor():
                x = s.snake[-1].obj.xcor()+20
                y = s.snake[-1].obj.ycor()
        o = Box(x,y,'yellow','square')
        s.snake.append(o)
        print(len(s.snake))   
    return score
        
#the motion function deals with the motion of the snake        
def motion(s,x,y):
    if(x!=s.snake[0].obj.xcor() or y!=s.snake[0].obj.ycor()):
        for i in range(1,len(s.snake)):
            if s.snake[i].obj.xcor()+20==x and s.snake[i].obj.ycor()==y:
                x = s.snake[i].obj.xcor()
                y = s.snake[i].obj.ycor()
                s.snake[i].snake_right()
            elif s.snake[i].obj.xcor()-20==x and s.snake[i].obj.ycor()==y:
                x = s.snake[i].obj.xcor()
                y = s.snake[i].obj.ycor()
                s.snake[i].snake_left()
            elif s.snake[i].obj.ycor()+20==y and s.snake[i].obj.xcor()==x:
                x = s.snake[i].obj.xcor()
                y = s.snake[i].obj.ycor()
                s.snake[i].snake_up()
            elif s.snake[i].obj.ycor()-20==y and s.snake[i].obj.xcor()==x:
                x = s.snake[i].obj.xcor()
                y = s.snake[i].obj.ycor()
                s.snake[i].snake_down()
    s.x,s.y = s.snake[0].obj.xcor(),s.snake[0].obj.ycor()
