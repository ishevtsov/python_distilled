#!/usr/bin/env python
# subtype is a type defined by inheritance

def removeall(items: list, item) -> list:
	return [i for i in items if i != item]

class mylist(list):
	def removeall(self, val):
		return [i for i in self if i != val]

items = mylist([5,8,2,7,2,13,9])
x = items.removeall(2)
print(items)
print(x)
