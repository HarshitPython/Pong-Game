from turtle import Turtle,Screen
from paddle import Paddle
from Ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
Ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    Ball.move()

    #Detect collision with the wall'''
    if Ball.ycor() > 280 or Ball.ycor() < -280:
        Ball.bounce_y()

#     #Detect collision with right paddle'''
#     if Ball.distance(r_paddle) < 50 and Ball.xcor() > 320:
#         Ball.bounce_x_r_paddle()
    
#     #Detect collision with left paddle'''
#     if Ball.distance(l_paddle) < 50 and Ball.xcor() < -320:
#         Ball.bounce_x_l_paddle()

#     #Detect R paddle misses'''
#     if Ball.xcor() > 380:
#         Ball.reset()
#         score.l_point()

#     #Detect L paddle misses'''
#     if Ball.xcor() < -380:
#         Ball.reset()
#         score.r_point()



# screen.exitonclick()
