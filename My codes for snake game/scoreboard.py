from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.turtlesize(50, 50, 50)
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 25, "normal"))




