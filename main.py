import pygame

import src.variables as variables
from src.game_manager import GameManager, Topbar
from src.map import Map, load_map
from src.pacman import Pacman

pygame.init()

screen = pygame.display.set_mode((variables.WINDOW_W, variables.WINDOW_H))

running = True

pygame.display.set_caption('pacman')


# initial game variable
Map.init()

game_manager = GameManager()

map1 = load_map('map1')

pacman = Pacman(game_manager, 13.5, 25)

topbar = Topbar(game_manager)

def init_entities() -> (Pacman):
    pacman = Pacman(game_manager, 13.5, 25)
    return pacman

while running:
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    if game_manager.pacman_dead and not game_manager.new_life_pause.isFinish():
        game_manager.new_life_pause.run()
    elif game_manager.pacman_dead and game_manager.new_life_pause.isFinish():
        game_manager.pacman_dead = False
        game_manager.decrease_life()
        game_manager.new_life_pause.reset()
        pacman = init_entities()

    map1.draw(screen)
    pacman.draw(screen, map1.map)
    topbar.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pacman.handle(event)

    pygame.display.update()

pygame.quit()
