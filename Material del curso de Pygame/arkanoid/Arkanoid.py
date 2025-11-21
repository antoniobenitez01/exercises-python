import pgzrun
import random

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 600

score = 0
lives = 3
currentWorld = 1

paddle = Actor("paddleblue",(WIDTH//2,HEIGHT-40))
ball = Actor("ballblue",(100,300))

ball_x_speed = -5
ball_y_speed = -5

bars_list = []

def place_bars(x,y,imagen):
    pos_x = x
    for i in range(9):
        block = Actor(imagen,(pos_x,y))
        bars_list.append(block)
        pos_x += 70

def world(level):
    match level:
        case 1:
            place_bars(120, 100, "element_blue_rectangle_glossy")
            place_bars(120, 150, "element_red_rectangle_glossy")
            place_bars(120, 200, "element_green_rectangle_glossy")
        case 2:
            place_bars(120, 100, "element_blue_rectangle_glossy")
            place_bars(120, 150, "element_red_rectangle_glossy")
            place_bars(120, 200, "element_green_rectangle_glossy")
def draw():
    screen.blit("background",(0,0))
    screen.draw.text(f"Score: { score }",(25,50),color="white")
    screen.draw.text(f"Lives: { lives }", (25,25), color="white")
    paddle.draw()
    ball.draw()
    if lives <= 0:
        screen.draw.text("GAME OVER YOU LOSE!",(WIDTH//2,HEIGHT//2),color="red")
    for block in bars_list:
        block.draw()

def update_paddle():
    if keyboard.left and paddle.left > 0:
        paddle.x -= 5
    if keyboard.right and paddle.right < WIDTH:
        paddle.x += 5

def update_ball():
    global ball_x_speed
    global ball_y_speed
    global lives
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed

    if ball.y >=HEIGHT:
        lives -= 1
        ball.x = 200
        ball.y = 400
    if ball.y <= 0:
        ball_y_speed *= -1
    if ball.x <= 0 or ball.x >= WIDTH:
        ball_x_speed *= -1
    if ball.colliderect(paddle):
        ball_y_speed *= -1
        rnd = random.randint(0,1)
        if rnd == 1:
            ball_x_speed *= -1

def update_bars():
    global ball_y_speed
    global score
    for block in bars_list:
        if block.colliderect(ball):
            bars_list.remove(block)
            score += 1
            ball_y_speed *= -1

def update():
    global lives
    global currentWorld
    if lives <= 0:
        return
    if len(bars_list) == 0:
        world(currentWorld)
        if currentWorld == 2:
            currentWorld = 1
        else:
            currentWorld = 2
    update_paddle()
    update_ball()
    update_bars()

pgzrun.go()