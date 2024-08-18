from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#Colision with wall.
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()
#Collision with paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.l_point()
        time.sleep(1)
        ball.reset_ball()
    if ball.xcor() < - 390:
        scoreboard.r_point()
        time.sleep(1)
        ball.reset_ball()


screen.exitonclick()
