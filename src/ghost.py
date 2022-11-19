import random
import pygame

from src.pacman import Pacman
import src.entity as entity
import src.spite as spite
import src.variables as variables
from src.interface import Animate, Manager_Method


def format(value: float):
    return float("{0:.2f}".format(value))


class Ghost(entity.Entity):
    image: pygame.surface.Surface | None = None

    def __init__(self, manager: Manager_Method, position: tuple[float, float], type: int):
        running_img_w = variables.GHOST_SURFACE_W
        running_img_h = variables.GHOST_SURFACE_H

        dead_img_w = 28 * variables.SCALE
        dead_img_h = 28 * variables.SCALE

        w = variables.FRAME_W
        h = variables.FRAME_H

        ghost_type = type
        if type >= 0 and type <= 4:
            ghost_type *= variables.GHOST_SURFACE_H
        else:
            ghost_type = 0

        if not Ghost.image:
            image = pygame.image.load('assets/ghost.png')
            if image:
                image = pygame.transform.scale(image, (image.get_width(
                ) * variables.SCALE, image.get_height() * variables.SCALE))
            Ghost.image = image

        imgs_rect: list[spite.Spite] = []
        imgs_rect.append(spite.Spite(
            0, ghost_type, running_img_w, running_img_h))  # right 1
        imgs_rect.append(spite.Spite(running_img_w, ghost_type,
                         running_img_w, running_img_h))  # right 2
        imgs_rect.append(spite.Spite(running_img_w * 2,
                         ghost_type, running_img_w, running_img_h))  # left 1
        imgs_rect.append(spite.Spite(running_img_w * 3,
                         ghost_type, running_img_w, running_img_h))  # left 2
        imgs_rect.append(spite.Spite(running_img_w * 4,
                         ghost_type, running_img_w, running_img_h))  # left 2
        imgs_rect.append(spite.Spite(running_img_w * 5,
                         ghost_type, running_img_w, running_img_h))  # left 2
        imgs_rect.append(spite.Spite(running_img_w * 6,
                         ghost_type, running_img_w, running_img_h))  # left 2
        imgs_rect.append(spite.Spite(running_img_w * 7,
                         ghost_type, running_img_w, running_img_h))  # left 2

        # dead
        # imgs_rect.append(spite.Spite(dead_img_w * 8, 0, dead_img_w, running_img_h))
        imgs_rect.append(spite.Spite(dead_img_w * 0, 5 *
                         variables.GHOST_SURFACE_H, dead_img_w, dead_img_h))
        imgs_rect.append(spite.Spite(dead_img_w * 1, 5 *
                         variables.GHOST_SURFACE_H, dead_img_w, dead_img_h))
        imgs_rect.append(spite.Spite(dead_img_w * 2, 5 *
                         variables.GHOST_SURFACE_H, dead_img_w, dead_img_h))
        imgs_rect.append(spite.Spite(dead_img_w * 3, 5 *
                         variables.GHOST_SURFACE_H, dead_img_w, dead_img_h))

        dead_animate = Animate()
        dead_animate.limit = 11
        dead_animate.set_infinity(False)

        # define
        self.game_manager = manager
        self.x = int(position[0] * variables.FRAME_W)
        self.y = int(position[1] * variables.FRAME_H)
        self.range_x = int((running_img_w - w) / 2)
        self.range_y = int((running_img_h - h) / 2)
        self.w = int(w)
        self.h = int(h)
        self.imgs_rect = imgs_rect
        self.status = 'right'
        self.surface = Ghost.image
        self.speed = variables.GHOST_SPEED
        self.running = True
        self.action = 'right'
        self.access = [45, 46, 47, 48]
        self.animate = Animate()
        self.dead_animate = dead_animate
        self.dead = False
        self.timing = 0
        self.pacman: Pacman | None = None

    def draw(self, screen: pygame.surface.Surface, mapHash: list[list[int]] = []):
        status = self.animate.status

        if self.status == 'left':
            status += 2
        if self.status == 'up':
            status += 4
        if self.status == 'down':
            status += 6

        current_image = self.imgs_rect[status]

        # render
        if not self.dead:
            screen.blit(self.surface, (self.x - self.range_x,
                                       self.y - self.range_y), current_image.get())
            self.__run(screen, mapHash)

        if self.dead and not self.dead_animate.isFinish():
            status = self.dead_animate.status + 8
            current_image = self.imgs_rect[status]

            screen.blit(self.surface, (self.x - self.range_x,
                                       self.y - self.range_y), current_image.get())
            self.dead_animate.run()
            pass

        elif self.dead and self.dead_animate.isFinish():
            self.game_manager.set_killing_pacman(False)
            self.game_manager.set_pacman_dead(True)

        if self.running and not self.dead:
            self.animate.run()

    def can_move(self, map_hash: list[list[int]],  pos: tuple[float, float]):
        access = self.access

        topleft_x = pos[0] + 1
        topleft_y = pos[1] + 1

        bottomleft_x = pos[0]
        bottomleft_y = pos[1] + variables.FRAME_H - 1

        topright_x = pos[0] + variables.FRAME_W - 1
        topright_y = pos[1] + 1

        bottomright_x = topright_x
        bottomright_y = bottomleft_y

        # index
        topleft_j = int(topleft_x / variables.FRAME_W)
        topleft_i = int(topleft_y / variables.FRAME_H)

        bottomleft_j = int(bottomleft_x / variables.FRAME_W)
        bottomleft_i = int(bottomleft_y / variables.FRAME_H)

        topright_j = int(topright_x / variables.FRAME_W)
        topright_i = int(topright_y / variables.FRAME_H)

        bottomright_j = int(bottomright_x / variables.FRAME_W)
        bottomright_i = int(bottomright_y / variables.FRAME_H)

        try:
            access.index(map_hash[topleft_i][topleft_j])
            access.index(map_hash[bottomleft_i][bottomleft_j])
            access.index(map_hash[topright_i][topright_j])
            access.index(map_hash[bottomright_i][bottomright_j])
            return True
        except:
            return False

    # kiểm tra có thể di chuyển theo hướng khác k
    def check_way(self, screen: pygame.surface.Surface, map_hash: list[list[int]], way: str):
        x, y = self.x, self.y
        w, h = screen.get_size()
        if way != 'left' and way != 'right' and way != 'up' and way != 'down':
            way = 'right'

        if way == 'left':
            if x - self.speed > 0:
                x -= self.speed
            elif x > 0:
                x = 0
        if way == 'right':
            if x + self.w + self.speed < w:
                x += self.speed
            elif x + self.w < w:
                x = w - self.w

        if way == 'up':
            if y - self.speed > 0:
                y -= self.speed
            elif y > 0:
                y = 0
        if way == 'down':
            if y + self.h + self.speed < h:
                y += self.speed
            elif y + self.h < h:
                y = h - self.h

        return self.can_move(map_hash, (x, y))
    # xử lý sự kiện

    def eat(self, map_hash: list[list[int]]):
        center_x = self.x + variables.FRAME_W / 2
        center_y = self.y + variables.FRAME_H / 2

        i = int(center_y / variables.FRAME_H)
        j = int(center_x / variables.FRAME_W)

        # if map_hash[i][j] != 45:
        #     # kill pacman
        #     if map_hash[i][j] == 48:
        #         self.set_dead(True)
        #         self.game_manager.set_killing_pacman(True)

        #     if map_hash[i][j] == 46:
        #         self.game_manager.up_score(10)
        #     # chuyển đường đi có item thành đường đi thường
        #     map_hash[i][j] = 45
        # pass

    def new_way(self, screen: pygame.surface.Surface, map_hash: list[list[int]]):
        way = random.randrange(0, 4)
        if way == 0 and self.check_way(screen, map_hash, 'left'):
            self.status = 'left'
        if way == 1 and self.check_way(screen, map_hash, 'right'):
            self.status = 'right'
        if way == 2 and self.check_way(screen, map_hash, 'up'):
            self.status = 'up'
        if way == 3 and self.check_way(screen, map_hash, 'down'):
            self.status = 'down'

    def __run(self, screen: pygame.surface.Surface, map_hash: list[list[int]] = []):
        w, h = screen.get_size()

        x: float = self.x
        y: float = self.y

        if self.pacman != None and self.pacman_inside():
            self.pacman.set_dead(True)

        if self.status == 'left':
            x = self.__move_left(w)
        if self.status == 'right':
            x = self.__move_right(w)

        if self.status == 'up':
            y = self.__move_up(h)
        if self.status == 'down':
            y = self.__move_down(h)

        if self.can_move(map_hash, (x, y)):

            if self.running:
                self.x = x
                self.y = y
            else:
                self.running = True
        else:
            self.running = False
            self.animate.status = 1
            self.new_way(screen, map_hash)

        if self.same_frame():
            self.timing += 1

            if self.timing == 5:
                self.new_way(screen, map_hash)
                self.timing = 0

    def __move_right(self, w: float):
        x: float = self.x
        x = format(x)

        nextframe_j = (int(x / variables.FRAME_W) + 1) * variables.FRAME_W
        nextframe_j = format(nextframe_j)

        range_h = nextframe_j - x

        if self.speed < range_h:
            if x + self.w + self.speed < w:
                x += self.speed
            elif x + self.w < w:
                x = w - self.w
        else:
            x = nextframe_j
        return x

    def __move_left(self, w: float):
        x: float = self.x
        x = float("{0:.2f}".format(x))

        nextframe_j = (int(x / variables.FRAME_W)) * variables.FRAME_W
        nextframe_j = float("{0:.2f}".format(nextframe_j))

        range_h = x - nextframe_j

        if x == nextframe_j or self.speed < range_h:
            if x - self.speed > 0:
                x -= self.speed
            elif x > 0:
                x = 0
        else:
            x = nextframe_j
        return x

    def __move_up(self, h: float):
        y: float = self.y
        y = float("{0:.2f}".format(y))

        nextframe_i = (int(y / variables.FRAME_H)) * variables.FRAME_H
        nextframe_i = float("{0:.2f}".format(nextframe_i))

        range_v = y - nextframe_i

        if y == nextframe_i or self.speed < range_v:
            if y - self.speed > 0:
                y -= self.speed
            elif y > 0:
                y = 0
        else:
            y = nextframe_i
        return y

    def __move_down(self, h: float):
        y: float = self.y
        y = float("{0:.2f}".format(y))

        nextframe_i = (int(y / variables.FRAME_H) + 1) * variables.FRAME_H
        nextframe_i = float("{0:.2f}".format(nextframe_i))

        range_v = nextframe_i - y

        if self.speed < range_v:
            if y + self.h + self.speed < h:
                y += self.speed
            elif y + self.h < h:
                y = h - self.h
        else:
            y = nextframe_i
        return y

    def same_frame(self):

        pos_x = self.x / int(variables.FRAME_W)
        pos_y = self.y / int(variables.FRAME_H)

        check_x = int(pos_x)
        check_y = int(pos_y)

        return abs(pos_x - check_x) < 0.01 and abs(pos_y - check_y) < 0.01

    def set_status(self, status: str):
        if self.status == 'left' or self.status == 'right' or self.status == 'up' or self.status == 'down':
            self.status = status

    def set_dead(self, value: bool):
        self.dead = value

    def set_pacman(self, pacman: Pacman):
        self.pacman = pacman

    def pacman_inside(self):
        is_inside = self.is_inside
        """
        pacman
        """
        p = self.pacman
        if not p:
            return False

        p_topleft: tuple[float, float] = p.x, p.y
        p_topright: tuple[float, float] = p.x + p.w, p.y
        p_bottomleft: tuple[float, float] = p.x, p.y + p.h
        p_bottomright: tuple[float, float] = p.x + p.w, p.y + p.h

        return is_inside(p_topleft) or is_inside(p_topright) or is_inside(p_bottomleft) or is_inside(p_bottomright)
