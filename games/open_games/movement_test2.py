#imports and starts the moduals needed to run the program
import pygame 
import sys

pygame.init()

#screen format
width = 960
height = 540
screen = pygame.display.set_mode((width, height))
gravity_momentum = 0
gravity = 1

#player format
player_width = 25
player_height = 25
player_color = (255,255,255)
player_x = width/2 - player_width/2
player_y = height-player_height

#player movement
player_speed = 10
player_left = False
player_right = False
player_gravity = False

#block format
block_color = (0,0,0)
block_width = 300
block_height = 50
block_x = 480
block_y = height - 200

#collision format

#backround format
background_color = (0,100,100)

#clock format
clock = pygame.time.Clock()
clock_rate = 60

#display loop
gameover = False
while not gameover:
	for event in pygame.event.get():

		if event.type == pygame.QUIT: #keeps the screen alive until the 'x' is pressed
			sys.exit()

	if event.type == pygame.KEYDOWN: #handles keydowns
		

		if event.key == pygame.K_a or event.key == pygame.K_LEFT: #starts 'a' or 'left arrow' input
			player_left = True
			player_right = False

		if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #starts 'd' or right arrow input
			player_right = True
			player_left = False

		if event.key == pygame.K_SPACE: #starts 'jump' input
			pass


	if event.type == pygame.KEYUP: #handles keyups


		if event.key == pygame.K_a or event.key == pygame.K_LEFT: #finishs 'a' or 'left arrow' input
			player_left = False

		if event.key == pygame.K_d or event.key == pygame.K_RIGHT: #finishs 'd' or 'right arrow' input
			player_right = False


	if player_left: #moves left until 'a' key is lifted
		player_x -= player_speed

	if player_right: #moves left until 'd' key is lifted
		player_x += player_speed


	if player_x + player_height < height:
		player_gravity = True
	if player_gravity == True:
		pass



	#handles keeping the player inside the browser
	if player_x < 0 - player_width:
		player_x = width
	if player_x > width:
		player_x = 0 - player_width
	if player_y < 0:
		player_y = 0
	if player_y + player_height > height:
		player_y = height - player_height

	#handles displaying and refreshing the screen after each evauluation
	clock.tick(clock_rate)
	screen.fill(background_color)
	pygame.draw.rect(screen, block_color, (block_x, block_y, block_width, block_height))
	pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
	pygame.display.update()