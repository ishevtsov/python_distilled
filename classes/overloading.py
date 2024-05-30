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
		return f'Account({self.owner!r}, {self.balance!r})'

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def inquiry(self):
		return self.balance

class AccountPortfolio:
	def __init__(self):
		self.accounts = []

	def add_account(self, account):
		self.accounts.append(account)

	def total_funds(self):
		return sum(account.inquiry() for account in self)

	def __len__(self):
		return len(self.accounts)

	def __getitem__(self, index):
		return self.accounts[index]

	def __iter__(self):
		return iter(self.accounts)

port = AccountPortfolio()
port.add_account(Account('Guido', 1000.0))
port.add_account(Account('Eva', 50.0))

print(port.total_funds())
print(len(port))

for account in port:
	print(account)

print(port[1].inquiry())