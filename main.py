import pygame
import random
import math
import time
from player import Player
from enemy import Enemy
from player_attacks import P_attack_1



# set up pygame modules
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

start_message = "Use WASD to move , Right click to attack, and shift to dash!"
name = "Collect coins as fast as you can!"
win_message = "TIME'S UP!"
lose_message = "YOU LOSE!"
message = "Collision not detected"

number = random.randint(1, 3)
remainder = random.randint(0, 1)
current_time = time.time()
start_time = current_time
red_start_time = current_time
elapsed_time = 0
countdown = 10.00
score = 0
r = 50
g = 0
b = 100
collision = False
start = False

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_score_message = my_font.render("Score: " + str(score), True, (255, 255, 255))
display_start_message = my_font.render(start_message, True, (255, 255, 255))
display_win_message = my_font.render(win_message, True, (255, 255, 255))
display_lose_message = my_font.render(lose_message, True, (255, 255, 255))
display_elapsed_time = my_font.render("Time Left: " + str(countdown), True, (255, 255, 255))
f = Player(40, 60)
a_1 = P_attack_1(7, 7)
e = Enemy(200, 100)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    clock.tick(60)
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
        pygame.time.get_ticks
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            f.move_dash("right")
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_a]:
            f.move_dash("left")
            keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_w]:
            f.move_dash("up")
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_s]:
            f.move_dash("down")




    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            a_1 = P_attack_1(40, 60)

        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse position", event.pos, "Player position:", f.rect.x, f.rect.y)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            slope = (mouse_y - f.rect.y)/(mouse_x - f.rect.x)
            y_int = mouse_y - slope * mouse_x
            x_length = mouse_x - f.rect.x
            y_length = f.rect.y - mouse_y
            angle = math. atan(x_length / y_length)
            print(slope)
            print(y_int)
            print(angle)





    if start is False:

        current_time = time.time()
        start_time = current_time
        elapsed_time = 0
        countdown = 10.00
        score = 0
        display_score_message = my_font.render("Score: " + str(score), True, (255, 255, 255))
        f = Player(40, 60)
        e = Enemy(200, 100)
        screen.fill((r, g, b))
        screen.blit(display_start_message, (100, 250))
        pygame.display.update()

    if start is True:
        screen.fill((r, g, b))
        screen.blit(display_name, (0, 0))
        screen.blit(display_message, (0, 15))
        screen.blit(f.image, f.rect)
        screen.blit(e.image, e.rect)
        screen.blit(a_1.image, a_1.rect)
        pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
