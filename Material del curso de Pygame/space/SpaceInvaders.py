import pgzrun
import random

TITLE = "Space Invaders"
WIDTH = 800
HEIGHT = 600

player = Actor("ship",(WIDTH//2,HEIGHT-50))

status = 0
aliens = []
lasers = []
aliens_lasers = []
shields = []
player_speed = 5
laser_speed = -5
alien_speed = 10
alien_laser_speed = 3

def create_shields():
    num = 6
    pos_x = WIDTH // (num+1)
    pos_y = HEIGHT - 120
    for i in range(num):
        shields.append(Actor("shield1",(pos_x,pos_y)))
        pos_x += WIDTH // (num+1)

def create_aliens():
    cont = 1
    for y in range(50,300,50):
        for x in range(50,WIDTH-50,100):
            match cont:
                case 1:
                    image = "enemy1_1"
                case 2:
                    image = "enemy2_1"
                case 3:
                    image = "enemy3_1"
            aliens.append(Actor(image,(x,y)))
        cont += 1
        if cont > 3:
            cont = 1

def draw():
    screen.clear()
    if status == 1:
        screen.draw.text("YOU WIN",(WIDTH//3,HEIGHT//2),fontsize = 40,color="green")
    if status == 2:
        screen.draw.text("GAME OVER",(WIDTH//3,HEIGHT//2),fontsize = 40,color="red")
    else:
        player.draw()
        for alien in aliens:
            alien.draw()
        for laser in lasers:
            laser.draw()
        for alien_laser in aliens_lasers:
            alien_laser.draw()
        for shield in shields:
            shield.draw()


def update_player():
    global player
    if keyboard.left and player.left >= 0:
        player.x -= player_speed
    if keyboard.right and player.right <= WIDTH:
        player.x += player_speed

def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("laser",(player.x,player.y - 30))
        lasers.append(laser)

def update_lasers():
    for laser in lasers:
        laser.y += laser_speed
        if laser.y < 0:
            lasers.remove(laser)

def shoot_alien_laser():
    if aliens:
        alien = random.choice(aliens)
        alien_laser = Actor("enemylaser",(alien.x,alien.y))
        aliens_lasers.append(alien_laser)

alien_pause = 50
alien_pause_count = 0
def update_aliens():
    global alien_pause, alien_pause_count, alien_speed
    if alien_pause_count < alien_pause:
        alien_pause_count += 1
    else:
        alien_pause_count = 0
        if alien_pause > 2:
            alien_pause -= 1
        change_direction = False
        for alien in aliens:
            if alien.image == "explosionpurple" or alien.image == "explosionblue" or alien.image == "explosiongreen":
                aliens.remove(alien)
            else:
                alien.x += alien_speed
                if alien.image == "enemy1_1": alien.image = "enemy1_2"
                elif alien.image ==  "enemy1_2": alien.image = "enemy1_1"
                if alien.image == "enemy2_1": alien.image = "enemy2_2"
                elif alien.image ==  "enemy2_2": alien.image = "enemy2_1"
                if alien.image == "enemy3_1": alien.image = "enemy3_2"
                elif alien.image ==  "enemy3_2": alien.image = "enemy3_1"
                if alien.left <= 0 or alien.right >= WIDTH:
                    change_direction = True
        if change_direction:
            alien_speed *= -1
            for alien in aliens:
                alien.y += 10
    if random.randint(1,100)<3:
        shoot_alien_laser()

def update_aliens_lasers():
    for alien_laser in aliens_lasers:
        alien_laser.y += alien_laser_speed
        if alien_laser.y >= HEIGHT:
            aliens_lasers.remove(alien_laser)

def check_collisions():
    global status
    for alien_laser in aliens_lasers:
        if alien_laser.colliderect(player):
            status = 2
        for shield in shields:
            if alien_laser.colliderect(shield):
                aliens_lasers.remove(alien_laser)
                if shield.image == "shield1": shield.image = "shield2"
                elif shield.image == "shield2":shield.image = "shield3"
                elif shield.image == "shield3":shield.image = "shield4"
                elif shield.image == "shield4": shields.remove(shield)
    for alien in aliens:
        if alien.colliderect(player):
            status = 2
    for laser in lasers:
        for alien in aliens:
            if laser.colliderect(alien):
                lasers.remove(laser)
                if alien.image == "enemy1_1" or alien.image == "enemy1_2":
                    alien.image = "explosionpurple"
                if alien.image == "enemy2_1" or alien.image == "enemy2_2":
                    alien.image = "explosionblue"
                if alien.image == "enemy3_1" or alien.image == "enemy3_2":
                    alien.image = "explosiongreen"
                aliens.remove(alien)
            if len(aliens) == 0:
                status = 1
        for shield in shields:
            if laser.colliderect(shield):
                lasers.remove(laser)

def update():
    if status == 0:
        update_player()
        update_lasers()
        update_aliens()
        update_aliens_lasers()
        check_collisions()

create_shields()
create_aliens()
pgzrun.go()