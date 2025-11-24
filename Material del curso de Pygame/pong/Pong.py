import pgzrun
import random

TITLE = "Pong"
WIDTH = 600
HEIGHT = 400

left_paddle = Actor("paddle_red",(50,HEIGHT//2))
right_paddle = Actor("paddle_blue",(WIDTH-50,HEIGHT//2))
ball = Actor("ball",(WIDTH//2,HEIGHT//2))

paddle_speed = 5
ball_speed = 5
ball_speed_x = ball_speed
ball_speed_y = ball_speed


left_score = 0
right_score = 0

def draw():
    screen.fill((0,0,0))
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()
    screen.draw.text(f"{left_score}", (WIDTH//4, 20), fontsize=40, color="white")
    screen.draw.text(f"{right_score}",(WIDTH*3 // 4, 20),fontsize=40, color="white")

def update_left_paddle():
    global left_paddle
    if keyboard.w and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keyboard.s and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed

def update_right_paddle():
    global right_paddle
    if keyboard.o and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keyboard.l and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed

def update_ball():
    global ball, ball_speed_x, ball_speed_y
    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -1 * ball_speed_y

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -1 * ball_speed_x
        if (random.randint(0,1)):
            ball_speed_y = -1 * ball_speed_y

def update_score():
    global left_score, right_score, ball_speed_x, ball_speed_y
    if ball.left <= 0:
        right_score += 1
        ball.pos = (WIDTH//2, HEIGHT//2)
        ball_speed_x = -1 * ball_speed_x
        if (random.randint(0,1)):
            ball_speed_y = -1 * ball_speed_y
    if ball.right >= WIDTH:
        left_score += 1
        ball.pos = (WIDTH//2, HEIGHT//2)
        ball_speed_x = -1 * ball_speed_x
        if (random.randint(0,1)):
            ball_speed_y = -1 * ball_speed_y

def update():
    update_left_paddle()
    update_right_paddle()
    update_ball()
    update_score()

pgzrun.go()