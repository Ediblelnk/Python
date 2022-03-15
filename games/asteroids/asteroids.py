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
factor = 760/ratio[0]

width, height = ratio[0]*factor, ratio[1]*factor
screen = pygame.display.set_mode((width, height))
object1 = Asteroid((0, 0), (50, 50), 0, 50)
object2 = Player((width, 0), (-10, 10), 0, 0)

#backround format
background_color = pygame.Color('black')

#clock format
clock = pygame.time.Clock()

#display loop
while True:

	if pygame.event.get(pygame.QUIT):
		sys.exit()

	keydowns = pygame.event.get(pygame.KEYDOWN)
	keyups = pygame.event.get(pygame.KEYUP)
	object2.handle_keypresses(keydowns, keyups)

	#handles displaying and refreshing the screen after each evauluation

	object1.update(clock.get_time())
	object2.update(clock.get_time())

	clock.tick(144)
	screen.fill(background_color)
	screen.blit(object1.get_image(), object1.get_pos())
	screen.blit(object2.get_image(), object2.get_pos())
	pygame.display.update()