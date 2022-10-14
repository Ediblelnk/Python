# imports and starts the moduals needed to run the program
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

  THIRD_H = W.HEIGHT//3
  THIRD_W = W.WIDTH//3

  t = [Object(V(THIRD_W, THIRD_H), V(y := 70, -y), x := 100, z := 10, a := C('orange')),
       Object(V(2*THIRD_W, THIRD_H), V(y, y), x//2, z, a),
       Object(V(THIRD_W, 2*THIRD_H), V(-y, -y), x//4, z, a)]
  """
  o = [Object(V(THIRD_W, THIRD_H), V(y := 70, -y), x := 10, z := 10, a := C('red')),
      Object(V(2*THIRD_W, THIRD_H), V(y, y), x, z, a),
      Object(V(THIRD_W, 2*THIRD_H), V(-y, -y), x, z, a),
      Object(V(2*THIRD_W, 2*THIRD_H), V(-y, y), x, z, a)]

  p = [Object(V(THIRD_W, THIRD_H), V(y := y-10, -y), x := 10, z := 10, a := C('orange')),
      Object(V(2*THIRD_W, THIRD_H), V(y, y), x, z, a),
      Object(V(THIRD_W, 2*THIRD_H), V(-y, -y), x, z, a),
      Object(V(2*THIRD_W, 2*THIRD_H), V(-y, y), x, z, a)]

  q = [Object(V(THIRD_W, THIRD_H), V(y := y-10, -y), x := 10, z := 10, a := C('yellow')),
      Object(V(2*THIRD_W, THIRD_H), V(y, y), x, z, a),
      Object(V(THIRD_W, 2*THIRD_H), V(-y, -y), x, z, a),
      Object(V(2*THIRD_W, 2*THIRD_H), V(-y, y), x, z, a)]

  r = [Object(V(THIRD_W, THIRD_H), V(y := y-10, -y), x := 10, z := 10, a := C('white')),
      Object(V(2*THIRD_W, THIRD_H), V(y, y), x, z, a),
      Object(V(THIRD_W, 2*THIRD_H), V(-y, -y), x, z, a),
      Object(V(2*THIRD_W, 2*THIRD_H), V(-y, y), x, z, a)]
  """  

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

      for i in [cls.t]:
        cls.all_update(cls.W.clock.get_time(), i)
        cls._normalize_positions(i)
        cls.all_draw(cls.W.screen, i)

      cls.W.update()

      

def main():
  Space.simulate()

if __name__ == '__main__':
  main()