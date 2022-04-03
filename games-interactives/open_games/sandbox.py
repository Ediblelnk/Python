#imports and starts the moduals needed to run the program
import pygame 
import sys
import random

pygame.init()

#screen format
screenFactor = 50
screenWH = (int(16*screenFactor), int(9*screenFactor))
screen = pygame.display.set_mode((screenWH[0], screenWH[1]))

#backround format
backgroundColor = (0, 0, 0)

#clock format
clock = pygame.time.Clock()
clockRate = 144

#player format
playerXY = (screenWH[0]//2, screenWH[1]//2)
playerWH = (int(0.5*screenFactor), int(0.5*screenFactor))
playerColor = (255, 255, 255)
playerDraw = (playerXY[0], playerXY[1], playerWH[0], playerWH[1])

#display loop
gameover = False
while not gameover:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
			sys.exit()

	#handles displaying and refreshing the screen after each evauluation
	clock.tick()
	screen.fill(backgroundColor)
	pygame.draw.rect(screen, playerColor, (playerXY[0], playerXY[1], playerWH[0], playerWH[1]))
	pygame.display.flip()