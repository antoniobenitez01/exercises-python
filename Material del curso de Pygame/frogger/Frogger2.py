import pgzrun
import random

TITLE = "FROGGER"
WIDTH = 800
HEIGHT = 600

lives = 3
score = 0

player = Actor("frog_up",(WIDTH//2,HEIGHT-50))

vehicles_right = []
vehicles_left = []
y = 50
num_vehicles = 8
for i in range (num_vehicles):
    x = random.randint(0,WIDTH)
    y = y + 40
    pos = random.randint(0,1)
    if pos == 0:
        car = Actor("car", (x, y))
        vehicles_right.append(car)
    else:
        car = Actor("car_inv", (x, y))
        vehicles_left.append(car)

def draw():
    screen.fill("grey")
    screen.draw.filled_rect(Rect((0,0), (WIDTH,50)),"green")
    screen.draw.text(f"Score: { score }", (10,10),color="white")
    screen.draw.text(f"Lives: { lives }", (WIDTH-100, 10), color="white")
    if(lives <= 0):
        screen.draw.text("GAME OVER", (WIDTH//2,HEIGHT//2), color="red")
    player.draw()
    for vehicle in vehicles_left + vehicles_right:
        vehicle.draw()

def reset_player():
    player.pos = (WIDTH // 2, HEIGHT - 50)

def update_player():
    global score
    player_speed = 3
    gap = 5
    if (keyboard.left) and (player.x > gap):
        player.x  = player.x - player_speed
        player.image = "frog_left"
    if (keyboard.right) and (player.x < WIDTH - gap):
        player.x  = player.x + player_speed
        player.image = "frog_right"
    if (keyboard.up) and (player.y > gap):
        player.y  = player.y - player_speed
        player.image = "frog_up"
    if (keyboard.down) and (player.y < HEIGHT - gap):
        player.y  = player.y + player_speed
        player.image = "frog_down"
    if player.y < 50:
        score += 1
        reset_player()

def update_vehicles():
    global lives
    vehicle_speed = 10
    for vehicle in vehicles_right:
        vehicle.x = vehicle.x + vehicle_speed
        if vehicle.x > WIDTH:
            vehicle.x = -50
    for vehicle in vehicles_left:
        vehicle.x = vehicle.x - vehicle_speed
        if vehicle.x < 0:
            vehicle.x = WIDTH + 50
    for vehicle in vehicles_left + vehicles_right:
        if player.colliderect(vehicle):
            lives -= 1
            reset_player()

def update():
    if lives <= 0:
        return
    update_player()
    update_vehicles()

pgzrun.go()