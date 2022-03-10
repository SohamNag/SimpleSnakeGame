from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(0, -50, -20):
            self.snake_bit = Turtle()
            self.snake_bit.penup()
            self.snake_bit.shape("square")
            self.snake_bit.color("white")
            self.snake_bit.goto(i, 0)
            self.snake_body.append(self.snake_bit)
        self.snake_body[0].color("red")

    def move_snake(self):
        for snake_segment in range(len(self.snake_body) - 1, 0, -1):
            xy_new = self.snake_body[snake_segment - 1].pos()
            self.snake_body[snake_segment].setpos(xy_new)
        self.snake_body[0].forward(20)

    def boundary_overshoot(self):
        if self.snake_body[0].xcor() >= 290 or self.snake_body[0].xcor() <= -290:
            return True
        if self.snake_body[0].ycor() >= 290 or self.snake_body[0].ycor() <= -290:
            return True

    def move_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def move_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def move_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def add_bit(self):
        new_bit = Turtle()
        new_bit.shape("square")
        new_bit.color("white")
        new_bit.penup()
        new_x = self.snake_body[-2].xcor() - self.snake_body[-1].xcor()
        new_y = self.snake_body[-2].ycor() - self.snake_body[-1].ycor()
        new_bit.goto(self.snake_body[-1].xcor() - new_x, self.snake_body[-1].ycor() - new_y)
        self.snake_body.append(new_bit)
