from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def go_up(self):
        # new_y = self.ycor() + 10
        # self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)

    def is_reach_Finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True






