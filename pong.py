import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong by Me")
wn.bgcolor("white")
wn.setup(width=800, height=600)


score_a= 0
score_b= 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#
# # Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
# paddle_b.shapesize(stretch_wid=5,stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

pen= turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : {} :: Player B : {}".format(score_a, score_b), align='center', font={'Courier',24,'normal'})
# to move paddle_a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# to move paddle_a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# to move paddle_b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# to move paddle_b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "d")
wn.onkeypress(paddle_b_up, "h")
wn.onkeypress(paddle_b_down, "b")
wn.onkeypress(paddle_a_down, "c")

while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # for bouncing the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {} :: Player B : {}".format(score_a, score_b), align='center',font={'Courier', 24, 'normal'})
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_b += 1
        pen.write("Player A : {} :: Player B : {}".format(score_a, score_b), align='center', font={'Courier', 24, 'normal'})
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # handling paddle collisions
    if (ball.xcor()>340 and ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() and ball.ycor() > (paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() +40 > ball.ycor() and ball.ycor() > (paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

turtle.down()
