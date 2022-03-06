from turtle import Turtle
from settings import s

ALIGNMENT = s.alignment
FONT = (s.font_family, s.font_size, s.font_set)
y_position = (s.screen_height // 2) - s.font_size - s.size

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, y_position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.penup()
        self.goto((s.screen_width - s.size) // 2, (s.screen_height - s.size) // 2)
        self.goto(s.screen_width // 2, s.screen_height // 2)
        self.pendown()
        self.pensize(20)
        self.setheading(270)
        self.forward(s.screen_height)
        self.setheading(180)
        self.forward(s.screen_width)
        self.setheading(90)
        self.forward(s.screen_height)
        self.setheading(0)
        self.forward(s.screen_width)
