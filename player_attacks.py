import pygame


class P_attack_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("coin-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*0.4, self.image_size[1]*0.4)

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


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

