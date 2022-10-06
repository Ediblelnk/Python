# imports and starts the moduals needed to run the program
from math import floor
import pygame
import sys
from pygame import Vector2 as V
from pygame import Color as C

pygame.init()


class Window:
  RATIO = 1, 1
  HEIGHT = 540
  WIDTH = HEIGHT * RATIO[0] // RATIO[1]
  COLOR = pygame.Color('black')
  MAX_FPS = 120

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
  def __init__(self, position: V, velocity: V, mass: float, radius: int, color: C):
    self.position = position
    self.velocity = velocity
    self.mass = mass
    self.color = color
    self.radius = radius

  def _update_pos(self, dt: int):
    self.position += self.velocity * dt / 1000

  def _update_vel(self, dt: int, o):
    d: V = self.position - o.position
    r: float = d.length()
    d = d.normalize()

    a_mag: float = Space.G * o.mass / r*r
    a_vec: V = d * a_mag
    self.velocity -= a_vec * dt / 1000

  def update(self, dt: int, o):
    self._update_vel(dt, o)
    self._update_pos(dt)

  def draw(self, surface):
    pygame.draw.circle(surface, self.color, self.position, self.radius)

  def __eq__(self, obj):
    return self.position == obj.position

class Space:
  G = 10
  W: Window = Window()

  QUARTER_H = W.HEIGHT//4
  QUARTER_W = W.WIDTH//4
  HALF_H = W.HEIGHT//2
  HALF_W = W.WIDTH//2

  e = Object(V(HALF_W, HALF_H), V(0, 0), 81, 22, C('blue'))
  m = Object(V(QUARTER_W, HALF_H), V(0, 500), 1, 6, C('silver'))

  @classmethod
  def all_update(cls, dt, objects: list[Object]):
    for object_a in objects:
      for object_b in objects:
        if object_a != object_b:
          object_a.update(dt, object_b)

  @classmethod
  def all_draw(cls, screen, objects: list[Object]):
    for object in objects:
      object.draw(screen)

  @classmethod
  def _average_position(cls, objects: list[Object]) -> V:
    average = V(0, 0)
    for object in objects:
      average += object.position
    average = average/len(objects)
    return average

  @classmethod
  def _normalize_positions(cls, objects: list[Object]):
    average = cls._average_position(objects)
    win = V(cls.W.WIDTH//2, cls.W.HEIGHT//2)
    delta = average - win
    for object in objects:
      object.position = object.position - delta

  @classmethod
  def simulate(cls):
    running = True
    while running:
      if pygame.event.get(pygame.QUIT):
        sys.exit()

      cls.W.tick().fill()

      cls.m.update(cls.W.clock.get_time(), cls.e)
      cls.m.draw(cls.W.screen)
      cls.e.draw(cls.W.screen)

      e1 = 0.5 * cls.G * cls.e.mass * cls.m.mass / (cls.e.position - cls.m.position).length()
      print("ENERGY:", e1)

      cls.W.update()

      

def main():
  Space.simulate()

if __name__ == '__main__':
  main()