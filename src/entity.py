import pygame

from src.interface import Animate


class Entity(object):
    status: str
    x: float
    y: float
    w: float
    h: float
    range_x: float  # khoảng cách render giữa frame và image
    range_y: float
    speed: float
    action: str
    running: bool
    access: list[int]  # nhận biết những ô có thể di chuyển
    dead: bool

    animate: Animate
    dead_animate: Animate

    surface: pygame.surface.Surface
