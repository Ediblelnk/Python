# imports and starts the moduals needed to run the program
import math
import pygame
import sys
from pygame import Vector2 as V

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


class Pendulum:
    def __init__(self, pivot: V, position: V, gravity: V, color: pygame.Color):
        self.pivot = pivot
        self.pos = pivot + position
        self.vel = V(0, 0)
        self.LENGTH = position.length()
        self.COLOR = color
        self.GRAVITY = gravity

    def draw(self, dest: pygame.Surface):
        pygame.draw.line(dest, self.COLOR, self.pivot, self.pos, width=3)
        pygame.draw.circle(dest, self.COLOR, self.pos, 5)
        pygame.draw.line(dest, pygame.Color('black'), self.pos, self.pos+self.GRAVITY, width=3)
        pygame.draw.line(dest, pygame.Color('red'), self.pos, self.pos+self.tension, width=3)
        return self

    @property
    def _phi(self):
        return (self.pivot-self.pos).as_polar()[1] - 180
    
    @property
    def _r(self):
        return (self.GRAVITY * math.cos(self._phi)).length()

    @property
    def tension(self):
        i = V(0, 0)
        i.from_polar((self._r, self._phi))
        return i.rotate(180)

    def update(self, dt: int):
        self.vel += (self.GRAVITY + self.tension) * dt / 1000
        self._control_length()
        self.pos += self.vel * dt / 1000
        return self

    def _control_length(self):
        i = V(0, 0)
        i.from_polar((self.LENGTH, self._phi))
        self.pos = self.pivot + i

# display loop
p = Pendulum(V(Window.WIDTH//2, Window.HEIGHT//4), V(-200, 0), V(0, 50), pygame.Color('white'))
while True:
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    Window.tick().fill()
    p.update(Window.clock.get_time()).draw(Window.screen)
    Window.update()
