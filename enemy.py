import pygame
import math

class Enemy:

    def __init__(self, x, y, move_to_x, move_to_y):
        self.delta = 5
        self.x = x
        self.y = y
        angle = math.atan2(move_to_y - y, move_to_x - x)
        self.dx = math.cos(angle) * self.delta
        self.dy = math.sin(angle) * self.delta

        self.image = pygame.image.load("Enemy.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0], self.image_size[1])
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_to(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
