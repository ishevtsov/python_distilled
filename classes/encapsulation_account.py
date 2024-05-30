class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self._balance = balance

	def __repr__(self):
		return f'Account({self.owner!r}, {self._balance!r})'

	def deposit(self, amount):
		self._balance += amount

	def withdraw(self, amount):
		self._balance -= amount

	def inquiry(self):
		return self._balance