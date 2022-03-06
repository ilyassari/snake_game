from turtle import Turtle
from settings import s


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = list()
for i in range(s.starting_length):
    starting_positions.append((-i * s.size, 0))


class Snake:
    def __init__(self):
        self.parts = list()
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_part(position)

    def add_part(self, position):
            new_part = Turtle(shape="square")
            new_part.color("white")
            new_part.penup()
            new_part.goto(position)
            self.parts.append(new_part)


    def extend(self):
        self.add_part(self.parts[-1].position())

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(s.size)

    def relational_left(self):
        current = self.head.heading()
        self.head.setheading(current + 90)

    def relational_right(self):
        current = self.head.heading()
        self.head.setheading(current - 90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)