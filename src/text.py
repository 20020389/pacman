import os
from typing import Optional

import pygame
from pygame.font import Font
from pygame.surface import Surface

import src.variables as variables
from src.interface import Position


class Text:
    text: str
    _font: Font
    pos: Position

    def __init__(self, text: str, font: Optional[Font] = None) -> None:

        font_size = 20 * variables.SCALE
        if font:
            self._font = font
        else:
            self._font = pygame.font.Font(os.path.join(
                variables.ROOT_DIR, 'assets/font/Plaguard-ZVnjx.otf'), int(font_size))
        pass

        self.text = text
        self.pos = Position(0, 0)
        self.center = False
    pass

    def set_pos(self, pos: tuple[float, float]):
        self.pos = Position(pos[0], pos[1])
    
    def set_text(self, text: str):
        self.text = text

    def set_center(self, center: bool):
        self.center = center

    def draw(self, screen: Surface):
        img = self._font.render(self.text, True, 'WHITE')
        if not self.center:
            screen.blit(img, (self.pos.x, self.pos.y))
        else:
            img_w, img_h = img.get_size()
            screen.blit(img, (self.pos.x - img_w / 2, self.pos.y - img_h / 2))
