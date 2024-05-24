# yield from

def countup(stop):
	n = 1
	while n <= stop:
		yield n
		n += 1

def countdown(start):
	n = start
	while n > 0:
		yield n
		n -= 1

def up_and_down(n):
	yield from countup(n)
	yield from countdown(n)

for x in up_and_down(5):
	print(x, end=' ')