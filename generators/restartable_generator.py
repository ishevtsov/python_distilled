class countdown:
	def __init__(self, start):
		self.start = start

	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

count = 3

while count > 0:
	for n in countdown(5):
		print(n)
	print()
	count -= 1