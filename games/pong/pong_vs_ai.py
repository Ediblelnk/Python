#imports and starts the moduals needed to run the program
import pygame 
import sys
import random

pygame.init()

#returns -1 or 1
def addOrSubtractOneToTwo():
	scaler = random.randint(1, 2)
	sign = random.randint(0, 1)
	if sign == 0:
		sign = -1
	if sign == 1:
		pass
	return scaler*sign

#get random initial x speed, CANNOT be 0
def getRandomXSpeed():
	integer = random.randint(1, 3)
	sign = random.randint(0, 1)
	if sign == 0:
		sign = -1
	if sign == 1:
		pass
	integer = sign*integer
	return integer

#get random initial y speed, CAN be 0
def getRandomYSpeed():
	integer = random.randint(-3, 3)
	return integer

#ball movement function
def moveBall(gameStarted, ballXY, ballXYspeed):
	if gameStarted: #only move ball if gamestarts and moves according to ball speed
		ballXY[0] += ballXYspeed[0]
		ballXY[1] += ballXYspeed[1]

#keep players on the screen function
def playerBorder(playerXY, playerWH, screenWH):
	if playerXY[1] <= 0: #keeps the player inputed on the screen
			playerXY[1] = 0
	if playerXY[1] + playerWH[1] >= screenWH[1]:
		playerXY[1] = screenWH[1] - playerWH[1]

#test for ball-playerLeft collision, returns true if there is collision
def testBallPlayerCollision(playerLeftXY, playerRightXY, playerWH, ballXY, ballWH, gameBenefit):
	if playerLeftXY[1] + playerWH[1] + gameBenefit >= ballXY[1] + ballWH[1] and playerLeftXY[1] - gameBenefit <= ballXY[1] and not hitLeft: 
		if playerLeftXY[0] + playerWH[0] >= ballXY[0] and playerLeftXY[0] <= ballXY[0] + ballWH[0]:
			return True
	if playerRightXY[1] + playerWH[1] + gameBenefit >= ballXY[1] + ballWH[1] and playerRightXY[1] - gameBenefit <= ballXY[1] and not hitRight:
		if playerRightXY[0] <= ballXY[0] + ballWH[0] and playerRightXY[0] + playerWH[0] >= ballXY[0]:
			return True
		else:
			return False
	else:
		return False

#keep the ball on the screen function, bounce off of side walls and player
def ballBorder(ballXY, screenWH, ballXYspeed, ballWH, playerLeftXY, playerRightXY, playerWH, hitLeft, hitRight):
	if ballXY[1] <= 0 or ballXY[1] >= screenWH[1] - ballWH[1]: #bounces the ball off the top and bottom of the screen
		ballXYspeed[1] = - ballXYspeed[1]
	if testBallPlayerCollision(playerLeftXY, playerRightXY, playerWH, ballXY, ballWH, gameBenefit):
		if abs(ballXYspeed[0]) != ballXYspeed[0]: #bounce ball off players
			if not hitLeft:
				ballXYspeed[0] = - (ballXYspeed[0] - 1)
				ballXYspeed[1] += addOrSubtractOneToTwo()
				hitLeft = True
				hitRight = False
		if abs(ballXYspeed[0]) == ballXYspeed[0] and not hitLeft:
			if not hitRight:
				ballXYspeed[0] = - (ballXYspeed[0] + 1)
				ballXYspeed[1] += addOrSubtractOneToTwo()
				hitLeft = False
				hitRight = True

#request size factor
sizeFactor = 0
while not sizeFactor >= 1 and sizeFactor <= 3:
	sizeFactor = int(input("\nWhat size would you like to window?\n"
					"options are 1, 2, or 3:\n"))

#request AI difficulty
AIdifficulty = str(input("What difficulty would you like the AI to be?\n"
				"options are impossible, hard, medium, easy, stupid easy:\n"))

#set default AI variance
AIvariance = 50*sizeFactor
#set AI variance according to input
if AIdifficulty.startswith('i'):
	#set variance for imposible difficulty
	AIvariance = 0*sizeFactor
elif AIdifficulty.startswith('h'):
	#set variance for hard difficulty
	AIvariance = 15*sizeFactor
elif AIdifficulty.startswith('m'):
	#set variance for medium difficulty
	AIvariance = 40*sizeFactor
elif AIdifficulty.startswith('e'):
	#set variance for easy difficulty
	AIvariance = 70*sizeFactor
elif AIdifficulty.startswith('s'):
	#set variance for stupid easy difficulty
	AIvariance = 90*sizeFactor

