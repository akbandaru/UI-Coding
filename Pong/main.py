from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

tim = Turtle()
screen.update()
tim.color("white")
tim.pencolor("white")
tim.penup()
tim.hideturtle()
tim.speed("fastest")

tim.goto(x=0, y=400)
tim.setheading(270)
tim.speed("fastest")

for i in range(40):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

user1_paddle = Paddle((350, 0))
user2_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=user1_paddle.up, key="Up")
screen.onkey(fun=user1_paddle.down, key="Down")
screen.onkey(fun=user2_paddle.up, key="w")
screen.onkey(fun=user2_paddle.down, key="s")
is_game_on = True


while is_game_on:
    time.sleep(0.01)
    screen.update()

    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(user1_paddle) < 50 and ball.xcor() > 320 or ball.distance(user2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect user1 paddle misses
    if ball.xcor() > 380:
        ball.reset_environment()
        scoreboard.user1_point()

    # Detect user2 paddle misses
    if ball.xcor() < -380:
        ball.reset_environment()
        scoreboard.user2_point()


screen.exitonclick()

