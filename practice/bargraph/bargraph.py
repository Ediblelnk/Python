import math

class BarGraph:

	empty = ' '
	filled = 'x'
	y_axis = '|'
	x_axis = '-'
	origin = '+'

	def __init__(self, *data):
		self.data: list = data
	
	def __add__(self, bargraph):
		ret = []
		for i in range(max(len(self.data), len(bargraph.data))):
			try: a = self.data[i]
			except IndexError: a = 0
			try: b = bargraph.data[i]
			except: b = 0

			ret.append(a + b)

		return BarGraph(*ret)

	@property
	def maximum(self) -> int:
		return max(self.data)

	@property
	def graph(self) -> list:
		ret = []
		for i in range(len(self.data)):
			sub = []
			for j in range(self.maximum):
				if j >= self.data[i]:
					sub.append(self.empty)
				else: sub.append(self.filled)
			sub.reverse()
			ret.append(sub)

		return ret

	def __str__(self) -> str:
		ret = ''
		g = self.graph
		for i in range(len(g[0])):
			for j in range(len(g)):
				ret += g[j][i]
			ret += '\n'

		return ret
			

	def minimum(self):
		return min(self.data)

def main():
	data = [round(4*math.sin(x/30)) + 4 for x in range(0, 200)]
	a = BarGraph(*data)
	b = BarGraph(5, 3, 5, 1, 6, 9)
	print((a+b).data)

	print(a.graph)
	print(a)

if __name__ == '__main__':
	main()