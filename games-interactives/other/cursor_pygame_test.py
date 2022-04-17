#imports and starts the moduals needed to run the program
import pygame 
import sys
import random

pygame.init()

#screen format
screenFactor = 50
screenWH = (int(16*screenFactor), int(9*screenFactor))
screen = pygame.display.set_mode((screenWH[0], screenWH[1]))

#clock format
clock = pygame.time.Clock()
clockRate = 1

#display loop
gameover = False
while not gameover:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
			sys.exit()

	#handles displaying and refreshing the screen after each evauluation
	pygame.mouse.set_pos([screenWH[0], 0])
	clock.tick(clockRate)