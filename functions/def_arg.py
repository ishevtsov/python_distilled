#!/usr/bin/env python

# default param evaluated once when the function is defined
# not each time the function runs
def func(x, items=[]):
	items.append(x)
	return items

print(func(1))
print(func(2))
print(func(3))

print()

def func(x, items=None):
	if items is None:
		items = []
	items.append(x)
	return items

print(func(1))
print(func(2))
print(func(3))