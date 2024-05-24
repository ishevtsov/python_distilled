def receiver():
	print('Ready to receive')
	while True:
		n = yield
		print('Got', n)

r = receiver()
r.send(None)
r.send(1)
r.send(2)
r.send('Hello')
r.close()
r.send(3)