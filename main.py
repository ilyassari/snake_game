from turtle import Screen
import time

from snake import Snake
from food import Food
from laborer import Boundary, Scoreboard
from settings import s



screen = Screen()
screen.setup(width=s.screen_width + s.size, height=s.screen_height + s.size)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
boundary_x = (s.screen_width // 2) - s.size
boundary_y = (s.screen_height // 2) - s.size

laborer = Boundary()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
if s.relational_direction:
    screen.onkey(snake.relational_left, 'Left')
    screen.onkey(snake.relational_right, 'Right')
else:
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(s.game_pace)
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 1:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if scoreboard.score % s.count_to_speed_up == 0:
            s.speed_up()

    # detect collision with wall
    if snake.head.xcor() > boundary_x or snake.head.xcor() < -boundary_x or snake.head.ycor() > boundary_y or snake.head.ycor() < -boundary_y:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    for part in snake.parts[1::]:
        if snake.head.distance(part) < 10:
            is_game_on = False
            scoreboard.game_over()




screen.exitonclick()
