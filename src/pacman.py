import pygame

import src.spite as spite
import src.variables as variables


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
    x: int
    y: int
    w: int
    h: int
    range_x: int
    range_y: int
    speed: int
    action: str
    running: bool
    access = [45, 46, 47]

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

        imgs: list[spite.Spite] = []
        imgs.append(spite.Spite(0, 0, img_w, img_h))  # right 1
        imgs.append(spite.Spite(img_w, 0, img_w, img_h))  # right 2
        imgs.append(spite.Spite(img_w * 2, 0, img_w, img_h))  # left 1
        imgs.append(spite.Spite(img_w * 3, 0, img_w, img_h))  # left 2
        imgs.append(spite.Spite(img_w * 4, 0, img_w, img_h))  # up 1
        imgs.append(spite.Spite(img_w * 5, 0, img_w, img_h))  # up 2
        imgs.append(spite.Spite(img_w * 6, 0, img_w, img_h))  # right 1
        imgs.append(spite.Spite(img_w * 7, 0, img_w, img_h))  # right 2

        # define
        self.x = int(x * variables.FRAME_W)
        self.y = int(y * variables.FRAME_H)
        self.range_x = int((img_w - w) / 2)
        self.range_y = int((img_h - h) / 2)
        self.w = int(w)
        self.h = int(h)
        self.imgs = imgs
        self.status = 'right'
        self.animate = Animate()
        self.surface = image
        self.speed = variables.PACMAN_SPEED
        self.running = True
        self.action = 'right'

    def draw(self, screen: pygame.surface.Surface, mapHash: list[list[int]] = []):
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
        
        if (self.running):
            self.__run(screen, mapHash)
            self.animate.run()

    # xử lý sự kiện
    def handle(self, event: pygame.event.Event):
        if event.key == pygame.K_a:
            if self.action == 'right':
                self.set_status('left')
                self.action = 'left'
            else:
                self.action = 'left'
        if event.key == pygame.K_d:
            if self.action == 'left':
                self.set_status('right')
                self.action = 'right'
            else:
                self.action = 'right'
        if event.key == pygame.K_w:
            if self.action == 'down':
                self.set_status('up')
                self.action = 'up'
            else:
                self.action = 'up'
        if event.key == pygame.K_s:
            if self.action == 'up':
                self.set_status('down')
                self.action = 'down'
            else:
                self.action = 'down'
        if event.key == pygame.K_q:
            self.running = not self.running

    def __run(self, screen: pygame.surface.Surface, mapHash: list[list[int]] = []):
        w, h = screen.get_size()

        x: int = self.x
        y: int = self.y

        if self.status == 'left':
            if x - self.speed > 0:
                x -= self.speed
            elif x > 0:
                x = 0
        if self.status == 'right':
            if x + self.w + self.speed < w:
                x += self.speed
            elif x + self.w < w:
                x = w - self.w

        if self.status == 'up':
            if y - self.speed > 0:
                y -= self.speed
            elif y > 0:
                y = 0
        if self.status == 'down':
            if y + self.h + self.speed < h:
                y += self.speed
            elif y + self.h < h:
                y = h - self.h

        
        self.x = int(x)
        self.y = int(y)

        if self.same_frame():
            self.set_status(self.action)
            
    def same_frame(self):
        
        pos_x = self.x / int(variables.FRAME_W)
        pos_y = self.y / int(variables.FRAME_H)


        check_x = int(pos_x)
        check_y = int(pos_y)

        return abs(pos_x - check_x) < 0.01 and abs(pos_y - check_y) < 0.01

    def set_status(self, status: str):
        if self.status == 'left' or self.status == 'right' or self.status == 'up' or self.status == 'down':
            self.status = status
