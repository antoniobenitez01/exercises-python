import pgzrun

TITLE = "Mario"
HEIGHT = 500
WIDTH = 800

player = Actor("mario_right",(100, HEIGHT-200))
coin = Actor("coin",(2 * WIDTH - 100, HEIGHT-150))

background = Actor("background",(WIDTH//2,HEIGHT//2))
background.left = 0

total_enemies = 5
enemies = []

platforms = []
ground = []

player_speed = 3
enemy_speed = 1

gravity = 0.5
jump_strength = -10
is_jumping = False
velocity_y = 0

status = 0

camera_offset = 0
scroll_limit = 100

def create_enemies():
    for i in range(0, total_enemies, 1):
        enemy = Actor("enemy_left", (WIDTH + 100 * i, HEIGHT - 60))
        enemies.append(enemy)

def create_block(list,image,x,y):
    block = Actor(image,(x,y))
    list.append(block)

def create_platforms():
    create_block(platforms,"brick",200,HEIGHT - 100)
    create_block(platforms, "brick", 300, HEIGHT - 200)
    create_block(platforms, "brick", 400, HEIGHT - 300)
    create_block(platforms, "brick", 500, HEIGHT - 400)
    for i in range(0, 200, 40):
        create_block(ground,"green",i, HEIGHT-20)
    for i in range(560, 2 * WIDTH, 40):
        create_block(ground,"green",i, HEIGHT-20)

def draw():
    screen.clear()
    if status == 1:
        screen.draw.text("YOU WIN!",(WIDTH // 2, HEIGHT // 2), fontsize = 40,color = "green")
    elif status == 2:
        screen.draw.text("GAME OVER", (WIDTH // 2, HEIGHT // 2), fontsize=40, color="red")
    else:
        background.draw()
        player.draw()
        coin.draw()
        for enemy in enemies:
            enemy.draw()
        for block in platforms:
            block.draw()
        for green in ground:
            green.draw()

def update_player():
    global status
    if keyboard.right and player.x < WIDTH:
        player.x += player_speed
        player.image = "mario_right"
    if keyboard.left and player.x > 0:
        player.x -= player_speed
        player.image = "mario_left"
    if player.y > HEIGHT:
        status = 2
    if player.colliderect(coin):
        status = 1
    for enemy in enemies:
        if player.colliderect(enemy):
            if player.y < enemy.y:
                enemies.remove(enemy)
            else:
                status = 2

def update_gravity():
    global is_jumping, velocity_y
    velocity_y += gravity
    if not is_jumping:
        if keyboard.up:
            velocity_y = jump_strength
            is_jumping = True
    player.y += velocity_y
    for block in platforms + ground:
        if player.colliderect(block) and player.y < block.y and velocity_y >= 0:
            player.bottom = block.top + 3
            velocity_y = 0
            is_jumping = False

def update_enemy(enemy):
    if enemy.image == "enemy_right":
        direction = 1
    else:
        direction = -1
    enemy.x += direction * enemy_speed
    change_direction = False
    for block in ground:
        if enemy.colliderect(block):
            change_direction = True
    if change_direction:
        enemy.x -= direction * enemy_speed
        if enemy.image == "enemy_right":
            enemy.image = "enemy_left"
        else:
            enemy.image = "enemy_right"
        change_direction = False

def update_enemies():
    for enemy in enemies:
        update_enemy(enemy)

def update_camera():
    global camera_offset
    if player.x > camera_offset + scroll_limit:
        camera_offset += player_speed
        background.x -= player_speed
        coin.x -= player_speed
        for block in ground + platforms:
            block.x -= player_speed
        for enemy in enemies:
            enemy.x -= player_speed
    if player.x < camera_offset + scroll_limit and camera_offset > 0:
        camera_offset -= player_speed
        background.x += player_speed
        coin.x += player_speed
        for block in ground + platforms:
            block.x += player_speed
        for enemy in enemies:
            enemy.x += player_speed

def update():
    if status == 0:
        update_player()
        update_enemies()
        update_gravity()
        update_camera()

create_enemies()
create_platforms()
pgzrun.go()