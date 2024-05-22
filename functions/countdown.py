def countdown(start):
	n = start
	def display():
		print('T-minus', n)
	while n > 0:
		display()
		n -= 1

countdown(5)