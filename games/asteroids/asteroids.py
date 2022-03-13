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
p = Player((100, 100))
a = Asteroid((200,200))

#backround format
background_color = pygame.Color('grey')

#clock format
clock = pygame.time.Clock()

#display loop
while True:
	if pygame.event.get(pygame.QUIT):
		sys.exit()

	#handles displaying and refreshing the screen after each evauluation
	clock.tick()
	screen.fill(background_color)
	screen.blit(p.IMAGE, p.pos, p.IMAGE_LOCATION)
	screen.blit(a.IMAGE, a.pos, a.IMAGE_LOCATION)
	pygame.display.update()