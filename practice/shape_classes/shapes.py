import math

class Circle:
	def __init__(self, radius: float) -> None:
		self.radius: float = radius

	@property
	def area(self) -> float:
		return math.pi * self.radius**2

class Rectangle:
	def __init__(self, length: float, width: float) -> None:
		self.length: float = length
		self.width: float = width

	@property
	def area(self) -> float:
		return self.length * self.width

class Triangle:
	def __init__(self, a: float, b: float, c: float) -> None:
		self.a: float = a
		self.b: float = b
		self.c: float = c

	@classmethod
	def from_angle(cls, a: float, b: float, ang: float):
		'''a = side a, b = side b, ang = angle between a and b in degrees'''
		c = math.sqrt(a**2 + b**2 - a * b * math.cos(math.radians(ang)))
		return cls(a, b, c)

	@property
	def area(self) -> float:
		a, b, c, s = self.a, self.b, self.c, (self.a + self.b + self.c)/2
		return round(math.sqrt(s * (s-a) * (s-b) * (s-c)), 14)

def main():
	c = Circle(2)
	print(c.area)
	r = Rectangle(4, 5)
	print(r.area)
	t = Triangle.from_angle(7, 4, 90)
	print(t.area)

if __name__ == '__main__':
	main()