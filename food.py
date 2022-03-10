import random
from turtle import Turtle


class Food:

    def __init__(self):
        self.food = Turtle()
        self.food.penup()
        self.food.color("pink")
        self.food.shape("square")
        self.place_food()

    def place_food(self):
        x_list = [x for x in range(-260, 270, 20)]
        y_list = [y for y in range(-260, 270, 20)]
        self.food.setposition(random.choice(x_list), random.choice(y_list))
