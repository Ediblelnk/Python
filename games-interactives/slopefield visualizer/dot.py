from pygame.math import Vector3 as Vect
from pygame import Color
from pygame import Rect

class Dot:
    def __init__(self, size, pos, vel):
        self.size = size
        self.pos = Vect(pos)
        self.vel = Vect(vel)
        self.color = Color('black')

    def update(self, tdelta):
        self.pos += self.vel * (tdelta / 1000)
    
    def loc(self, dimensions = 2):
        match dimensions:
            case 2: return [self.pos.x, self.pos.y*-1]
            case _: return self.pos.xyz

    def get_rect(self) -> Rect:
        s = self.size
        p = self.loc()
        return Rect(p[0]-s, p[1]-s, s*2, s*2)
    
    def new_vel(self, *new_vel):
        match len(new_vel):
            case 2: self.vel = Vect(*new_vel, 0)
            case 3: self.vel = Vect(*new_vel)

def main():
    d = Dot(4, (3, 2, 1), (4, 5, 6))
    print(d.loc())
    d.update()
    print(d.loc(2))

if __name__ == '__main__':
    main()