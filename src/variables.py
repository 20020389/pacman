import os

SCALE = 1.5
FRAME_W = 16 * SCALE
FRAME_H = 16 * SCALE

WINDOW_W = FRAME_W * 28
WINDOW_H = FRAME_H * 33

PACMAN_SURFACE_W = 26 * SCALE
PACMAN_SURFACE_H = 26 * SCALE
PACMAN_SPEED = 2

GHOST_SURFACE_W = 28 * SCALE
GHOST_SURFACE_H = 28 * SCALE
GHOST_SPEED = 2.1

# animate
ANIMATE_DELAYTIME = 10  # càng nhỏ hiệu ứng càng nhanh
_DIRNAME = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(_DIRNAME, '..')
