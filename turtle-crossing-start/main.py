import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)


t = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(t.go_up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.move_cars()

# Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(t) < 20:
            game_is_on = False
            scoreboard.game_over()

# Detect turtle reaches the other side
    if t.is_reach_Finish_line():
        t.start()
        car_manager.level_up()
        scoreboard.update_scoreboard()







screen.exitonclick()


