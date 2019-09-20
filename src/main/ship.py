import pygame as pg


class Ship(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.base_image = pg.image.load('png/Raumschiff1.png').convert_alpha()
        self.image = self.base_image
        self.position = position
        self.rotation = 0
        self.rotate(0)

    def rotate(self, angle):
        self.rotation += angle
        self.image = pg.transform.rotozoom(self.base_image, self.rotation, 0.3)
        self.rect = self.image.get_rect(center=self.position)
