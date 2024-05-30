# use properties for implementing read-only computed data attributes

class Box:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	@property
	def area(self):
		return self.width * self.height

	@property
	def perimeter(self):
		return 2 * self.width + 2 * self.height

b = Box(4, 5)
print(b.area)
print(b.perimeter)
b.area = 5  # ERROR:
