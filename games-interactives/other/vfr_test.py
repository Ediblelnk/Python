#imports and starts the moduals needed to run the program
import pygame 
import sys
import random

pygame.init()

#pygame draw rectangle function
def pydrawRect(screen, rectColor, rectDraw):
	pygame.draw.rect(screen, rectColor, rectDraw)

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
playerXY = [screenWH[0]//2, screenWH[1]//2]
playerWH = [screenFactor//2, screenFactor//2]
playerColor = (255, 255, 255)
playerSpeed =  150 / clockRate
playerXMotion = ''
playerYMotion = ''

#display loop
gameover = False
while not gameover:

	#shorten pygame formalities
	playerDraw = (int(playerXY[0]), int(playerXY[1]), playerWH[0], playerWH[1])

	for event in pygame.event.get():
		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
			sys.exit()

	#movement request start logic
	if event.type == pygame.KEYDOWN: #handles keydowns
		
		if event.key == pygame.K_a or event.key == pygame.K_LEFT: #starts 'a' or 'left arrow' input
			playerXMotion = 'left'

		if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #starts 'd' or right arrow input
			playerXMotion = 'right'

		if event.key == pygame.K_w or event.key == pygame.K_UP: #starts 'w' or 'up arrow' input
			playerYMotion = 'up'

		if event.key == pygame.K_s or event.key == pygame.K_DOWN: #starts 's' or 'down arrow' input
			playerYMotion = 'down'

	#move request stop logic
	if event.type == pygame.KEYUP: #handles keydowns
		
		if event.key == pygame.K_a or event.key == pygame.K_LEFT: #starts 'a' or 'left arrow' input
			playerXMotion = ''

		if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #starts 'd' or right arrow input
			playerXMotion = ''

		if event.key == pygame.K_w or event.key == pygame.K_UP: #starts 'w' or 'up arrow' input
			playerYMotion = ''

		if event.key == pygame.K_s or event.key == pygame.K_DOWN: #starts 's' or 'down arrow' input
			playerYMotion = ''

	#movement execution
	if playerXMotion == 'left':
		playerXY[0] -= playerSpeed
	if playerXMotion == 'right':
		playerXY[0] += playerSpeed
	if playerYMotion == 'up':
		playerXY[1] -= playerSpeed
	if playerYMotion == 'down':
		playerXY[1] += playerSpeed

	#handles displaying and refreshing the screen after each evauluation
	clock.tick(clockRate)
	screen.fill(backgroundColor)
	pydrawRect(screen, playerColor, playerDraw)
	pygame.display.update()