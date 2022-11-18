
import pygame

from src.ghost import Ghost
from src.pacman import Pacman
from src.interface import Animate, Manager_Method
import src.variables as variables
from src.spite import Spite
from src.text import Text


class GameManager(Manager_Method):
    __life: int
    __score: int
    __pause: bool
    killing_pacman: bool
    pacman_dead: bool
    new_life_pause: Animate

    pacman: Pacman
    list_ghost: list[Ghost]  # tuple[, Ghost, Ghost, Ghost]

    def __init__(self) -> None:
        new_life_pause = Animate()
        new_life_pause.set_infinity(False)
        new_life_pause.set_delaytime(50)

        ghost_pink = Ghost(self, (12, 13), 0)
        ghost_red = Ghost(self, (12, 16), 1)
        ghost_blue = Ghost(self, (15, 13), 2)
        ghost_yellow = Ghost(self, (15, 16), 3)

        self.__life = 3
        self.__score = 0
        self.__pause = False
        self.killing_pacman = False
        self.pacman_dead = False
        self.new_life_pause = new_life_pause

        self.pacman = Pacman(self, 13.5, 25)
        self.list_ghost = [ghost_red, ghost_pink, ghost_blue, ghost_yellow]
        pass

    def draw(self, screen: pygame.surface.Surface, mapHash: list[list[int]] = []):
        for ghost in self.list_ghost:
            ghost.draw(screen, mapHash)
        self.pacman.draw(screen, mapHash)

    def handle(self, event: pygame.event.Event):
        self.pacman.handle(event)

    def reset_on_dead(self):
        self.pacman = Pacman(self, 13.5, 25)
        self.pacman_dead = False
        self.decrease_life()
        self.new_life_pause.reset()
        ghost_pink = Ghost(self, (12, 13), 0)
        ghost_red = Ghost(self, (12, 16), 1)
        ghost_blue = Ghost(self, (15, 13), 2)
        ghost_yellow = Ghost(self, (15, 16), 3)
        self.list_ghost = [ghost_red, ghost_pink, ghost_blue, ghost_yellow]

    def up_score(self, score: int):
        self.__score += score

    @property
    def score(self):
        return self.__score

    @property
    def life(self):
        return self.__life

    def decrease_life(self):
        self.__life = self.__life - 1

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, value: bool):
        self.__pause = value

    def set_killing_pacman(self, value: bool):
        self.killing_pacman = value

    def set_pacman_dead(self, value: bool):
        self.pacman_dead = value


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
            screen.blit(self.image, (10 + (img_size + 10)
                        * i, pacman_y), self.img_rect.get())

        self.scoreText.set_text(str(self.game_manager.score))
        self.scoreText.draw(screen)
