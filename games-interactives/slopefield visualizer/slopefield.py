# imports and starts the moduals needed to run the program
import pygame
import sys
import random
from pygame.math import Vector3 as V

pygame.init()


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    COLOR = pygame.Color('yellow')
    line_color = pygame.Color('black')
    clock = pygame.time.Clock()

    @classmethod
    def draw_grid(cls):
        pygame.draw.line(cls.screen, cls.line_color,
                         (cls.WIDTH//2, 0), (cls.WIDTH//2, cls.HEIGHT))
        pygame.draw.line(cls.screen, cls.line_color,
                         (0, cls.HEIGHT//2), (cls.WIDTH, cls.HEIGHT//2))


class Dots:
    pos = [V(0, 0, 0), V(100, 100, 0)]
    COLOR = pygame.Color('blue')
    radius = 10

    @classmethod
    def refill(cls, win: Window, value):
        while len(cls.pos) < value:
            cls.pos.append([random.randint(-Window.WIDTH//2, Window.WIDTH//2),
                            random.randint(-Window.HEIGHT//2, Window.HEIGHT//2)])

    @classmethod
    def draw(cls, win: Window):
        for coord in cls.pos:
            pygame.draw.circle(win.screen, cls.COLOR, (coord.x +
                               win.WIDTH//2, win.HEIGHT//2-coord.y), cls.radius)

    @classmethod
    def update(cls, win: Window):
        for coord in cls.pos:
            dt = win.clock.get_time() / win.MS_PER_SEC
            d = V(0, 0, 0)



# display loop
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    # handles displaying and refreshing the screen after each evauluation
    Window.clock.tick()
    Window.screen.fill(Window.COLOR)
    Window.draw_grid()
    Dots.draw(Window)
    pygame.display.update()
