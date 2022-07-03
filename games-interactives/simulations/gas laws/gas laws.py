# imports and starts the moduals needed to run the program
import pygame
import sys

pygame.init()


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = pygame.Color('dark gray')
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


class Particle:

    def __init__(self, mass: float, radius: int, location: tuple, color: pygame.Color):
        self.mass = mass
        self.radius = radius
        self.location = location
        self.color = color


class Boundaries:
    t = 300
    w = Window
    COLOR = pygame.Color('blue')
    lines = {'left': t, 'right': w.WIDTH - t, 'top': t, 'bottom': w.HEIGHT - t}

    @classmethod
    def get_rects(cls) -> tuple:
        left = pygame.Rect(0, 0, cls.lines['left'], cls.w.HEIGHT)
        right = pygame.Rect(b:=cls.lines['right'], 0, cls.w.WIDTH - b, cls.w.HEIGHT)
        top = pygame.Rect(0, 0, cls.w.WIDTH, cls.lines['top'])
        bottom = pygame.Rect(0, b:=cls.lines['bottom'], cls.w.WIDTH, cls.w.HEIGHT - b)

        return (left, right, top, bottom)


class Simulation:
    pass


    # display loop

w = Window
p = Particle(5, 20, (w.WIDTH//2, w.HEIGHT//2), pygame.Color('pink'))
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    Window.tick().fill()
    for rect in Boundaries.get_rects():
        pygame.draw.rect(Window.screen, Boundaries.COLOR, rect)
    pygame.draw.circle(w.screen, p.color, p.location, p.radius)
    Window.update()
