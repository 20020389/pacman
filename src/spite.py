import pygame

import src.variables as variables

image = pygame.image.load('assets/sprites.png')
if image:
    image = pygame.transform.scale(image, (image.get_width(
    ) * variables.SCALE, image.get_height() * variables.SCALE))

class Spite:
    def __init__(self, x: float | int, y: float | int, w: float | int, h: float | int):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)

    def get(self):
        return self.x, self.y, self.w, self.h
