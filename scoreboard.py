from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("purple")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("oops! GAME OVER", False, "center", ("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()






