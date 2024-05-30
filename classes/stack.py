class Stack:
	def __init__(self):
		self._items = list()

	def push(self, item):
		self._items.append(item)

	def pop(self):
		return self._items.pop()

	def __len__(self):
		return len(self._items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push('Hello')
print(s.pop())
print(s.pop())