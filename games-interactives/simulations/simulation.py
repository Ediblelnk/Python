# imports and starts the modules needed to run the program
import pygame
import sys
from pygame import Vector2 as V
from pygame import Color as C

pygame.init()


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = pygame.Color('darkslategray')
    MAX_FPS = 144

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    @classmethod
    def tick(cls, fps=MAX_FPS):
        cls.clock.tick(fps)
        return cls

    @classmethod
    def fill(cls, color=COLOR):
        cls.screen.fill(color)
        return cls

    @classmethod
    def update(cls, *rect_list):
        if not rect_list:
            pygame.display.update()
        else:
            try:
                pygame.display.update(rect_list)
            except ValueError:
                pygame.display.update(*rect_list)
        return cls


class Object:
    def __init__(self, position: V, velocity: V, mass: float, color: C):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.color = color

    def _update_pos(self, dt: int):
        self.position += self.velocity * dt / 1000


def main():
    while True:
        if pygame.event.get(pygame.QUIT):
            sys.exit()

        Window.tick().fill().update()


if __name__ == '__main__':
    main()
