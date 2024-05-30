class Ops:
	@staticmethod
	def add(x, y):
		return x + y

	@staticmethod
	def sub(x, y):
		return x - y

a = Ops.add(2, 3)
b = Ops.sub(4, 5)

print(a)
print(b)