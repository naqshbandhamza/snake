import turtle

class Box:
    def __init__(self,x,y,color,shape):
        self.obj = turtle.Turtle()
        self.obj.shape(shape)
        self.obj.color(color)
        self.obj.penup()
        self.obj.goto(x,y)
        
    def snake_up(self):
        y = self.obj.ycor()
        y+=20
        self.obj.sety(y)

    def snake_down(self):
        y = self.obj.ycor()
        y-=20
        self.obj.sety(y)

    def snake_left(self):
        x = self.obj.xcor()
        x-=20
        self.obj.setx(x)
        

    def snake_right(self):
        x = self.obj.xcor()
        x+=20
        self.obj.setx(x)


class Snake():
    def __init__(self):
        self.snake = []
        self.pos = []
        self.pos1 = []
        self.x = -330
        self.y = 250
        
