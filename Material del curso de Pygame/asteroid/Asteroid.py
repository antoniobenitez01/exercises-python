import pgzrun
import random

TITLE = "Asteroid"
WIDTH = 600
HEIGHT = 400

spaceship = Actor("spaceship_right",(50,HEIGHT//2))

def create_asteroid():
    pos_x = WIDTH + 50
    pos_y = random.randint(0,HEIGHT)
    speed_x = random.randint(2,5)
    speed_y = random.randint(-1,1)
    if random.randint(0,1):
        image = "asteroid1"
    else:
        image = "asteroid2"
    asteroid = Actor(image,(pos_x,pos_y))
    asteroid.speed_x = speed_x
    asteroid.speed_y = speed_y
    return asteroid

asteroids = []
max_asteroids = 10
lasers = []
status = 0
score = 0
max_score = 10

def create_asteroids_list():
    for i in range(len(asteroids),max_asteroids):
        asteroids.append(create_asteroid())

def draw():
    if status == 1:
        screen.draw.text("YOU WIN!",(WIDTH//2,HEIGHT//2),fontsize = 40,color="green")
    elif status == 2:
        screen.draw.text("GAME OVER", (WIDTH // 2, HEIGHT // 2), fontsize=40, color="red")
    else:
        screen.clear()
        spaceship.draw()
        create_asteroids_list()
        for asteroid in asteroids:
            asteroid.draw()
        for laser in lasers:
            laser.draw()
        screen.draw.text(f"Puntos: { score }",(10,10),fontsize=20,color="white")

spaceship_vel = 5
def update_spaceship():
    if keyboard.left and spaceship.left > 0:
        spaceship.x -= spaceship_vel
    elif keyboard.right and spaceship.right < WIDTH:
        spaceship.x += spaceship_vel
    elif keyboard.up and spaceship.top > 0:
        spaceship.y -= spaceship_vel
    elif keyboard.down and spaceship.bottom < HEIGHT:
        spaceship.y += spaceship_vel

def update_asteroids():
    global asteroids
    new_asteroids = []
    for asteroid in asteroids:
        asteroid.x -= asteroid.speed_x
        asteroid.y -= asteroid.speed_y
        if asteroid.x > 0:
            new_asteroids.append(asteroid)
        else:
            new_asteroids.append(create_asteroid())
        asteroids = new_asteroids

def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("bullet",(spaceship.x + 30,spaceship.y))
        lasers.append(laser)

def update_lasers():
    for laser in lasers:
        laser.x += 10
        if (laser.x < 0) or (laser.x > WIDTH):
            lasers.remove(laser)

def check_collission():
    global status, score
    for asteroid in asteroids:
        for laser in lasers:
            if laser.colliderect(asteroid):
                lasers.remove(laser)
                asteroids.remove(asteroid)
                score += 1
                if score == max_score:
                    status = 1
                if asteroid.image == "asteroid2":
                    for i in range(random.randint(1,3)):
                        new_asteroid = Actor("asteroid1",(asteroid.x,asteroid.y))
                        new_asteroid.speed_x = random.randint(2,5)
                        new_asteroid.speed_y = random.randint(-1,1)
                        asteroids.append(new_asteroid)

        if asteroid.colliderect(spaceship):
            status = 2

def update():
    update_spaceship()
    update_asteroids()
    update_lasers()
    check_collission()

pgzrun.go()