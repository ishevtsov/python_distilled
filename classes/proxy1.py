class A:
	def spam(self):
		print('A.spam')

	def grok(self):
		print('A.grok')

	def yow(self):
		print('A.yow')

class LoggedA:
	def __init__(self):
		self._a = A()

	def __getattr__(self, name):
		print('Accessing', name)
		# Delegate to internal A instance
		return getattr(self._a, name)

a = LoggedA()
a.spam()
a.yow()