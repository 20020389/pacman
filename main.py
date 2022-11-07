import pygame

import src.variables as variables
from src.map import Map, load_map
from src.pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((variables.WINDOW_W, variables.WINDOW_H))
running = True

pygame.display.set_caption('pacman')

# assets load
pacman_right = pygame.image.load('assets/sprites.png')

# initial map
Map.init()

map1 = load_map('map1')

pacman = Pacman(13.5, 25)


while running:
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    

    map1.draw(screen)
    pacman.draw(screen, map1.map)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pacman.handle(event)

    pygame.display.update()

pygame.quit()
