
import pygame

import src.variables as variables
from src.spite import Spite
from src.text import Text


class GameManager:
    __life: int
    __score: int
    __pause: bool


    def __init__(self) -> None:
        self.__life = 3
        self.__score = 0
        self.__pause = False
        pass

    def up_score(self, score: int):
        self.__score += score

    @property
    def score(self):
        return self.__score

    @property
    def life(self):
        return self.__life

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, value: bool):
        self.__pause = value

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
