from turtle import Turtle
from random import choice
from settings import s

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("orange")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        x = choice(range(-(s.screen_width//2 - s.size), s.screen_width//2, s.size))
        y = choice(range(-(s.screen_height//2 - s.size), s.screen_height//2, s.size))
        self.goto(x, y)