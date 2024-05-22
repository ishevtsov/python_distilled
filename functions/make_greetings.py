def make_greetings(names):
	funcs = []
	for name in names:
		funcs.append(lambda name=name: print('Hello', name))
	return funcs

a, b, c = make_greetings(['Guildo', 'Ada', 'Margaret'])

a()
b()
c()