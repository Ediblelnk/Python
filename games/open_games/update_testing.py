#imports and starts the moduals needed to run the program
from turtle import back
import pygame 
import sys
import os.path

pygame.init()

#screen format
ratio = 16, 9
factor = 120

width, height = ratio[0]*factor, ratio[1]*factor
screen = pygame.display.set_mode((width, height))

#blit format
ref_image = pygame.image.load(os.path.join(os.path.dirname(__file__), r"RockSml.jpg")).convert()
ref_image.set_colorkey(ref_image.get_at((0, 0)))
image = ref_image
rect = image.get_rect()

#backround format
background_color = pygame.Color('lemonchiffon3')

#clock format
clock = pygame.time.Clock()

def load_screen():
	"""loads the screen before getting put into display loop"""
	global background_color, screen
	screen.fill(background_color)
	pygame.display.update()

changed_rects = []
def register_movement(rect: pygame.Rect):
	"""registers rectanges of the screen as changed, to later be changed via 'update_changed()'"""
	changed_rects.append(rect.inflate(rect.w*.3, rect.h*.3))


def update_changed():
	"""updates the parts of the screen that have been changed"""
	print(changed_rects)
	for changed in changed_rects:
		pygame.display.update(changed)
	screen.fill(background_color)
	changed_rects.clear()

#draw the rock
def move_rock(pos: tuple):
	"""Currently moves the rock to the position of the cursor"""
	register_movement(rect)	#register position before moving
	rect.x, rect.y = pos[0]-0.5*rect.w, pos[1]-0.5*rect.h
	screen.blit(image, rect)
	register_movement(rect)	#register position after moving

#display loop
load_screen()
while True:
	if pygame.event.get(pygame.QUIT):
		sys.exit()
	pygame.event.clear()
	rect = image.get_rect()

	current_mouse_states = pygame.mouse.get_pressed()

	if current_mouse_states[0] == True:
		move_rock(pygame.mouse.get_pos())
		image = pygame.transform.rotate(ref_image, 360*(pygame.mouse.get_pos()[0] + pygame.mouse.get_pos()[1])/ width)
	#handles displaying and refreshing the screen after each evauluation
	clock.tick()
	update_changed()