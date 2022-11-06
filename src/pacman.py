import pygame

import spite
import variables
from spite import Spite


class Animate:
    __time: int = 0
    status: int = 0

    def __init__(self) -> None:
        self.speed = variables.ANIMATE_SPEED
        pass

    def run(self):
        self.__time += 1

        if self.__time % self.speed == 0:
            self.status += 1

        if self.status == 2:
            self.status = 0


class Pacman:
    animate: Animate
    status: str
    x: float
    y: float
    w: float
    h: float
    range_x: float
    range_y: float
    speed: float
    action: str

    surface: pygame.surface.Surface

    def __init__(self, x: float = 0, y: float = 0):
        img_w = variables.PACMAN_SURFACE_W
        img_h = variables.PACMAN_SURFACE_H
        w = variables.FRAME_W
        h = variables.FRAME_H
        

        image = pygame.image.load('assets/pacman.png')
        if image:
            image = pygame.transform.scale(image, (image.get_width(
            ) * variables.SCALE, image.get_height() * variables.SCALE))

        imgs: list[Spite] = []
        imgs.append(spite.Spite(0, 0, img_w, img_h))  # right 1
        imgs.append(spite.Spite(img_w, 0, img_w, img_h))  # right 2
        imgs.append(spite.Spite(img_w * 2, 0, img_w, img_h))  # left 1
        imgs.append(spite.Spite(img_w * 3, 0, img_w, img_h))  # left 2
        imgs.append(spite.Spite(img_w * 4, 0, img_w, img_h))  # up 1
        imgs.append(spite.Spite(img_w * 5, 0, img_w, img_h))  # up 2
        imgs.append(spite.Spite(img_w * 6, 0, img_w, img_h))  # right 1
        imgs.append(spite.Spite(img_w * 7, 0, img_w, img_h))  # right 2

        # define
        self.x = x
        self.y = y
        self.range_x = (img_w - w) / 2
        self.range_y = (img_h - h) / 2
        self.w = w
        self.h = h
        self.imgs = imgs
        self.status = 'right'
        self.animate = Animate()
        self.surface = image
        self.speed = variables.PACMAN_SPEED

    def draw(self, screen: pygame.surface.Surface):
        status = self.animate.status

        if self.status == 'left':
            status += 2
        if self.status == 'up':
            status += 4
        if self.status == 'down':
            status += 6

        current_image = self.imgs[status]

        # render
        screen.blit(self.surface, (self.x - self.range_x,
                    self.y - self.range_y), current_image.get())

        self.__run(screen)
        self.animate.run()

    def __run(self, screen: pygame.surface.Surface):
        w, h = screen.get_size()

        w -= self.w
        h -= self.h

        if self.status == 'left':
            if self.x - self.speed > 0:
                self.x -= self.speed
            elif self.x > 0:
                self.x = 0
        if self.status == 'right':
            if self.x + self.speed < w:
                self.x += self.speed
            elif self.x < w:
                self.x = w
        if self.status == 'up':
            if self.y - self.speed > 0:
                self.y -= self.speed
            elif self.y > 0:
                self.y = 0
        if self.status == 'down':
            if self.y + self.speed < h:
                self.y += self.speed
            elif self.y < h:
                self.y = h

    def set_status(self, status: str):
        if self.status == 'left' or self.status == 'right' or self.status == 'up' or self.status == 'down':
            self.status = status
