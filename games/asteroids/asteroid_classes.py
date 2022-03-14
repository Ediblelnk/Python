from pygame.math import Vector2
from pygame import Rect, Surface
from pygame.transform import rotate
import pygame.image as Image
import os.path
import random

class GameObject:
	'''Most basic form of a object in the game.'''

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		'''Defines a position and rotation and velocity for the GameObject'''
		self.pos = Vector2(pos)
		self.velocity = Vector2(velocity)
		self.rotation = rotation
		self.rot_velocity = rot_velocity

	def update(self, time_delta_ms: int) -> None:
		'''Updates the position and rotation of a GameObject'''
		self.pos += self.velocity * (time_delta_ms / 1000)
		self.rotation += self.rot_velocity * (time_delta_ms / 1000)

class Player(GameObject):

	_IMAGE = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"player2.png"))#.convert()
	_IMAGE.set_colorkey(_IMAGE.get_at((0, 0)))
	
	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		'''Creates a new Player with position, velocity, rotation, and rotational velocity'''
		super().__init__(pos, velocity, rotation, rot_velocity)

	def get_image(self) -> Surface:
		'''Gets the image to use for the player, (use because of rotation)'''
		image = rotate(self._IMAGE, self.rotation)
		image.set_colorkey(self._IMAGE.get_at((0,0)))
		return image

	def get_pos(self) -> Vector2:
		'''Gets the position of the player, centered, (use because of rotation)'''
		image = self.get_image()
		print(image)
		return self.pos - Vector2(image.get_width()/2, image.get_height()/2)

class Asteroid(GameObject):
	
	ASTEROID_L1 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_L1.png"))#.convert()
	ASTEROID_L2 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_L2.png"))#.convert()
	ASTEROID_L3 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_L3.png"))#.convert()
	ASTEROID_M1 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_M1.png"))#.convert()
	ASTEROID_M2 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_M2.png"))#.convert()
	ASTEROID_M3 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_M3.png"))#.convert()
	ASTEROID_S1 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_S1.png"))#.convert()
	ASTEROID_S2 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_S2.png"))#.convert()
	ASTEROID_S3 = Image.load(os.path.join(os.path.dirname(__file__), r"sprites", r"asteroid_S3.png"))#.convert()

	ASTEROIDS_LARGE = (ASTEROID_L1, ASTEROID_L2, ASTEROID_L3)
	ASTEROIDS_MEDIUM = (ASTEROID_M1, ASTEROID_M2, ASTEROID_M3)
	ASTEROIDS_SMALL = (ASTEROID_S1, ASTEROID_S2, ASTEROID_S3)

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float, size: int=2) -> None:
		super().__init__(pos, rotation, velocity)
		self.size = size
		self._IMAGE = self._assign_image(size)
		self._IMAGE.set_colorkey(self._IMAGE.get_at((0, 0)))

	def _assign_image(self, size: int) -> Surface:
		'''Assigns a sprite location based on the size of the asteroid'''
		match size:
			case 2:
				return random.choice(Asteroid.ASTEROIDS_LARGE)
			case 1:
				return random.choice(Asteroid.ASTEROIDS_MEDIUM)
			case _:
				return random.choice(Asteroid.ASTEROIDS_SMALL)

	def get_image(self):

		return rotate(self._IMAGE, self.rotation)

class Saucer(GameObject):
	
	SAUCER_2 = Rect(34, 535, 71, 134)
	SAUCER_3 = Rect(175, 514, 147, 147)

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		super().__init__(pos, rotation, velocity)
		self.IMAGE_LOCATION = Saucer.SAUCER_3#random.choice((Saucer.SAUCER_2, Saucer.SAUCER_3))

def main():
	pass

if __name__ == '__main__':
	main()