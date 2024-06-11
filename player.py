import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .9, self.image_size[1] * .9)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 5

    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_dash(self, direction):
        if direction == "right":
            self.x = self.x + self.delta * 50
        if direction == "left":
            self.x = self.x - self.delta * 50
        if direction == "up":
            self.y = self.y - self.delta * 50
        if direction == "down":
            self.y = self.y + self.delta * 50
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
