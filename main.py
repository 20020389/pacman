import pygame

import src.variables as variables
from src.game_manager import GameManager, Topbar
from src.map import Map, load_map

pygame.init()

screen = pygame.display.set_mode((variables.WINDOW_W, variables.WINDOW_H))

running = True

pygame.display.set_caption('pacman')


# initial game variable
Map.init()

game_manager = GameManager()

map1 = load_map('map1')

topbar = Topbar(game_manager)



while running:
    pygame.time.wait(10)
    screen.fill((0, 0, 0))
    if game_manager.pacman_dead and not game_manager.new_life_pause.isFinish():
        game_manager.new_life_pause.run()
    elif game_manager.pacman_dead and game_manager.new_life_pause.isFinish():
        if game_manager.life > 1:
            game_manager.reset_on_dead()

    map1.draw(screen)
    game_manager.draw(screen, map1.map)
    topbar.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            game_manager.handle(event)

    pygame.display.update()

pygame.quit()
