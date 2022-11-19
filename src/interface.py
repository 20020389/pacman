import typing
import pygame
from abc import ABC, abstractmethod

import src.variables as variables


class Position:

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y
        pass

    def get(self):
        return self.x, self.y


class Manager_Method(ABC):
    @abstractmethod
    def draw(self, screen: pygame.surface.Surface, mapHash: list[list[int]] = []):
        pass

    @abstractmethod
    def handle(self, event: pygame.event.Event):
        pass

    @abstractmethod
    def reset_on_dead(self):
        pass

    @abstractmethod
    def up_score(self, score: int):
        pass

    @abstractmethod
    def make_ghostweak(self):
        pass

    @abstractmethod
    def get_weakanimate() -> typing.Any:
        pass

    @abstractmethod
    def is_ghostweak(self):
        pass

    @property
    def score(self):
        pass

    @property
    def life(self):
        pass

    def decrease_life(self):
        pass

    @property
    def pause(self):
        pass

    @pause.setter
    def pause(self, value: bool):
        pass

    @abstractmethod
    def set_killing_pacman(self, value: bool):
        pass

    @abstractmethod
    def set_pacman_dead(self, value: bool):
        pass


class Animate:
    def __init__(self) -> None:
        self.__delaytime = variables.ANIMATE_DELAYTIME
        self.__time: int = 0
        self.__status: int = 0
        self.__infinity: bool = True
        self.__limit: int = 2
        pass

    def run(self):
        self.__time += 1

        if self.__time % self.__delaytime == 0:
            if self.__status < self.__limit:
                self.__status += 1

        if self.__infinity and self.__status == self.__limit:
            self.__status = 0

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value: int):
        self.__limit = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: int):
        if value >= 0 and value <= 1:
            self.__status = value

    def set_infinity(self, value: bool):
        self.__infinity = value

    def isFinish(self):
        return self.__status == self.__limit

    def set_delaytime(self, value: int):
        self.__delaytime = value

    def get_delaytime(self):
        return self.__delaytime

    def reset(self):
        self.__status = 0
        self.__time = 0
