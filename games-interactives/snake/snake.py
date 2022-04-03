#imports and starts the moduals needed to run the program
import pygame 
import sys
import os
import random

pygame.init()

#draws the snake
def drawItems(snake, display, block, apple, scoreBox):
	#draw scorebox
	pygame.draw.rect(display, scoreBox['color'], (scoreBox['XY'][0], scoreBox['XY'][1] , scoreBox['width'], scoreBox['height']), 0, factor)
	pygame.draw.rect(display, scoreBox['border color'], (scoreBox['XY'][0], scoreBox['XY'][1] , scoreBox['width'], scoreBox['height']), factor//5, factor)
	#draw apple
	pygame.draw.rect(display, apple['color'], (apple['XY'][0]+block//6, apple['XY'][1]+block//6, snake['size'], snake['size']), 0, factor)
	#draw snake head
	pygame.draw.rect(display, snake['headcolor'], (snake['body'][0][0]+block//6, snake['body'][0][1]+block//6, snake['size'], snake['size']), 0, factor)
	#draw entire snake body
	for segment in snake['body'][1:]:
		pygame.draw.rect(display, snake['color'], (segment[0]+block//6, segment[1]+block//6, snake['size'], snake['size']), factor*4//5, factor)

#moves snake according to direction requests and body segments
def snakeMove(snake):
	#replace each element in snakebody with segment in front of it, but keep head the same
	if snake['direction'] != 'none':
		snake['body'].insert(1, snake['body'][0][:]) #[:] to assign value, but not bind addresses
		del snake['body'][-1]

	#move snakehead according to direction request
	if snake['direction'] == 'left':
		snake['body'][0][0] -= snake['step']
	elif snake['direction'] == 'right':
		snake['body'][0][0] += snake['step']
	elif snake['direction'] == 'up':
		snake['body'][0][1] -= snake['step']
	elif snake['direction'] == 'down':
		snake['body'][0][1] += snake['step']

#adds a segment at the end of the snake
def snakeAddJoint(snake):
	snake['body'].append(snake['body'][-1][:])

#moves the location of the apple
def newApple(apple, snakebody):
	apple['XY'] = [block*random.randint(0, columns-1), block*random.randint(0, rows-2)] #-2 because of scoreBox
	if apple['XY'] in snakebody:
		newApple(apple, snakebody)

#test if the snake head is on the apple
def testAppleEat(appleXY, snakeheadXY):
	if appleXY == snakeheadXY:
		return True
	return False

#tests if the snake is going to hit the edge of the screen
def testBoundries(snake, screenW, screenH):
	if snake['direction'] == 'left' and snake['body'][0][0] - snake['step'] < 0:
		return True #snake hitting left wall condition
	elif snake['direction'] == 'right' and snake['body'][0][0] + snake['step'] + factor >= screenW:
		return True #snake hitting right wall condition
	elif snake['direction'] == 'up' and snake['body'][0][1] - snake['step'] < 0:
		return True #snake hitting top wall condition
	elif snake['direction'] == 'down' and snake['body'][0][1] + snake['step'] + factor >= screenH - block:
		return True #snake hitting botton wall condition
	else:
		return False #snake is not in risk of hitting a wall, yay!

#test if the snake is going to collide with itself
def testSnakeCollision(snake):
	snakebody = snake['body'][1:]
	snakehead = snake['body'][0][:] #want a copy, do not want to edit the original
	if snake['direction'] == 'left':
		snakehead[0] -= snake['step']
		if snakehead in snakebody:
			return True #snake hitting itself from the right
	elif snake['direction'] == 'right':
		snakehead[0] += snake['step']
		if snakehead in snakebody:
			return True #snake hitting itself from the left
	elif snake['direction'] == 'up':
		snakehead[1] -= snake['step']
		if snakehead in snakebody:
			return True #snake hitting itself from below
	elif snake['direction'] == 'down':
		snakehead[1] += snake['step']
		if snakehead in snakebody:
			return True #snake hitting itself from above
	else:
		return False

#draws text
def drawText(text, xPos, yPos):
	result = font['font'].render(text, True, font['color'])
	display.blit(result, (xPos, yPos))

def setGameOver():
	global gameover
	gameover = True
	screen['color'] = colors['grey']
	if score > high:
		scorenew = open(os.path.join(os.path.dirname(__file__), r"high_score.txt"), 'w')
		scorenew.write(str(score))
		scorenew.close()

#color dictionary
colors = {'black': (0,0,0), 'white': (255,255,255), 'red': (255,0,0), 'forest': (34, 94, 51),
		  'body white': (255,255,255), 'grey':(31,31,31)}

#game variables
factor = 8	#size factor of the game
columns = 20	#number of columns
rows = 10		#number of rows
difficulty = 9/10 	#if 1, difficulty remains the same throughout run
					#closer to 0, the harder
					#kinda breaks the game if above 1

#prevent game from being run with unviable variables
assert rows > 2
assert columns*factor >= 20 and columns >= 10

#box pixel size
block = factor*6

while(True):

	#clock format
	clock = pygame.time.Clock()
	clockRate = 100
	clockTimer = clockRate // 4 #divisor is base number of movements each second
	clockPosition = 0
	movement = False
	recentMovement = 'right'

	#score format
	score = 0
	hightext = open(os.path.join(os.path.dirname(__file__), r"high_score.txt"))
	high = int(hightext.read())
	hightext.close()

	#snake dictionary
	snake = {'body': [[block*3,block*1],[block*2,block*1],[block*1,block*1]], 'color': colors['body white'], 'headcolor': colors['white'],
			 'size': block*5//6, 'direction': 'none', 'step': block}
		#first index of body is segment, next is x or y of that segment

	apple = {'XY': [block*random.randint(4, columns-1), block*random.randint(0, rows-2)], 'color': colors['red'], 'size': block*5//6}

	#screen dictionary
	screen = {'width': block*columns + block//6, 'height': block*rows + block//6, 'color': colors['forest']}
	display = pygame.display.set_mode((screen['width'], screen['height']))
	scoreBox = {'XY': (0, screen['height']-block), 'width': screen['width'], 'height': block, 'color': colors['black'], 'border color': colors['white']}
	font = {'color': colors['white'], 'font': pygame.font.Font(os.path.join(os.path.dirname(__file__), r"OBLIVIOUSFONT.TTF"), 5*factor)}

	#display loop
	gameover = False
	while not gameover:

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()

		#process movment requests, cannot directly move in opposite to what is currently movment direction
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and recentMovement != 'right': #left movement request
				snake['direction'] = 'left'
			elif event.key == pygame.K_RIGHT and recentMovement != 'left': #right movement request
				snake['direction'] = 'right'
			elif event.key == pygame.K_UP and recentMovement != 'down': #up movement request
				snake['direction'] = 'up'
			elif event.key == pygame.K_DOWN and recentMovement != 'up': #down movement request
				snake['direction'] = 'down'

		#update clock position and movement boolean
		clockPosition += 1
		if clockPosition == clockTimer:
			movement = True
		elif clockPosition > clockTimer:
			clockPosition = 0
			movement = False

		#handles displaying and refreshing the screen after each evauluation
		clock.tick(clockRate)
		display.fill(screen['color'])

		#update snake position if it is a movement eval
		if movement:

			if testBoundries(snake, screen['width'], screen['height']) or testSnakeCollision(snake):
				setGameOver()
			if gameover:
				break #breaks out of the if statement if gameover to avoid moving snake

			snakeMove(snake) #moves the snake according to desired direction
			recentMovement = snake['direction'] #updates so the last recorded movement is the most recent movement

			if testAppleEat(apple['XY'], snake['body'][0]):
				score += 1
				if score%5 == 0:
					clockTimer = int(clockTimer * difficulty)
				try:
					newApple(apple, snake['body'])
				except RecursionError:
					setGameOver()
					break
				snakeAddJoint(snake)

		#draws the items onto the screen
		drawItems(snake, display, block, apple, scoreBox)

		#draw score
		textScore = f'Score: {score}'
		font['size'] = list(font['font'].size(textScore))
		drawText(textScore, factor, screen['height']-font['size'][1]-(factor//3))

		#draw high score
		textHigh = f'High: {high}'
		font['size'] = list(font['font'].size(textHigh))
		drawText(textHigh, screen['width']-font['size'][0]-factor, screen['height']-font['size'][1]-(factor//3))


		pygame.display.update()

	#gameover loop
	while gameover:

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #keeps the screen alive until the 'x' button is pressed
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()

		#starts a new game if enter key is hit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				gameover = False

		#handles displaying and refreshing the screen after each evauluation
		clock.tick(clockRate)
		display.fill(screen['color'])

		#draws the items onto the screen
		drawItems(snake, display, block, apple, scoreBox)

		#draw score
		textScore = f'Score: {score}'
		font['size'] = list(font['font'].size(textScore))
		drawText(textScore, factor, screen['height']-font['size'][1]-(factor//3))

		#draw high score
		textHigh = f'High: {high}'
		font['size'] = list(font['font'].size(textHigh))
		drawText(textHigh, screen['width']-font['size'][0]-factor, screen['height']-font['size'][1]-(factor//3))

		pygame.display.update()