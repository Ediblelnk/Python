#imports and starts the modules needed to run the program
import pygame 
import sys
from asteroid_classes import Player
from asteroid_classes import Asteroid
from asteroid_classes import Saucer
from pygame.math import Vector2
import random

pygame.init()

class Asteroids:
	screen_ratio = 1, 1
	size_factor = min(1000/screen_ratio[0], 1000/screen_ratio[1])
	width, height = screen_ratio[0]*size_factor, screen_ratio[1]*size_factor
	print(width, height)
	screen = pygame.display.set_mode((width, height))
	background_color = pygame.Color('black')

	alpha = 150
	beta = 150

	objects =  [Player((width/2, height/2), (0,0), 0, 0)]

	changed_rects = [] #need to implement this

	clock = pygame.time.Clock()

	@classmethod
	def _get_random_asteroids(cls, n: int, size: int=2, pos: tuple=None) -> list:
		a = cls.alpha
		b = cls.beta
		w = cls.width
		h = cls.height

		return_list = []
		for i in range(n):
			sides = 'top bottom left right'.split()

			match sides[i%len(sides)]:
				case 'top': 
					return_list.append(Asteroid(
							(random.randint(b, w-b), b),
							(random.randint(-a, a), random.randint(-a, a)),
							0, random.randint(-a, a), size))
				case 'bottom':
					return_list.append(Asteroid(
							(random.randint(b, w-b), h-b),
							(random.randint(-a, a), random.randint(-a, a)),
							0, random.randint(-a, a), size))
				case 'left':
					return_list.append(Asteroid(
							(b, random.randint(b, h-b)),
							(random.randint(-a, a), random.randint(-a, a)),
							0, random.randint(-a, a), size))
				case 'right':
					return_list.append(Asteroid(
							(w-b, random.randint(b, h-b)),
							(random.randint(-a, a), random.randint(-a, a)),
							0, random.randint(-a, a), size))

		return return_list

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

		cls.objects += cls._get_random_asteroids(4)

		while True:

			keydowns = pygame.event.get(pygame.KEYDOWN)
			keyups = pygame.event.get(pygame.KEYUP)

			if pygame.event.get(pygame.QUIT):
				sys.exit()

			#print('Speed:', cls.objects[0].velocity.length(), 'Rot Speed:', cls.objects[0].rot_velocity)

			cls.objects[0].handle_keypresses(keydowns, keyups)
			cls._keep_objects_onscreen()

			#handles displaying and refreshing the screen after each evauluation
			
			cls.clock.tick(144)
			cls.screen.fill(cls.background_color)
			cls._blit_game_objects()
			pygame.display.update()

if __name__ == '__main__':
	Asteroids.run()