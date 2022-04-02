class BarGraph:

	empty = ' '
	filled = 'x'
	y_axis = '|'
	x_axis = '-'
	origin = '+'

	def __init__(self, *data):
		self.data: list = data
	
	@property
	def maximum(self):
		return max(self.data)

	def minimum(self):
		return min(self.data)

def main():
	pass

if __name__ == '__main__':
	main()