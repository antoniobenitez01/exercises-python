import pgzrun
import random

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 700

class GameConfig():
    def __init__(self,speed:int):
        self.speed = speed

gameConfig = GameConfig(5)

bird = Actor('bird1',(75,200))
pipe_top = Actor('top', anchor=('left','bottom'))
pipe_bottom = Actor('bottom', anchor=('left','top'))

def reset_pipes():
    gameConfig.speed = 5
    GAP = random.randint(100,300)
    pos = random.randint(200, HEIGHT-200)
    pipe_top.pos = (WIDTH,pos - GAP//2)
    pipe_bottom.pos = (WIDTH,pos + GAP//2)

reset_pipes()

def draw():
    screen.blit('background',(0,0))
    bird.draw()
    pipe_top.draw()
    pipe_bottom.draw()

def update_pipes():
    pipe_top.left = pipe_top.left - gameConfig.speed
    pipe_bottom.left = pipe_bottom.left - gameConfig.speed
    if pipe_top.right < 0:
        reset_pipes()

bird.dead = False
GRAVITY = 0.3
bird.vy = 0
def update_bird():
    bird.vy = bird.vy + GRAVITY
    bird.y = bird.y + bird.vy
    bird.x = 75
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'
        gameConfig.speed = 0
    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.vy = 0
        reset_pipes()
    if not bird.dead:
        if bird.vy < -1:
            bird.image = 'bird1'
        else:
            bird.image = 'bird2'

FLAP_VELOCITY = -6.5
def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY

def update():
    update_pipes()
    update_bird()

pgzrun.go()