#game loop
gameRunning = True
while gameRunning:

	#color format
	brown = (160, 82, 45)
	black = (0, 0, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)
	green = (0, 255, 0)
	white = (255, 255, 255)
	yellow = (255, 255, 0)

	#screen format
	screenWH = [512*sizeFactor, 256*sizeFactor]
	screen = pygame.display.set_mode((screenWH[0], screenWH[1]))
	screenColor = black

	#game format
	gameStarted = False
	gameWinner = ''
	gameSpeed = 60
	gameBenefit = 5*sizeFactor
	hitLeft = False
	hitRight = False
	scoreLeft = 0
	scoreRight = 0

	#font format
	fontColor = white
	myFont = pygame.font.Font(r"pong\bit5x3.ttf", 36*sizeFactor)

	#clock format
	clock = pygame.time.Clock()
	clockRate = gameSpeed 

	#AI format
	AIposition = 0
	AIballprediction = screenWH[1]//2
	AIballpredictionMade = False

	#player format
	playerWH = [6*sizeFactor, 48*sizeFactor]
	playerSpeed = 5*sizeFactor

	#playerLeft format
	playerLeftXY = [4*playerWH[0], screenWH[1]//2 - playerWH[1]//2]
	playerLeftColor = white
	playerLeftDirection = ''

	#playerRight format
	playerRightXY = [screenWH[0] - playerWH[0] - 4*playerWH[0], (screenWH[1] - playerWH[1])//2]
	playerRightColor = white
	playerRightDirection = ''

	#ball format
	ballWH = [10*sizeFactor, 10*sizeFactor]
	ballXY = [(screenWH[0] - ballWH[0])//2, (screenWH[1] - ballWH[1])//2]
	ballXYspeed = [getRandomXSpeed()*sizeFactor, getRandomYSpeed()*sizeFactor]
	ballColor = red

	#display loop
	gameOver = False
	while not gameOver:

		#round loop
		roundOver = False
		while not roundOver:

			for event in pygame.event.get(): #keeps the screen alive until the 'x' button is pressed
				if event.type == pygame.QUIT:
					sys.exit()

			if event.type == pygame.KEYDOWN: #handles keydowns
				
				if event.key == pygame.K_UP: #playerLeft wants to go up
					playerLeftDirection = 'up'

				if event.key == pygame.K_DOWN: #playerLeft wants to go down
					playerLeftDirection = 'down'

			if event.type == pygame.KEYUP: #handles keyups

				if event.key == pygame.K_UP or event.key == pygame.K_DOWN: #playerLeft wants to stop moving
					playerLeftDirection = ''

			if not playerLeftDirection == '': #playerLeft movement logic
				gameStarted = True
				if playerLeftDirection == 'up':
					playerLeftXY[1] -= playerSpeed
				elif playerLeftDirection == 'down':
					playerLeftXY[1] += playerSpeed

			if not playerRightDirection == '': #playerRight movement logic
				if playerRightDirection == 'up':
					playerRightXY[1] -= playerSpeed
				elif playerRightDirection == 'down':
					playerRightXY[1] += playerSpeed

			moveBall(gameStarted, ballXY, ballXYspeed) #move ball according to its speed components

			#keep players on the screen
			playerBorder(playerLeftXY, playerWH, screenWH)
			playerBorder(playerRightXY, playerWH, screenWH)

			#keep ball between top and bottom of the screen and bouncing off players
			ballBorder(ballXY, screenWH, ballXYspeed, ballWH, playerLeftXY, playerRightXY, playerWH, hitLeft, hitRight)	

			#move AI according to ball location and difficulty
			if not AIballpredictionMade:
				if ballXYspeed[0] > 0:
					AIballprediction = (ballXY[1] + ballWH[1]//2) + ballXYspeed[1]*((playerRightXY[0] - ballXY[0])//ballXYspeed[0])

					while AIballprediction < 0 or AIballprediction > screenWH[1]:
						if AIballprediction < 0:
							AIballprediction *= -1
						if AIballprediction > screenWH[1]:
							AIballprediction -= screenWH[1]
							AIballprediction = screenWH[1] - AIballprediction

					#vary the AIballprediction based on difficulty
					AIballprediction += random.randint(-AIvariance, AIvariance)
					AIballpredictionMade = True

			#resets the ball prediction after hit by playerLeft
			if ballXYspeed[0] < 0:
				AIballpredictionMade = False

			#move playerRight according to prediction
			if playerRightXY[1] + 2*playerWH[1]//3 < AIballprediction:
				playerRightDirection = 'down'
			if playerRightXY[1] + playerWH[1]//3 > AIballprediction:
				playerRightDirection = 'up'
			if playerRightXY[1] + 2*playerWH[1]//3 > AIballprediction and playerRightXY[1] + playerWH[1]//3 < AIballprediction:
				playerRightDirection = ''

			#when a ball goes passed one of the goals, the round is over
			if ballXY[0] + ballWH[0] <= 0:
				scoreRight += 1
				playerRightColor = green
				roundOver = True
			if ballXY[0] >= screenWH[0]:
				scoreLeft += 1
				playerLeftColor = green
				roundOver = True

			#handles displaying and refreshing the screen after each evauluation
			clock.tick(clockRate)
			screen.fill(screenColor)

			#draw score
			text = f"{scoreLeft} : {scoreRight}"
			textXY = list(myFont.size(text))
			label = myFont.render(text, False, fontColor)
			screen.blit(label, ((screenWH[0] - textXY[0])//2 , 10*sizeFactor))

			#draw figures on the screen
			pygame.draw.rect(screen, playerLeftColor, (playerLeftXY[0], playerLeftXY[1], playerWH[0], playerWH[1]))
			pygame.draw.rect(screen, playerRightColor, (playerRightXY[0], playerRightXY[1], playerWH[0], playerWH[1]))
			pygame.draw.rect(screen, ballColor, (ballXY[0], ballXY[1], ballWH[0], ballWH[1]))

			#update the display
			pygame.display.update()

		#round over loop
		while roundOver:

			#end game if score is greater than or equal to 10
			if scoreLeft >= 10:
				gameWinner = 'left'
				gameOver = True
			if scoreRight >= 10:
				gameWinner = 'right'
				gameOver = True

			for event in pygame.event.get(): #keeps the screen alive until the 'x' button is pressed
				if event.type == pygame.QUIT:
					sys.exit()

			#starts a new round if return/enter is pressed
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_RETURN: #resets the court for the new round

					#reset ball location and speed
					ballXY = [(screenWH[0] - ballWH[0])//2, (screenWH[1] - ballWH[1])//2]
					ballXYspeed = [getRandomXSpeed()*sizeFactor, getRandomYSpeed()*sizeFactor]

					#reset playerLeft direction requests and position
					playerLeftDirection = ''
					playerLeftColor = white
					playerLeftXY = [4*playerWH[0], screenWH[1]//2 - playerWH[1]//2]

					#reset playerRight direction requests and position
					playerRightDirection = ''
					playerRightColor = white
					playerRightXY = [screenWH[0] - playerWH[0] - 4*playerWH[0], (screenWH[1] - playerWH[1])//2]

					#reset game state
					gameStarted = False
					roundOver = False

			#handles displaying and refreshing the screen after each evauluation
			clock.tick(clockRate)
			screen.fill(screenColor)

			#draw score
			text = f"{scoreLeft} : {scoreRight}"
			textXY = list(myFont.size(text))
			label = myFont.render(text, False, fontColor)
			screen.blit(label, ((screenWH[0] - textXY[0])//2 , 10*sizeFactor))

			#draw figures on the screen
			pygame.draw.rect(screen, playerLeftColor, (playerLeftXY[0], playerLeftXY[1], playerWH[0], playerWH[1]))
			pygame.draw.rect(screen, playerRightColor, (playerRightXY[0], playerRightXY[1], playerWH[0], playerWH[1]))
			pygame.draw.rect(screen, ballColor, (ballXY[0], ballXY[1], ballWH[0], ballWH[1]))

			#update the screen
			pygame.display.update()

	#game over loop
	while gameOver:

		for event in pygame.event.get(): #keeps the screen alive until the 'x' button is pressed
				if event.type == pygame.QUIT:
					sys.exit()

		#starts a new round if return/enter is pressed
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_RETURN: #resets the court for the new round
				gameRunning = False
				
		#makes the winner green
		if gameWinner == 'left':
			playerLeftColor = blue
		if gameWinner == 'right':
			playerRightColor = blue

		#handles displaying and refreshing the screen after each evauluation
		clock.tick(clockRate)
		screen.fill(screenColor)

		#draw score
		text = f"{scoreLeft} : {scoreRight}"
		textXY = list(myFont.size(text))
		label = myFont.render(text, False, fontColor)
		screen.blit(label, ((screenWH[0] - textXY[0])//2 , 10*sizeFactor))

		#draw figures on the screen
		pygame.draw.rect(screen, playerLeftColor, (playerLeftXY[0], playerLeftXY[1], playerWH[0], playerWH[1]))
		pygame.draw.rect(screen, playerRightColor, (playerRightXY[0], playerRightXY[1], playerWH[0], playerWH[1]))
		pygame.draw.rect(screen, ballColor, (ballXY[0], ballXY[1], ballWH[0], ballWH[1]))

		#update the screen
		pygame.display.update()

#keep the game running
while not gameRunning:
	gameRunning = True