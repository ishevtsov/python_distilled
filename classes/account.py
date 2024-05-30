class Account:
	num_accounts = 0

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
		Account.num_accounts += 1

	@classmethod
	def from_xml(cls, data):
		from xml.etree.ElementTree import XML
		doc = XML(data)
		return cls(doc.findtext('owner'), float(doc.findtext('amount')))

	def __repr__(self):
		return f'{type(self).__name__}({self.owner!r}, {self.balance!r})'

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.deposit(-amount)

	def inquiry(self):
		return self.balance

a = Account('Guildo', 1000.0)
b = Account('Eva', 10.0)
print(Account.num_accounts)
print()

data = '''
<account>
	<owner>Guildo</owner>
	<amount>1000.0</amount>
</account>
'''

c = Account.from_xml(data)
print(c)