from pygame.math import Vector2
from pygame import Rect
import pygame.image as Image
import os.path
import random

class GameObject:
	'''Most basic form of a object in the game.'''

	#image is a sprite set for this game, use specific regions of IMAGE when blitting
	IMAGE = Image.load(os.path.join(os.path.dirname(__file__), r"asteroids_sprites.png"))
	#IMAGE.set_colorkey(IMAGE.get_at((0,0)))

	def __init__(self, pos: tuple) -> None:
		'''Defines a position for the GameObject'''
		self.pos = Vector2(pos)

class Player(GameObject):

	IMAGE_LOCATION = Rect(503, 242, 75, 104)
	
	def __init__(self, pos: tuple) -> None:
		'''Creates a new Player with a defined position and velocity'''
		super().__init__(pos)

class Asteroid(GameObject):
	
	ASTEROID_L1 = Rect(0, 0, 200, 200)
	ASTEROID_L2 = Rect(200, 0, 185, 200)
	ASTEROID_L3 = Rect(400, 0, 200, 200)
	ASTEROID_M1 = Rect(0, 200, 200, 200)
	ASTEROID_M2 = Rect(0, 200, 200, 200)
	ASTEROID_M3 = Rect(0, 200, 200, 200)
	ASTEROID_S1 = Rect(0, 200, 200, 200)
	ASTEROID_S2 = Rect(0, 200, 200, 200)
	ASTEROID_S3 = Rect(0, 200, 200, 200)

	ASTEROIDS_LARGE = (ASTEROID_L1, ASTEROID_L2, ASTEROID_L3)
	ASTEROIDS_MEDIUM = (ASTEROID_M1, ASTEROID_M2, ASTEROID_M3)
	ASTEROIDS_SMALL = (ASTEROID_S1, ASTEROID_S2, ASTEROID_S3)

	def __init__(self, pos: tuple, size: int=2) -> None:
		super().__init__(pos)
		self.size = size
		self.IMAGE_LOCATION = self._assign_image_location(size)

	def _assign_image_location(self, size: int) -> Rect:
		'''Assigns a sprite location based on the size of the asteroid'''
		match size:
			case 2:
				return Asteroid.ASTEROID_L1
			case 1:
				return random.choice(Asteroid.ASTEROIDS_MEDIUM)
			case _:
				return random.choice(Asteroid.ASTEROIDS_SMALL)

class Saucer(GameObject):
	
	def __init__(self, pos: tuple) -> None:
		super().__init__(pos)

def main():
	p = Player((0,0))
	print(p.IMAGE, p.IMAGE_LOCATION, p.pos)
	a = Asteroid((1,1), 2)
	print(a.IMAGE, a.IMAGE_LOCATION, a.pos)

if __name__ == '__main__':
	main()