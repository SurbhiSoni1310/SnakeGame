from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

