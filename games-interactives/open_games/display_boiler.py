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


# display loop
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    # handles displaying and refreshing the screen after each evauluation
    Window.clock.tick()
    Window.screen.fill(Window.COLOR)
    pygame.display.update()
