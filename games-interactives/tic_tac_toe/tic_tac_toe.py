# imports and starts the moduals needed to run the program
import pygame
import sys

pygame.init()


class Window:
    RATIO = 1, 1
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = pygame.Color('black')
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


# display loop
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    Window.tick().fill().update()
