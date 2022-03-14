#imports and starts the moduals needed to run the program
import pygame 
import sys
from asteroid_classes import Player
from asteroid_classes import Asteroid
from asteroid_classes import Saucer
from pygame.math import Vector2

pygame.init()

#screen format
ratio = 4, 3
factor = 1440/ratio[0]

width, height = ratio[0]*factor, ratio[1]*factor
screen = pygame.display.set_mode((width, height))
p = Player((0, 0), (50, 50), 0, 50)

#backround format
background_color = pygame.Color('darkolivegreen')

#clock format
clock = pygame.time.Clock()

#display loop
while True:

	if pygame.event.get(pygame.QUIT):
		sys.exit()

	#handles displaying and refreshing the screen after each evauluation

	p.update(clock.get_time())

	clock.tick(144)
	screen.fill(background_color)
	screen.blit(p.get_image(), p.get_pos())
	pygame.display.update()