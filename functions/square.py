def square(items):
	for i, x in enumerate(items):
		items[i] = x * x

a = [1, 2, 3, 4, 5]
print(a)

square(a)

print(a)