#imports and starts the moduals needed to run the program
import pygame 
import sys

pygame.init()

#screen format
ratio = 16, 9

height = 720
width = height * ratio[0] // ratio[1]

screen = pygame.display.set_mode((width, height))

#backround format
background_color = pygame.Color('darkgreen')

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