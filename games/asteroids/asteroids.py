#imports and starts the moduals needed to run the program
import pygame 
import sys
from asteroid_classes import Player
from asteroid_classes import Asteroid
from asteroid_classes import Saucer
from pygame.math import Vector2

pygame.init()

class Asteroids:
	screen_ratio = 2, 1
	size_factor = min(1000/screen_ratio[0], 500/screen_ratio[1])
	width, height = screen_ratio[0]*size_factor, screen_ratio[1]*size_factor
	print(width, height)
	screen = pygame.display.set_mode((width, height))
	background_color = pygame.Color('black')

	objects =  [Player((width, 0), (-10, 10), 0, 0),
				Asteroid((0, 0), (50, 50), 0, 50),
				Asteroid((width, 0), (-50, 50), 0, 50, size=0)]

	changed_rects = [] #need to implement this

	clock = pygame.time.Clock()

	@classmethod
	def _blit_game_objects(cls):
		for object in cls.objects:
			object.update(cls.clock.get_time())
			cls.screen.blit(object.get_image(), object.get_pos())

	@classmethod
	def _keep_objects_onscreen(cls):
		for object in cls.objects:
			object_box = object.get_image().get_rect().move(*object.get_pos())
			if not cls.screen.get_rect().colliderect(object_box):
				match object_box.topleft:
					case (x, _) if x > cls.width:
						object.set_pos(0, object.pos.y)
					case (_, y) if y > cls.height:
						object.set_pos(object.pos.x, 0)
					case (x, _) if x < -object.get_image().get_rect().width:
						object.set_pos(cls.width, object.pos.y, True)
					case (_, y) if y < -object.get_image().get_rect().height:
						object.set_pos(object.pos.x, cls.height, True)

	@classmethod
	def run(cls):
		while True:

			keydowns = pygame.event.get(pygame.KEYDOWN)
			keyups = pygame.event.get(pygame.KEYUP)

			if pygame.event.get(pygame.QUIT):
				sys.exit()

			#print('Player Speed:', cls.objects[0].velocity.length())

			cls.objects[0].handle_keypresses(keydowns, keyups)
			cls._keep_objects_onscreen()

			#handles displaying and refreshing the screen after each evauluation
			
			cls.clock.tick(144)
			cls.screen.fill(cls.background_color)
			cls._blit_game_objects()
			pygame.display.update()

if __name__ == '__main__':
	Asteroids.run()