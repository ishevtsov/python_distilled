def make_greeting(name):
	def greeting():
		print('Hello', name)
	return greeting

f = make_greeting('Guido')
g = make_greeting('Ada')

f()
g()