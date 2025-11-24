import pgzrun
from pgzero.actor import Actor

TITLE = "Rally"
CELL_SIZE = 30
MAP_HEIGHT = 20
MAP_WIDTH = 10
WIDTH = MAP_WIDTH * CELL_SIZE
HEIGHT = MAP_HEIGHT * CELL_SIZE

car = Actor("car_up",(WIDTH//2, HEIGHT - 30))

circuit = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 11, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 5, 1],
    [1, 1, 1, 1, 7, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 9, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 10, 0, 0, 1],
    [1, 1, 1, 1, 4, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 2, 0, 0, 6, 1],
    [1, 1, 1, 10, 0, 0, 8, 1, 1, 1],
    [4, 2, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 6, 1, 1, 1, 1],
    [0, 0, 8, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 11, 1, 1, 1, 1, 1, 1, 1],
    [0, 2, 0, 0, 0, 5, 1, 1, 1, 1],
    [7, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 9, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
]

walls = []
goals = []
coins = []
corners = []

def convert_position(pos):
    return pos * CELL_SIZE + CELL_SIZE // 2

def setmap(circuit):
    for x in range (0, MAP_WIDTH, 1):
        for y in range (0, MAP_HEIGHT, 1):
            if circuit[y][x] == 1:
                walls.append(Actor("wall",pos=(convert_position(x),convert_position(y))))
            if circuit[y][x] == 2:
                coins.append(Actor("coin",pos=(convert_position(x),convert_position(y))))
            if circuit[y][x] == 3:
                goals.append(Actor("goal",pos=(convert_position(x),convert_position(y))))
            if circuit[y][x] >= 4:
                corners.append(Actor("corner" + str((circuit[y][x])-3),pos=(convert_position(x),convert_position(y))))

status = 0
def draw():
    screen.clear()
    if status == 1:
        screen.draw.text("YOU WIN!", (WIDTH//2,HEIGHT//2), fontsize=40, color="green")
    elif status == 2:
        screen.draw.text("GAME OVER", (WIDTH//2,HEIGHT//2), fontsize=40, color="red")
    else:
        screen.fill((255,255,255))
        car.draw()
        for wall in walls:
            wall.draw()
        for coin in coins:
            coin.draw()
        for goal in goals:
            goal.draw()
        for corner in corners:
            corner.draw()
        screen.draw.text(f"Score: { score }",(10,10),fontsize = 20, color = "red")

car_speed = 2
def update_car():
    if keyboard.up and car.y > 0:
        car.y -= car_speed
        car.image = "car_up"
    elif keyboard.down and car.y < HEIGHT:
        car.y += car_speed
        car.image = "car_down"
    elif keyboard.left and car.x > 0:
        car.x -= car_speed
        car.image = "car_left"
    elif keyboard.right and car.x < WIDTH:
        car.x += car_speed
        car.image = "car_right"

score = 0
def check_gain():
    global score
    for coin in coins:
        if coin.colliderect(car):
            score += 1
            coins.remove(coin)

def check_goal():
    global status
    for goal in goals:
        if goal.colliderect(car):
            status = 1

def check_collision():
    global status
    for wall in walls:
        if wall.colliderect(car):
            status = 2

def update():
    if status == 0:
        update_car()
        check_collision()
        check_goal()
        check_gain()

setmap(circuit)
pgzrun.go()