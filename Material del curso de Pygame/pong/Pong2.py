import pgzrun
import random

TITLE = "Pong 2"
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
start_screen = True
mode = 0

def draw():
    if start_screen:
        screen.draw.text("SELECCIONA EL MODO DE JUEGO", center=(WIDTH//2, HEIGHT//2-50),fontsize = 40, color = "white")
        screen.draw.text("1 - Contra CPU", center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color="white")
        screen.draw.text("2 - 2 Jugadores", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")
    else:
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
    if ball_speed_x > 0 and ball.x > WIDTH//2:
        if ball.y < right_paddle.top and right_paddle.top > 0:
            right_paddle.y -= paddle_speed
        if ball.y > right_paddle.bottom and right_paddle.bottom < HEIGHT:
            right_paddle.y += paddle_speed

def update_right_paddle_player():
    global right_paddle
    if keyboard.u and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keyboard.j and right_paddle.bottom < HEIGHT:
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
    global start_screen, mode
    if start_screen:
        if keyboard.k_1:
            mode = 1
            start_screen = False
        if keyboard.k_2:
            mode = 2
            start_screen = False
    update_left_paddle()
    if mode == 1:
        update_right_paddle()
    else:
        update_right_paddle_player()
    update_ball()
    update_score()

pgzrun.go()