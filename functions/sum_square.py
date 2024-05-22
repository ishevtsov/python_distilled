def sum_squares(items):
	items = [x * x for x in items]
	return sum(items)


a = [1, 2, 3, 4, 5]
print(a)

result = sum_squares(a)
print(result)
print(a)