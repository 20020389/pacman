
import pygame

import src.variables as variables
from src.spite import Spite
from src.text import Text


class GameManager:
    life: int
    score: int

    def __init__(self) -> None:
        self.life = 3
        self.score = 0
        pass

    def up_score(self, score: int):
        self.score += score


class Topbar:

    def __init__(self, manager: GameManager) -> None:
        scoreText = Text(str(manager.score))
        scoreText.set_pos((variables.WINDOW_W / 2, variables.FRAME_H))
        scoreText.set_center(True)

        # asset
        image = pygame.image.load('assets/pacman.png')
        
        self.image = image
        self.img_rect = Spite(26, 0, 26, 26)

        self.scoreText = scoreText
        self.game_manager = manager
        pass

    def draw(self, screen: pygame.surface.Surface):
        manager = self.game_manager

        frame_h = variables.FRAME_H
        img_size = 26
        pacman_y = frame_h - img_size / 2
        for i in range(manager.life):
            screen.blit(self.image, (10 + (img_size + 10) * i, pacman_y), self.img_rect.get())
        

        self.scoreText.set_text(str(self.game_manager.score))
        self.scoreText.draw(screen)
