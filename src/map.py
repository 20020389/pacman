import pygame

import src.variables as variables
from src.spite import Spite


class Map:
    # static
    path: list[Spite] = []
    w: float
    h: float

    img: pygame.surface.Surface
    map: list[list[int]]

    @staticmethod
    def init():
        w = 16 * variables.SCALE
        h = 16 * variables.SCALE
        img = pygame.image.load('assets/frame.png').convert_alpha()

        if img:
            img = pygame.transform.scale(
                img, (img.get_width() * variables.SCALE, img.get_height() * variables.SCALE))

        Map.img = img
        for i in range(4):
            for j in range(16):
                Map.path.append(Spite(j * w, i * h, w, h))
        Map.w = w
        Map.h = h

    def __init__(self, initial: list[list[int]]):
        self.map = initial

    def draw(self, screen: pygame.surface.Surface):
        # print('---------------start----------------')
        # for i in range(len(Map.path)):
        #     print(Map.path[i].get())
        # print('---------------stop----------------')
        map_data = self.map
        for i in range(len(map_data)):
            for j in range(len(map_data[i])):
                index = map_data[i][j] - 1
                screen.blit(Map.img, (Map.w * j, Map.h * i),
                            Map.path[index].get())
