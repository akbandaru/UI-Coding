from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.user2_score = 0
        self.user1_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.user1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.user2_score, align="center", font=("Courier", 80, "normal"))

    def user2_point(self):
        self.user2_score += 1
        self.update_score()

    def user1_point(self):
        self.user1_score += 1
