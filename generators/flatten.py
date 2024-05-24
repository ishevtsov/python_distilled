def flatten(item):
	for i in item:
		if isinstance(i, list):
			yield from flatten(i)
		else:
			yield i

a = [1, 2, [3, [4, 5], 6, 7], 8]

for x in flatten(a):
	print(x, end=' ')