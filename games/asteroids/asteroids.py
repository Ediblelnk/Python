#imports and starts the moduals needed to run the program
import pygame 
import sys
from asteroid_classes import Player
from asteroid_classes import Asteroid
from asteroid_classes import Saucer

pygame.init()

#screen format
ratio = 4, 3
factor = 1080/ratio[0]

width, height = ratio[0]*factor, ratio[1]*factor
screen = pygame.display.set_mode((width, height))
p = Player((0,0))

#backround format
background_color = pygame.Color('black')

#clock format
clock = pygame.time.Clock()

#display loop
while True:
	if pygame.event.get(pygame.QUIT):
		sys.exit()

	#handles displaying and refreshing the screen after each evauluation
	clock.tick()
	screen.fill(background_color)
	pygame.display.update()