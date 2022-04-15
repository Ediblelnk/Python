# imports and starts the moduals needed to run the program
import pygame
import sys

pygame.init()


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = pygame.Color('darkgreen')
    MAX_FPS = 144

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    @classmethod
    def tick(cls, fps=MAX_FPS):
        cls.clock.tick(fps)

    @classmethod
    def fill(cls, color=COLOR):
        cls.screen.fill(color)

    @classmethod
    def update(cls, *rect_list):
        if not rect_list:
            pygame.display.update()
        else:
            try:
                pygame.display.update(rect_list)
            except ValueError:
                pygame.display.update(*rect_list)


# display loop
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    Window.tick()
    Window.fill()
    Window.update()
