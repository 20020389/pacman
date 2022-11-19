import pygame

from src.interface import Animate


class Entity(object):

    def __init__(self) -> None:
        self.status: str
        self.x: float
        self.y: float
        self.w: float
        self.h: float
        self.range_x: float  # khoảng cách render giữa frame và image
        self.range_y: float
        self.speed: float
        self.action: str
        self.running: bool
        self.access: list[int]  # nhận biết những ô có thể di chuyển
        self.dead: bool

        self.animate: Animate
        self.dead_animate: Animate

        self.surface: pygame.surface.Surface
        pass
