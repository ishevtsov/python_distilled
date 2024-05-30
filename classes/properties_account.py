import string

class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	@property
	def owner(self):
		return self._owner

	@owner.setter
	def owner(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected str')
		if not all(c in string.ascii_uppercase for c in value):
			raise ValueError('Must be uppercase ASCII')
		if len(value) > 10:
			raise ValueError('Must be 10 characters or less')
		self._owner = value

a = Account('GUIDO', 1000.0)
a.owner = 'EVA'
# a.owner = 42
# a.owner = 'Carol'
#a.owner = 'RENÉE'
a.owner = 'RAMAKRISHNAN'