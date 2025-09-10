from turtle import Turtle,Screen
import time

#constants for each key in degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segments = []  #Holding all the snake objects created
        self.create_snake()    #method which defines snake creation
        self.move_snake()    #method which defines snake movement  
        self.reset_snake()

    #--------------------------Snake body-----------------------#
    def create_snake(self):
        distance = 0
        for i in range(3):
            body = Turtle()
            self.all_segments.append(body)
            #Body features
            body.shape('square')
            body.color('white')
            body.penup()
            
            #body creation
            distance += 20
            body.backward(distance)

    #####-----------------------Move snake--------------------##### 
    def move_snake(self):
        
        for segments in range(len(self.all_segments)-1,0,-1):
            xcord = self.all_segments[segments-1].xcor()
            ycord = self.all_segments[segments-1].ycor()
            self.all_segments[segments].goto(xcord,ycord)
        self.all_segments[0].forward(20)

    def reset_snake(self):
        for seg in self.all_segments:
            seg.goto(1000,1000)
        self.all_segments.clear()
        self.create_snake()
        self.all_segments[0] = self.all_segments[0]
        

    def extend_body(self):
        tail = self.all_segments[-1]
        xcord = tail.xcor()
        ycord = tail.ycor()
        new_seg = Turtle('square')
        new_seg.shape('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(xcord,ycord)

        self.all_segments.append(new_seg)
        

    def up(self):
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(UP)
    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(DOWN)
    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(LEFT)
    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(RIGHT)
    