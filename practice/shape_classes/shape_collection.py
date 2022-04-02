from shapes import Circle, Rectangle, Triangle
from functools import total_ordering
import math

@total_ordering
class ShapeCollection:
	def __init__(self, *shapes) -> None:
		self.shapes = shapes

	def __eq__(self, s) -> bool:
		return self.area == s.area

	def __lt__(self, s) -> bool:
		return self.area < s.area

	def __add__(self, s) -> float:
		return ShapeCollection(*self.shapes, *s.shapes)

	def __sub__(self, s) -> float:
		return self.area - s.area

	def __mul__(self, s) -> float:
		return self.area * s.area

	def __floordiv__(self, s) -> int:
		return round(self / s)

	def __truediv__(self, s) -> float:
		return self.area / s.area

	def __mod__(self, s) -> float:
		return self.area % s.area

	def __divmod__(self, s) -> tuple:
		return self // s, self % s

	def __pow__(self, p) -> float:
		return self.area ** p

	@property
	def area(self) -> float:
		return sum([shape.area for shape in self.shapes])

def main():
	c = Circle(1)
	t = Triangle.from_angle(4, 5, 90)
	r = Rectangle(2, 2)
	r2 = Rectangle(1, 1)

	s = ShapeCollection(c, t, r)
	s2 = ShapeCollection(c, t, r2)
	print((s + s2).area, f's: {s.area}', f's2: {s2.area}')

if __name__ == '__main__':
	main()