import random

class Account:
	'''
	A simple bank account
	'''
	owner: str
	balance: float

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __repr__(self):
		return f'{type(self).__name__}({self.owner!r}, {self.balance!r})'

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def inquiry(self):
		return self.balance

class MyAccount(Account):
	def panic(self):
		self.withdraw(self.balance)

class EvilAccount(Account):
	def __init__(self, owner, balance, factor):
		super().__init__(owner, balance)
		self.factor = factor

	def inquiry(self):
		if random.randint(0,4) == 1:
			return self.factor * super().inquiry()
		else:
			return super().inquiry()

a = MyAccount('Guildo', 1000.0)
a.withdraw(23.0)
print(a.inquiry())
a.panic()
print(a.inquiry())
print()

a = EvilAccount('Guildo', 1000.0, 1.10)
a.deposit(10.0)
available = a.inquiry()
print(available)
