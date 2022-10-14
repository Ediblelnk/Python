# imports and starts the moduals needed to run the program
import pygame
from pygame import Vector2 as V2
from pygame import Color as C
import sys

pygame.init()


class Entity:

    def __init__(self, pos: V2, vel: V2, RADIUS: int, COLOR: str):
        self.RADIUS = RADIUS
        self.COLOR = C(COLOR)
        self.pos = pos
        self.vel = vel


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = C('black')
    MAX_FPS = 144

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    reference = Entity(V2(100, 100), V2(100, 0), 10, 'white')
    object = Entity(V2(600, 600), V2(0, 0), 10, 'red')

    Kp = 5
    Ki = 1
    Kd = 5

    @classmethod
    def tick(cls, fps=MAX_FPS):
        cls.clock.tick(fps)
        return cls

    @classmethod
    def draw(cls):
        for ent in (cls.reference, cls.object):
            pygame.draw.circle(cls.screen, ent.COLOR, ent.pos, ent.RADIUS)
        return cls

    @classmethod
    def ploop(cls, ref=reference, obj=object):
        obj.vel = ref.pos - obj.pos
        return cls

    @classmethod
    def pdloop(cls, ref=reference, obj=object):
        obj.vel = (ref.pos - obj.pos) * cls.Kp + (ref.pos - obj.pos) * \
            cls.clock.get_time() * cls.Kd
        return cls

    @classmethod
    def move(cls, entities: Entity):
        for ent in entities:
            ent.pos += cls.clock.get_time() * 1/1_000 * ent.vel
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
    print(Window.object.vel)
    if pygame.event.get(pygame.QUIT):
        sys.exit()

    Window.tick().fill().draw().move(
        (Window.object, Window.reference)).pdloop().update()
