import pygame

import variables

image = pygame.image.load('assets/sprites.png')
if image:
    image = pygame.transform.scale(image, (image.get_width(
    ) * variables.SCALE, image.get_height() * variables.SCALE))

print(image)

class Spite:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get(self):
        return self.x, self.y, self.w, self.h
