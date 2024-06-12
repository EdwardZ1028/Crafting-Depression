import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1, self.image_size[1] * 1)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0]*.5, self.image_size[1]*.5)
        self.delta = 4
        self.stop_max = False
        self.stop_min = False

    def move_direction(self, direction):
        if self.y > 200:
            self.stop_max = True
        else:
            self.stop_max = False
        if self.y < 540:
            self.stop_min = True
        else:
            self.stop_min = False

        if direction == "right":
            self.x = self.x + self.delta
        if direction == "left":
            self.x = self.x - self.delta
        if direction == "up" and self.stop_max is True:
            self.y = self.y - self.delta
        if direction == "down" and self.stop_min is True:
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_dash(self, direction):
        if direction == "right":
            self.x = self.x + self.delta * 50
        if direction == "left":
            self.x = self.x - self.delta * 50
