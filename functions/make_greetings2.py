def make_greetings(names):
	funcs = []
	for name in names:
		def greeting(name=name):
			print('Hello', name)
		funcs.append(greeting)
	return funcs

a, b, c = make_greetings(['Guildo', 'Ada', 'Margater'])

a()
b()
c()