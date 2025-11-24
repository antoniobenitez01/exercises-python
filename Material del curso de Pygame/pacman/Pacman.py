import pgzrun

TITLE = "Pac-Man"

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 2, 2, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

tiles = ["empty", "wall", "empty"]

TILE_SIZE = 32
MAZE_SIZE = len(maze)
WIDTH = TILE_SIZE * MAZE_SIZE
HEIGHT = TILE_SIZE * MAZE_SIZE + 20

def get_position(x,y):
    return (x * TILE_SIZE + TILE_SIZE / 2, y * TILE_SIZE + TILE_SIZE / 2)

pacman = Actor("pacman-right", pos=get_position(1,1))
ghost1 = Actor("ghost1", pos=get_position(8,7))
ghost2 = Actor("ghost2", pos=get_position(7,8))
ghost3 = Actor("ghost3", pos=get_position(7,7))
ghost4 = Actor("ghost4", pos=get_position(8,8))

walls = []
pellets = []
total_pellets = 0
score = 0
status = 0
pacman_speed = 4

def draw_maze():
    global total_pellets
    for x in range (0,MAZE_SIZE,1):
        for y in range (0, MAZE_SIZE, 1):
            if maze[y][x] == 1:
                wall = Actor("wall",get_position(x,y))
                walls.append(wall)
            if maze[y][x] == 0:
                pellet = Actor("pellet",get_position(x,y))
                pellets.append(pellet)
                total_pellets += 1

def draw():
    screen.clear()
    if status == 1:
        screen.draw.text("YOU WIN!",(WIDTH // 2, HEIGHT // 2), fontsize = 40, color = "green")
    elif status == 2:
        screen.draw.text("GAME OVER", (WIDTH // 2, HEIGHT // 2), fontsize=40, color="red")
    else:
        pacman.draw()
        ghost1.draw()
        ghost2.draw()
        ghost3.draw()
        ghost4.draw()
        for wall in walls:
            wall.draw()
        for pellet in pellets:
            pellet.draw()
        screen.draw.text(f"Score: { score }", (10, HEIGHT - 20), fontsize = 20, color = "yellow")

def check_collision(x,y):
    actor_rect = Rect((x,y),(29,29))
    for wall in walls:
        wall_rect = Rect ((wall.x,wall.y),(32,32))
        if actor_rect.colliderect(wall_rect):
            return True
    return False

def update_pacman():
    if keyboard.left and not check_collision(pacman.x - pacman_speed, pacman.y):
        pacman.x -= pacman_speed
        pacman.image = "pacman-left"
    elif keyboard.right and not check_collision(pacman.x + pacman_speed, pacman.y):
        pacman.x += pacman_speed
        pacman.image = "pacman-right"
    elif keyboard.up and not check_collision(pacman.x, pacman.y - pacman_speed):
        pacman.y -= pacman_speed
        pacman.image = "pacman-up"
    elif keyboard.down and not check_collision(pacman.x, pacman.y + pacman_speed):
        pacman.y += pacman_speed
        pacman.image = "pacman-down"
    else:
        pacman.x = ((pacman.x // TILE_SIZE) * TILE_SIZE) + (TILE_SIZE // 2)
        pacman.y = ((pacman.y // TILE_SIZE) * TILE_SIZE) + (TILE_SIZE // 2)

def update_pellets():
    global score, total_pellets, status
    for pellet in pellets:
        if pellet.colliderect(pacman):
            pellets.remove(pellet)
            score += 1
            if score == total_pellets:
                status = 1

def update_ghost(ghost, ghost_speed):
    global status
    if pacman.x < ghost.x and not check_collision(ghost.x - ghost_speed, ghost.y):
        ghost.x = ghost.x - ghost_speed
    elif pacman.x > ghost.x and not check_collision(ghost.x + ghost_speed, ghost.y):
        ghost.x = ghost.x + ghost_speed
    elif pacman.y < ghost.y and not check_collision(ghost.x, ghost.y - ghost_speed):
        ghost.y = ghost.y - ghost_speed
    elif pacman.y > ghost.y and not check_collision(ghost.x, ghost.y + ghost_speed):
        ghost.y = ghost.y + ghost_speed
    if ghost.colliderect(pacman):
        status = 2

def update():
    if status == 0:
        update_pacman()
        update_pellets()
        update_ghost(ghost1,3)
        update_ghost(ghost2,2)
        update_ghost(ghost3,1)
        update_ghost(ghost4,4)

draw_maze()
pgzrun.go()