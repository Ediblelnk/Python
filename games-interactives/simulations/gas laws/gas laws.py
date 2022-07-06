# imports and starts the moduals needed to run the program
from random import randint, random
import pygame
import sys

pygame.init()


class Window:
    RATIO = 16, 9
    HEIGHT = 720
    WIDTH = HEIGHT * RATIO[0] // RATIO[1]
    COLOR = pygame.Color('white')
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

    @classmethod
    def time_scalar(cls) -> float:
        return (cls.clock.get_time() / 1_000)


class Particle:

    def __init__(self, mass: float, radius: int, location: pygame.Vector2, vel: pygame.Vector2, color: pygame.Color):
        self.mass = mass
        self.radius = radius
        self.location = location
        self.vel = vel
        self.color = color
        self.BORDER_COLOR = pygame.Color('black')

    def update(self):
        self.location += self.vel * Window.time_scalar()


class Boundaries:
    t = 10
    w = Window
    COLOR = pygame.Color('black')
    lines = {'left': t, 'right': w.WIDTH - t, 'top': t, 'bottom': w.HEIGHT - t}
    vert_vel = 50
    hori_vel = 50
    actions = {'verticle': 0, 'horizontal': 0}

    @classmethod
    def get_rects(cls) -> tuple:
        left = pygame.Rect(0, 0, cls.lines['left'], cls.w.HEIGHT)
        right = pygame.Rect(
            b := (cls.lines['right']), 0, cls.w.WIDTH - b + 5, cls.w.HEIGHT)
        top = pygame.Rect(0, 0, cls.w.WIDTH, cls.lines['top'])
        bottom = pygame.Rect(
            0, b := (cls.lines['bottom']), cls.w.WIDTH, cls.w.HEIGHT - b + 5)

        return (left, right, top, bottom)

    @classmethod
    def use_down_input(cls, key: int) -> None:
        match(key):
            case pygame.K_UP:
                cls.actions['verticle'] = 1
            case pygame.K_DOWN:
                cls.actions['verticle'] = -1
            case pygame.K_LEFT:
                cls.actions['horizontal'] = 1
            case pygame.K_RIGHT:
                cls.actions['horizontal'] = -1

    @classmethod
    def use_up_input(cls, key: int) -> None:
        if key in (pygame.K_UP, pygame.K_DOWN):
            cls.actions['verticle'] = 0
        elif key in (pygame.K_LEFT, pygame.K_RIGHT):
            cls.actions['horizontal'] = 0

    @classmethod
    def update(cls):
        cls.lines['top'] += cls.vert_vel * \
            cls.actions['verticle'] * Window.time_scalar()
        cls.lines['bottom'] -= cls.vert_vel * \
            cls.actions['verticle'] * Window.time_scalar()
        cls.lines['left'] += cls.vert_vel * \
            cls.actions['horizontal'] * Window.time_scalar()
        cls.lines['right'] -= cls.vert_vel * \
            cls.actions['horizontal'] * Window.time_scalar()


class Simulation:

    global w
    w = Window
    p = [Particle(random(), 50, pygame.Vector2(60, 60), pygame.Vector2(randint(
        0, 1000), randint(0, 1000)), (randint(0, 255), randint(0, 255), randint(0, 255))) for x in range(1, 3)]

    @classmethod
    def run(cls):

        while True:
            Window.tick().fill()
            cls.detect_keys()
            for particle in cls.p:
                particle.update()
                pygame.draw.circle(w.screen, particle.color,
                                   particle.location, particle.radius)
                pygame.draw.circle(w.screen, particle.BORDER_COLOR,
                                   particle.location, particle.radius, width=2)
                cls.collision_handling(particle)
            cls.self_collision_handling(cls.p)
            Boundaries.update()

            for rect in Boundaries.get_rects():
                pygame.draw.rect(w.screen, Boundaries.COLOR, rect)

            Window.update()

    @classmethod
    def detect_keys(cls):

        if pygame.event.get(pygame.QUIT):
            sys.exit()

        keydowns = pygame.event.get(pygame.KEYDOWN)
        keyups = pygame.event.get(pygame.KEYUP)

        for keydown in keydowns:
            if keydown.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                Boundaries.use_down_input(keydown.key)
        for keyup in keyups:
            if keyup.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                Boundaries.use_up_input(keyup.key)

    @classmethod
    def collision_handling(cls, particle: Particle):
        if particle.location.x + particle.radius >= Boundaries.lines['right'] or particle.location.x - particle.radius <= Boundaries.lines['left']:
            particle.vel.x *= -1
        if particle.location.y + particle.radius >= Boundaries.lines['bottom'] or particle.location.y - particle.radius <= Boundaries.lines['top']:
            particle.vel.y *= -1

    @classmethod
    def self_collision_handling(cls, particles: list):
        for particle_a in particles:
            for particle_b in particles:
                if particle_a != particle_b:
                    if (particle_a.location - particle_b.location).length() <= particle_a.radius + particle_b.radius:
                        print('collision detected!!')


def main():
    Simulation.run()


if __name__ == '__main__':
    main()
