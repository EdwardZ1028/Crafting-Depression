import pygame
import math


class P_attack_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("P_Attack (1).png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.4, self.image_size[1]*0.4)
        self.pos = (x, y)
        self.delta = .3
