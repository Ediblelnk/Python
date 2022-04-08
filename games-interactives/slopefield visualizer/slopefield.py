# imports and starts the moduals needed to run the program
import pygame
import sys
import random
from pygame.math import Vector3 as V

pygame.init()


class Window:
    RATIO = 3, 2, 3
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    DEPTH = HEIGHT * RATIO[0] // RATIO[2]
    COLOR = pygame.Color('yellow')
    MS_PER_SEC = 1000
    TIME_FACTOR = 1
    TICK_RATE = 144
    MAX_DOTS = 700
    DOTS_PER_SECOND = round(MAX_DOTS)
    ZOOM = HEIGHT/3

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    line_color = pygame.Color('black')
    clock = pygame.time.Clock()

    @classmethod
    def draw_grid(cls):
        pygame.draw.line(cls.screen, cls.line_color,
                         (cls.WIDTH//2, 0), (cls.WIDTH//2, cls.HEIGHT))
        pygame.draw.line(cls.screen, cls.line_color,
                         (0, cls.HEIGHT//2), (cls.WIDTH, cls.HEIGHT//2))

    @classmethod
    def tick(cls):
        cls.clock.tick(cls.TICK_RATE)

    @classmethod
    def get_sec(cls):
        return cls.clock.get_time() / cls.MS_PER_SEC


class Dots:
    ps = [V(0, 0, 0)]
    COLOR = pygame.Color('black')
    radius = 3

    @classmethod
    def refill(cls, win: Window, value):
        while len(cls.ps) < value:
            rx, ry, rz = random.random()*2 - 1, random.random() * \
                2 - 1, random.random()*2 - 1
            cls.ps.append(V(rx * win.WIDTH/win.ZOOM, ry *
                          win.HEIGHT/win.ZOOM, rz * win.DEPTH/win.ZOOM))

    @classmethod
    def prune(cls, win: Window, value: int | float):
        value *= win.get_sec()
        value = round(value)
        for _ in range(value):
            if cls.ps:
                cls.ps.pop(0)

    @classmethod
    def draw(cls, win: Window):
        for p in cls.ps:
            pygame.draw.circle(win.screen, cls.COLOR, (p.x * win.ZOOM +
                               win.WIDTH//2, win.HEIGHT//2 - p.y * win.ZOOM), cls.radius)

    @classmethod
    def update(cls, win: Window):
        for p in cls.ps:
            dt = win.get_sec() * win.TIME_FACTOR
            d = V(0, 0, 0)
            #d.x, d.y, d.z = (p.y-p.x) * dt, (p.x*(10 - p.z) - p.y) * dt, p.x * p.y - p.z
            d.x, d.y, d.z = dt, p.x**2 * dt, 0
            p += d


# display loop
while True:

    if pygame.event.get(pygame.QUIT):
        sys.exit()

    # handles displaying and refreshing the screen after each evauluation
    Window.tick()
    Window.screen.fill(Window.COLOR)
    Window.draw_grid()
    Dots.update(Window)
    Dots.refill(Window, Window.MAX_DOTS)
    Dots.prune(Window, Window.DOTS_PER_SECOND)
    Dots.draw(Window)
    pygame.display.update()
