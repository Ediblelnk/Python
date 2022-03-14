from pygame.math import Vector2
from pygame import Surface
from pygame.transform import rotate
import pygame.image as Image
import os.path
import random

def _load_image(file_within_sprites: str) -> Surface:
	'''shorthand method to avoid ghastly repetition of code'''
	_base = os.path.join(os.path.dirname(__file__), r"sprites")
	return Image.load(os.path.join(_base, file_within_sprites))#.convert()

class GameObject:
	'''Most basic form of a object in the game.'''

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		'''Creates a new GameObject with position, velocity, rotation, and rotational velocity'''
		self.pos = Vector2(pos)
		self.velocity = Vector2(velocity)
		self.rotation = rotation
		self.rot_velocity = rot_velocity

	def update(self, time_delta_ms: int) -> None:
		'''Updates the position and rotation of a GameObject'''
		self.pos += self.velocity * (time_delta_ms / 1000)
		self.rotation += self.rot_velocity * (time_delta_ms / 1000)

class Player(GameObject):
	
	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		'''Creates a new Player with position, velocity, rotation, and rotational velocity'''
		super().__init__(pos, velocity, rotation, rot_velocity)
		self._IMAGE = _load_image(r'player.png')
		self._IMAGE.set_colorkey(self._IMAGE.get_at((0, 0)))

	def get_image(self) -> Surface:
		'''Gets the image to use for the player, (use because of rotation)'''
		image = rotate(self._IMAGE, self.rotation)
		image.set_colorkey(self._IMAGE.get_at((0,0)))
		return image

	def get_pos(self) -> Vector2:
		'''Gets the position of the player, centered, (use because of rotation)'''
		image = self.get_image()
		return self.pos - Vector2(image.get_width()/2, image.get_height()/2)

class Asteroid(GameObject):

	ASTEROIDS_LARGE = (_load_image(r'asteroid_L1.png'), 
	_load_image(r'asteroid_L2.png'), _load_image(r'asteroid_L3.png'))
	ASTEROIDS_MEDIUM = (_load_image(r'asteroid_M1.png'), 
	_load_image(r'asteroid_M2.png'), _load_image(r'asteroid_M3.png'))
	ASTEROIDS_SMALL = (_load_image(r'asteroid_S1.png'), 
	_load_image(r'asteroid_S2.png'), _load_image(r'asteroid_S3.png'))

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float, size: int=2) -> None:
		'''Creates a new Asteroid with position, velocity, rotation, and rotational velocity'''
		super().__init__(pos, velocity, rotation, rot_velocity)
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

	def get_image(self) -> Surface:
		'''Gets the image to use for the asteroid, (use because of rotation)'''
		image = rotate(self._IMAGE, self.rotation)
		image.set_colorkey(self._IMAGE.get_at((0,0)))
		return image

	def get_pos(self) -> Vector2:
		'''Gets the position of the asteroid, centered, (use because of rotation)'''
		image = self.get_image()
		return self.pos - Vector2(image.get_width()/2, image.get_height()/2)

class Saucer(GameObject):
	
	SAUCERS = _load_image(r'saucer_2.png'), _load_image(r'saucer_3.png')

	def __init__(self, pos: tuple, velocity: tuple, rotation: float, rot_velocity: float) -> None:
		'''Creates a new Saucer with position, velocity, rotation, and rotational velocity'''
		super().__init__(pos, velocity, rotation, rot_velocity)
		self._IMAGE = random.choice(Saucer.SAUCERS)

	def get_image(self) -> Surface:
		'''Gets the image to use for the saucer, (use because of rotation)'''
		image = rotate(self._IMAGE, self.rotation)
		image.set_colorkey(self._IMAGE.get_at((0,0)))
		return image

	def get_pos(self) -> Vector2:
		'''Gets the position of the saucer, centered, (use because of rotation)'''
		image = self.get_image()
		return self.pos - Vector2(image.get_width()/2, image.get_height()/2)	

def main():
	print("It Compiled!")

if __name__ == '__main__':
	main()