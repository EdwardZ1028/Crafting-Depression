import pygame
import math


class P_attack_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("coin-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.4, self.image_size[1]*0.4)
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        degree = math.degrees(math.atan2(-self.dir[1], self.dir[0]))


class RedCoin:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("red-coin-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

