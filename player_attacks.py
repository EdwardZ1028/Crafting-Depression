import math
import pygame


class P_attack_1:

    def __init__(self, x, y, target_x, target_y):
        self.delta = 5
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = math.cos(angle) * self.delta
        self.dy = math.sin(angle) * self.delta
        self.x = x
        self.y = y
        self.image = pygame.image.load("P_Bullet_1 (1).png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(x, y, self.image_size[0]*0.4, self.image_size[1]*0.4)

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
