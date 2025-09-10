from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

food = Food()
snake = Snake()
score = ScoreBoard()

#Screen setup 
screen = Screen()
screen.setup(width = 600,height=600) 
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(key = 'Up',fun = snake.up)
screen.onkey(key = 'Down',fun = snake.down )
screen.onkey(key = 'Left',fun = snake.left)
screen.onkey(key = 'Right',fun = snake.right)

game_status_on = True
while game_status_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


    #detect collision of snake head with food

    if snake.all_segments[0].distance(food) < 15:
        food.refreshfood()
        score.trackscore()
        snake.extend_body()

    #detect collision with wall
    if (snake.all_segments[0].xcor() > 290) or (snake.all_segments[0].xcor() < -300) or (snake.all_segments[0].ycor() > 300) or (snake.all_segments[0].ycor() < -290):
         score.restart()
         snake.reset_snake()
        
       

    #detect collision with tail
    for segment in snake.all_segments[1:]:
            if snake.all_segments[0].distance(segment) < 1:
                 score.restart()
                 snake.reset_snake()
                
        
        














screen.exitonclick()