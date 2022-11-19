from __future__ import annotations
import pygame

from src.interface import Animate


class Entity:

    def __init__(self) -> None:
        self.status: str
        self.x: float = 0
        self.y: float = 0
        self.w: float = 0
        self.h: float = 0
        self.range_x: float  # khoảng cách render giữa frame và image
        self.range_y: float
        self.speed: float
        self.action: str
        self.running: bool
        self.access: list[int]  # nhận biết những ô có thể di chuyển
        self.dead: bool

        self.animate: Animate

        self.surface: pygame.surface.Surface
        pass

    def is_inside(self, point: tuple[float, float]):
        point_x = point[0]
        point_y = point[1]

        return point_x >= self.x and point_x <= self.x + self.w and point_y >= self.y and point_y <= self.y + self.h
