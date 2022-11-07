import os

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
                if index != -1:
                    screen.blit(Map.img, (Map.w * j, Map.h * i),
                                Map.path[index].get())
                else:
                    screen.blit(Map.img, (Map.w * j, Map.h * i),
                                Map.path[44].get())


def load_map(name: str) -> Map:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(ROOT_DIR, str.format("../assets/map/{}.txt", name))
    file_data = open(map_path, 'r')

    map_hash: list[list[int]] = []
    i = 0

    for line in file_data:
        list_data = line.split(',')
        map_hash.append([])
        for num in list_data:
            try:
                map_hash[i].append(int(num))
            except:
                pass
        i += 1
    # print(map_hash)
    return Map(map_hash)
