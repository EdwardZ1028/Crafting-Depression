import pygame


class Enemy_attack:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("enemy_attack.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.5, self.image_size[1] * 1.5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 4

    def move_to_e_1(self):
        self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
