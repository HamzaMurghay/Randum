import pygame as pg
import pygame.sprite
from pygame.examples.midi import fill_region

# Setting Up Pygame Pre-requisites -----------------------------------------------------------------------------

screen = pg.display.set_mode((600, 600))
pg.display.set_caption("Elemental shooter game or smn")
clock = pg.time.Clock()

pg.init()

# Setting up Sprite Classes

class Zombie(pygame.sprite.Sprite):

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((36,36))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.health = 50
        self.health_bar = pg.Rect(x - 6, 555, self.health, 3)
        self.under_health_bar = pg.Rect(x - 6, 555, self.health, 3)

    def update(self):
        global zombie_kill_count, can_spawn, player_health

        if self.health <= 0:
            can_spawn = False
            zombie_kill_count += 1

        distance_from_player = abs(character_x - self.rect.x)

        if abs(character_x - (self.rect.x + 3)) < distance_from_player:
            self.rect.x += 3
        else:
            self.rect.x -= 3

        self.rect.x = self.rect.x

        if (self.rect.x <= character_x <= self.rect.x + 36 or self.rect.x <= character_x + 36 <= self.rect.x + 36) and 529 < character_y <= 565:
            player_health -= 5

        self.health_bar = pg.Rect(self.rect.x - 6, 555, self.health, 3)
        self.under_health_bar = pg.Rect(self.rect.x - 6, 555, self.health, 3)
        pygame.draw.rect(screen, "red", self.under_health_bar)
        pygame.draw.rect(screen, "green", self.health_bar)

        if self.health <= 0:
            self.kill()
            can_spawn = True

class Fireball(pygame.sprite.Sprite):

    def __init__(self, shoot_height, shoot_pos, direction):

        pygame.sprite.Sprite.__init__(self)
        self.y = shoot_height + 17
        self.x = shoot_pos
        self.direction = direction

    def update(self):
        global can_shoot

        travel = pg.time.get_ticks() - last_shot

        self.x = character_x + 17 + (travel * self.direction)
        self.y = character_y + 17

        pg.draw.circle(screen, "darkorange1", (self.x, self.y), 10)

        for zombie in zombies:
            if (zombie.rect.x <= self.x + 10 <= zombie.rect.x + 36 or zombie.rect.x <= self.y - 10 <= zombie.rect.x + 36) and 529 < self.y:
                zombie.health -= 17
                zombie.health_bar = pg.Rect(zombie.rect.x - 6, 555, zombie.health, 3)
                zombies.update()
                can_shoot = True
                self.kill()


        if character_x + (travel * self.direction) > 630 or character_x + (travel * self.direction) < -30:
            can_shoot = True
            self.kill()


zombies = pygame.sprite.Group()
fireballs = pygame.sprite.Group()

# Defining Run Time Variables ----------------------------------------------------------------------------------

game_font = pg.font.SysFont("SimSun", 20)

character_x = 200
character_y = 0

character_size_x = 35
character_size_y = 35

character_ground_level = 565

fall_velocity = 9.8 / 1000
jump_velocity = 4.9

to_jump = False

last_time_on_ground = pg.time.get_ticks()
last_time_jumped = -900

player_direction = 1

can_shoot = True
can_wall = True
last_shot = 0

shot_height = character_y
shot_pos = character_x

player_health = 100
player_healthbar_border = pg.Rect(82, 15, 104, 15)
player_healthbar = pg.Rect(84, 17, player_health, 11)

player_mana = 100
player_manabar_border = pg.Rect(63, 45, 104, 15)
player_manabar = pg.Rect(65, 47, player_mana, 11)

wall_direction = 1

mana_regen = 4
health_regen = 1

can_spawn = True

zombie_kill_count = 0


# Defining Functions -------------------------------------------------------------------------------------------


def handle_key_input():
    global character_x, character_y, to_jump, can_shoot, last_shot, player_health,  player_mana, shot_height, can_spawn, player_direction, can_wall, wall_direction
    keys = pg.key.get_pressed()

    if keys[pg.K_d]:
        character_x += 5
        if can_shoot: player_direction = 1
        if can_wall: wall_direction = 1
    if keys[pg.K_a]:
        character_x -= 5
        if can_shoot: player_direction = -1
        if can_wall: wall_direction = -1

    if keys[pg.K_SPACE] and character_y == character_ground_level:
        to_jump = True

    # Abilities

    if keys[pg.K_e] and len(fireballs) != 1 and player_mana >= 15:
        can_shoot = False
        last_shot = pg.time.get_ticks()
        player_mana -= 15

        fireball = Fireball(character_y, character_x, player_direction)
        fireballs.add(fireball)



    if keys[pg.K_q] and can_wall and player_mana >= 35:
        can_wall = False
        last_shot = pg.time.get_ticks()
        shot_pos = character_x

        player_mana -= 35

    if keys[pg.K_x] and can_spawn:
        zombie = Zombie("red", 500, 565)
        zombies.add(zombie)
        can_spawn = False


def implement_gravity():
    global character_y, last_time_on_ground, to_jump

    frame_fall_velocity = fall_velocity * (1 + pg.time.get_ticks() - last_time_on_ground)

    if character_y >= character_ground_level and not to_jump:
        last_time_on_ground = pg.time.get_ticks()
        character_y = character_ground_level
        return

    character_y += frame_fall_velocity - to_jump * jump_velocity

    if character_y >= character_ground_level: to_jump = False


def plant_wall(shot_position):
    global zombie_x, can_wall

    wall_x = shot_position + (40 * wall_direction)
    pg.draw.rect(screen, "gray", pg.Rect(wall_x, 536, 12, 64))

    if wall_x <= zombie_x <= wall_x + 14:
        zombie_x += 3

    if wall_x + 14 >= zombie_x + 36 >= wall_x:
        zombie_x -= 3

    if pg.time.get_ticks() - last_shot >= 1000:
        can_wall = True


def values_regen():
    global player_health, player_mana, player_manabar, player_healthbar

    if player_health < 100 and pg.time.get_ticks()%60 == 0:
        player_health += health_regen


    if player_mana < 100 and pg.time.get_ticks()%60 == 0:
        player_mana += mana_regen

    if player_mana > 100: player_mana = 100

    player_manabar = pg.Rect(65, 47, player_mana, 11)
    player_healthbar = pg.Rect(84, 17, player_health, 11)


def draw_elements():
    pg.draw.rect(screen, "purple", pg.Rect(character_x, character_y, 36, 36))

    if not can_shoot:
        fireballs.update()

    if not can_wall:
        plant_wall(shot_pos)

    if not can_spawn:
        zombies.draw(screen)
        zombies.update()


    game_health = game_font.render("Health: ", True, 'black')
    game_mana = game_font.render("Mana: ", True, 'black')
    game_score = game_font.render(f"Zombies Killed: {zombie_kill_count}", True, 'black')

    screen.blit(game_health, (10,10))
    screen.blit(game_mana, (10,40))
    screen.blit(game_score, (400, 10))


    pg.draw.rect(screen, "Black", player_healthbar_border, 2)
    pg.draw.rect(screen, "Green", player_healthbar)

    pg.draw.rect(screen, "Black", player_manabar_border, 2)
    pg.draw.rect(screen, "aqua", player_manabar)


    if player_health <= 0:
        screen.fill('White')
        screen.blit(game_font.render("Game Over!", True, "black"), (243, 222))
        screen.blit(game_score, (205, 245))


# Main Loop ----------------------------------------------------------------------------------------------------

while True:
    screen.fill('white')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    implement_gravity()
    handle_key_input()
    values_regen()

    draw_elements()

    pg.display.update()
    clock.tick(60)