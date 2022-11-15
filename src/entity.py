import pygame

from src.game_manager import GameManager
from src.interface import Animate


class Entity(object):
    status: str
    x: int
    y: int
    w: int
    h: int
    range_x: int  # khoảng cách render giữa frame và image
    range_y: int
    speed: int
    action: str
    running: bool
    access: list[int]  # nhận biết những ô có thể di chuyển
    dead: bool

    animate: Animate
    dead_animate: Animate

    surface: pygame.surface.Surface

    game_manager: GameManager