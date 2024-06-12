import pygame
import random
import math
import time
from player import Player
from enemy import Enemy
from player_attacks import P_attack_1
from enemy_attack import Enemy_attack



# set up pygame modules
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Eras Demi ITC', 15)
start_font = pygame.font.SysFont('Eras Demi ITC', 25)
cooldown_font = pygame.font.SysFont('Eras Demi ITC', 20)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
start_message_1 = "Use WASD to move , Right click to attack, and shift to dash (WIP)"
start_message_2 = "RULES -->"
start_message_3 = "Use r to reset and t to start"
lose_message = "You Lose!"
name = "Collect coins as fast as you can!"
win_message = "You Win! (Use r to reset and t to start)"
lose_message = "YOU LOSE!"
message = "Collision not detected"

number = random.randint(1, 3)
remainder = random.randint(0, 1)
start_time = 0
elapsed_time = 0
countdown = 10.00
score = 0
r = 50
g = 0
b = 100
hit_points = 3
boss_hp = 1000
collision = False
start = False
boss_move = True
cd_message = False
win = False
attacks = []
e_attacks = []
cooldown_P_attk = []
cooldown_P_attk.append(0)
cooldown_P_dash = []
cooldown_P_dash.append(0)

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_score_message = my_font.render("Score: " + str(score), True, (255, 255, 255))
display_start_message = start_font.render(start_message_1, True, (255, 255, 255))
display_start_message_2 = start_font.render(start_message_2, True, (255, 255, 255))
display_start_message_3 = start_font.render(start_message_3, True, (255, 255, 255))
display_hit_points = my_font.render("Health: " + str(hit_points), True, (255, 255, 255))
display_boss_hp = my_font.render("Health: " + str(boss_hp), True, (255, 255, 255))
display_win_message = start_font.render(win_message, True, (255, 255, 255))
display_lose_message = my_font.render(lose_message, True, (255, 255, 255))
display_elapsed_time = my_font.render("Time Left: " + str(countdown), True, (255, 255, 255))
f = Player(40, 60)
a_1 = P_attack_1(7, 7, 7, 7)
e = Enemy(200, 100, 7, 7)
e_1 = Enemy_attack(100, 200)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    clock.tick(60)
    current_time = time.time()
    elapsed_time = current_time - start_time

    keys = pygame.key.get_pressed()
    if keys[pygame.K_t]:
        start = True
    if keys[pygame.K_r]:
        start = False

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        f.move_direction("right")
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_a]:
        f.move_direction("left")
        keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_w]:
        f.move_direction("up")
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_s]:
        f.move_direction("down")


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        cd_message = False
        cooldown_P_dash.append(pygame.time.get_ticks())
        if cooldown_P_dash[0] - cooldown_P_dash[1] == 500:
            keys = pygame.key.get_pressed()  # checking pressed keys
            if keys[pygame.K_d]:
                f.move_dash("right")
                cooldown_P_dash.remove(cooldown_P_dash[0])
            keys = pygame.key.get_pressed()  # checking pressed keys
            if keys[pygame.K_a]:
                f.move_dash("left")
                cooldown_P_dash.remove(cooldown_P_dash[0])
        else:
            cooldown_P_dash.remove(cooldown_P_dash[0])
            cd_message = True



    if boss_move == False and elapsed_time % 2 == 1:
        boss_move = True

    if boss_move == True:
        move_to_x = random.randint(100, 1100)
        move_to_y = random.randint(100, 600)
        e = Enemy(e.rect.x, e.rect.y, move_to_x, move_to_y)
        boss_move = False

    if random.randint(1, 30) == 15 and start is True:
        x = random.randint(-50, 1100)
        e_1 = Enemy_attack(x, 0)
        e_attacks.append(e_1)

    if f.rect.colliderect(e_1) and start is True:
        hit_points -= 1
        display_hit_points = my_font.render("(WIP) Health: " + str(hit_points), True, (255, 255, 255))

    if a_1.rect.colliderect(e) and start is True:
        boss_hp -= 1
        display_boss_hp = my_font.render("Boss Health: " + str(boss_hp), True, (255, 255, 255))

    if boss_hp == 0:
        win = True

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            cooldown_P_attk.append(pygame.time.get_ticks())
            print(cooldown_P_attk)
            if cooldown_P_attk[1] - cooldown_P_attk[0] >= 400:
                target_x, target_y = pygame.mouse.get_pos()
                a_1 = P_attack_1(f.rect.centerx/1.2, f.rect.centery/1.5, target_x, target_y)
                attacks.append(a_1)
                cooldown_P_attk.remove(cooldown_P_attk[0])
                print(cooldown_P_attk)
            else:
                cooldown_P_attk.remove(cooldown_P_attk[0])
                print(cooldown_P_attk)







    if start is False:

        current_time = time.time()
        start_time = current_time
        boss_hp = 1000
        win = False
        elapsed_time = 0
        hit_points = 3
        countdown = 10.00
        score = 0
        display_score_message = my_font.render("Score: " + str(score), True, (255, 255, 255))
        f = Player(450, 400)
        e = Enemy(200, 100, 7, 7)
        screen.fill((r, g, b))
        screen.blit(display_start_message, (250, 400))
        screen.blit(display_start_message_3, (400, 300))
        screen.blit(display_start_message_2, (525, 200))
        pygame.display.update()

    if start is True and win is False:
        screen.fill((r, g, b))
        screen.blit(display_name, (0, 0))
        screen.blit(display_message, (0, 15))
        screen.blit(display_hit_points, (0, 30))
        screen.blit(display_boss_hp, (0, 45))
        for e_1 in e_attacks:
            e_1.move_to_e_1()
            screen.blit(e_1.image, e_1.rect)
        for a_1 in attacks:
            a_1.move()
            screen.blit(a_1.image, a_1.rect)
        screen.blit(f.image, f.rect)
        screen.blit(e.image, e.rect)
        pygame.display.update()

    if start is True and win is True:
        screen.fill((r, g, b))
        screen.blit(display_win_message, (400, 300))
        pygame.display.update()



# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
