import turtle

window = turtle.Screen()

window.title("Ping Pong")

window.bgcolor("Black")

window.setup(800, 600)

window.tracer(0)

hitter1 = turtle.Turtle()
hitter1.speed(0)
hitter1.shape('square')
hitter1.shapesize(stretch_len=1, stretch_wid=5)
hitter1.color('red')
hitter1.penup()
hitter1.goto(350, 0)

hitter2 = turtle.Turtle()
hitter2.speed(0)
hitter2.shape('square')
hitter2.shapesize(stretch_len=1, stretch_wid=5)
hitter2.color('blue')
hitter2.penup()
hitter2.goto(-350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09

Scorer = turtle.Turtle()
Scorer.speed(0)
Scorer.color('white')
Scorer.penup()
Scorer.hideturtle()
Scorer.goto(0, 260)
Scorer.write('Player 1: 0 Player 2: 0', align='center', font=("Courier",24,"normal"))


def hitter1_move_up():
    y = hitter1.ycor()
    y += 20
    hitter1.sety(y)


def hitter1_move_down():
    y = hitter1.ycor()
    y -= 20
    hitter1.sety(y)


def hitter2_move_up():
    y = hitter2.ycor()
    y += 20
    hitter2.sety(y)


def hitter2_move_down():
    y = hitter2.ycor()
    y -= 20
    hitter2.sety(y)


window.listen()
window.onkeypress(hitter1_move_up, 'w')
window.onkeypress(hitter1_move_down, 's')
window.onkeypress(hitter2_move_up, 'Up')
window.onkeypress(hitter2_move_down, 'Down')

player1_score = 0
player2_score = 0

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player1_score += 1
        Scorer.clear()
        Scorer.write('Player 1: {} Player 2: {}'.format(player1_score,player2_score), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player2_score += 1
        Scorer.clear()
        Scorer.write('Player 1: {} Player 2: {}'.format(player1_score,player2_score), align='center', font=('Courier', 24, 'normal'))

    if (340 < ball.xcor() < 350) and (hitter1.ycor() + 40 > ball.ycor() > hitter1.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (hitter2.ycor() + 40 > ball.ycor() > hitter2.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
