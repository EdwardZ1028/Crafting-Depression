import pygame

class P_health:

    def __init__(self):
        self.image = pygame.image.load("Player.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1, self.image_size[1] * 1)
        self.image = pygame.transform.scale(self.image, scale_size)

    def damage_taken(self, hit_points):
        if hit_points == 2:
            self.image = pygame.image.load("Player.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 1, self.image_size[1] * 1)
            self.image = pygame.transform.scale(self.image, scale_size)
        if hit_points == 1:
            self.image = pygame.image.load("Player.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 1, self.image_size[1] * 1)
            self.image = pygame.transform.scale(self.image, scale_size)
        if hit_points == 0:
            self.image = pygame.image.load("Player.png")
            self.image_size = self.image.get_size()
            scale_size = (self.image_size[0] * 1, self.image_size[1] * 1)
            self.image = pygame.transform.scale(self.image, scale_size)