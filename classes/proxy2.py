class A:
	def spam(self):
		print('A.spam')

	def grok(self):
		print('A.grok')

	def yow(self):
		print('A.yow')

class B:
	def __init__(self):
		self._a = A()

	def grok(self):
		print('B.grok')

	def __getattr__(self, name):
		return getattr(self._a, name)

b = B()
b.spam()
b.grok()
b.yow()