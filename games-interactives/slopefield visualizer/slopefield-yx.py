#imports and starts the moduals needed to run the program
import pygame
import sys
from dot import Dot
from pygame import Rect

pygame.init()

class Slopefield:

    #screen formatting
    ratio = 16, 9
    height = 720
    width = height * ratio[0] // ratio[1]
    screen = pygame.display.set_mode((width, height))
    screen_color = pygame.Color('darkgreen')

    clock = pygame.time.Clock()

    #game formatting
    dots = [Dot(3, (0, 0, 0), (0, 0, 0)), Dot(10, (0, 100, 0), (0, 0, 0))]


    @classmethod
    def update(cls):
        pygame.display.update()

    @classmethod
    def draw_dots(cls):
        for dot in cls.dots:
            l = dot.loc()
            l[0], l[1] = l[0] + cls.width//2, l[1] + cls.height//2
            pygame.draw.circle(cls.screen, dot.color, l, dot.size)

    @classmethod
    def update_dots(cls):
        for dot in cls.dots: dot.update(cls.clock.get_time())

    @classmethod
    def run(cls, debug = False):
        while True:
            if pygame.event.get(pygame.QUIT):
                sys.exit()

            #handles displaying and refreshing the screen after each evauluation
            cls.clock.tick(144)
            cls.screen.fill(cls.screen_color)
            cls.draw_dots()
            cls.update_dots()
            cls.update()

def main():
    Slopefield.run()

if __name__ == '__main__':
    main()