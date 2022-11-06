import pygame

import src.variables as variables
from src.map import Map
from src.pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((variables.FRAME_W * 28, variables.FRAME_H * 31))
running = True

pygame.display.set_caption('pacman')

# assets load
pacman_right = pygame.image.load('assets/sprites.png')

# initial map
Map.init()

map1 = Map([[2, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 44, 43, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1],
            [4, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46,
                26, 25, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 3],
            [4, 46, 24, 15, 15, 23, 46, 45, 45, 45, 45, 45, 45, 46,
                26, 25, 46, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 3],
            [4, 48, 26, 45, 45, 25, 46, 45, 45, 45, 45, 45, 45, 46,
             26, 25, 46, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 3],
            [4, 46, 28, 22, 22, 27, 46, 45, 45, 45, 45, 45, 45, 46,
             28, 27, 46, 45, 45, 45, 45, 45, 45, 45, 45, 45, 48, 3],
            [4, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46,
             46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 3],
            [4, 46, 24, 15, 15, 23, 46, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 46, 28, 22, 22, 27, 46, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 46, 46, 46, 46, 46, 46, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [6, 13, 13, 13, 13, 23, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 24, 14, 14, 14, 14, 5],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [12, 12, 12, 12, 12, 27, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 28, 12, 12, 12, 12, 12],
            [45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45],
            [13, 13, 13, 13, 13, 23, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 24, 14, 14, 14, 14, 14],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [45, 45, 45, 45, 45, 4, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 3, 45, 45, 45, 45, 45],
            [2, 12, 12, 12, 12, 27, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 28, 12, 12, 12, 12, 1],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [4, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
             45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 3],
            [6, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5]])

pacman = Pacman(200, 200)


while running:
    pygame.time.wait(10)
    screen.fill('#000000')
    

    map1.draw(screen)
    pacman.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pacman.set_status('left')
            if event.key == pygame.K_d:
                pacman.set_status('right')
            if event.key == pygame.K_w:
                pacman.set_status('up')
            if event.key == pygame.K_s:
                pacman.set_status('down')

    pygame.display.update()

pygame.quit()
