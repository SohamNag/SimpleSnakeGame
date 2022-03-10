import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
new_snake = Snake()
new_food = Food()
screen.update()
new_score = ScoreBoard()

while game_on:
    if new_snake.boundary_overshoot():
        game_on = False
        #screen.bye()
        break
    if new_snake.snake_body[0].distance(new_food.food) < 20:
        new_snake.add_bit()
        new_food.place_food()
        new_score.increase_score()
    time.sleep(0.3)
    screen.onkeypress(new_snake.move_left, "Left")
    screen.onkeypress(new_snake.move_right, "Right")
    screen.onkeypress(new_snake.move_up, "Up")
    screen.onkeypress(new_snake.move_down, "Down")
    new_snake.move_snake()
    screen.update()
