from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # The shape from the above is normally 20 X 20, so this will do 10 X 10
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)  # our screen is -300 to 300
        random_y = random.randint(-280, 280)  # our screen is -300 to 300
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # our screen is -300 to 300
        random_y = random.randint(-280, 280)  # our screen is -300 to 300
        self.goto(random_x, random_y)