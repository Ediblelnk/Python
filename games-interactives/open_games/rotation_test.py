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
clockRate = 120

#player format
playerXYWH = [screenWH[0]//2, screenWH[1]//2, screenFactor//2, screenFactor//2]
playerColor = (255, 255, 255)
playerSpeed =  150 / clockRate
playerMove = 0
playerRotate = 0
playerVelocity = pygame.math.Vector2(1, 0)

#display loop
gameover = False
while not gameover:

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
			sys.exit()

	#movement request start logic
	if event.type == pygame.KEYDOWN: #handles keydowns
		
		if event.key == pygame.K_LEFT: #starts 'a' or 'left arrow' input
			playerRotate = 1

		if event.key == pygame.K_RIGHT: #starts 'd' or right arrow input
			playerRotate = -1

		if event.key == pygame.K_UP: #starts 'w' or 'up arrow' input
			playerMove = 1

		if event.key == pygame.K_DOWN: #starts 'd' or 'down arrow' input
			playerMove = -1

	#move request stop logic
	if event.type == pygame.KEYUP: #handles keydowns
		
		if event.key == pygame.K_LEFT: #starts 'a' or 'left arrow' input
			playerRotate = 0

		if event.key == pygame.K_RIGHT: #starts 'd' or right arrow input
			playerRotate = 0

		if event.key == pygame.K_UP: #starts 'w' or 'up arrow' input
			playerMove = 0

		if event.key == pygame.K_DOWN: #starts 'd' or 'down arrow' input
			playerMove = 0

	if playerRotate == 1:
		playerVelocity = playerVelocity.rotate(1)

	if playerRotate == -1:
		playerVelocity = playerVelocity.rotate(-1)


	if playerMove == 1:
		playerXYWH[0] += playerVelocity.x
		playerXYWH[1] -= playerVelocity.y

	if playerMove == -1:
		playerXYWH[0] -= playerVelocity.x
		playerXYWH[1] += playerVelocity.y


	#handles displaying and refreshing the screen after each evauluation
	clock.tick(clockRate)
	screen.fill(backgroundColor)
#	pygame.draw.rect(screen, playerColor, playerXYWH)
	pygame.draw.line(screen, (255,0,0), playerXYWH[:2], (playerXYWH[0]+playerVelocity.x*screenFactor, playerXYWH[1]-playerVelocity.y*screenFactor) , width=1)
	pygame.draw.line(screen, (255,255,255), playerXYWH[:2], (playerXYWH[0]-playerVelocity.x*screenFactor, playerXYWH[1]+playerVelocity.y*screenFactor) , width=1)
	pygame.display.update()