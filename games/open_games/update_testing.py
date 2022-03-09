#imports and starts the moduals needed to run the program
import pygame 
import sys

pygame.init()

#screen format
ratio = 16, 9
factor = 120

width, height = ratio[0]*factor, ratio[1]*factor
screen = pygame.display.set_mode((width, height))

#backround format
background_color = pygame.Color('lemonchiffon2')

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