#imports and starts the moduals needed to run the program
import pygame 
import sys

pygame.init()

#screen format
width = 960
height = 540
screen = pygame.display.set_mode((width, height))

#backround format
background_color = (0,0,0)

#clock format
clock = pygame.time.Clock()
clock_rate = 60

#display loop
gameover = False
while not gameover:
	for event in pygame.event.get():

		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
			sys.exit()

	#handles displaying and refreshing the screen after each evauluation
	clock.tick(clock_rate)
	screen.fill(background_color)
	pygame.display.update()