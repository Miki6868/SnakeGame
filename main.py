# steps to create snake game:
# create snake body, move snake, control snake with arrow keys, create snake food, detect collision with food, detect # collision with wall, detect collision with tail, reset game, scoreboard

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake() #initialize snake object
food = Food() #initialize food object
scoreboard = scoreboard() #initialize scoreboard object

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        #print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()
screen.exitonclick()