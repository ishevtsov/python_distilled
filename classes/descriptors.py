class Typed:
	expected_type = object

	def __set_name__(self, cls, name):
		self.key = name

	def __get__(self, instance, cls):
		if instance:
			return instance.__dict__[self.key]
		else:
			return self

	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError(f'Expected {self.expected_type}')
		instance.__dict__[self.key] = value

	def __delete__(self, instance):
		raise AttributeError("Can't delete attribute")

class Integer(Typed):
	expected_type = int

class Float(Typed):
	expected_type = float

class String(Typed):
	expected_type = str

# Example use
class Account:
	owner = String()
	balance = Float()

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

a = Account('Guildo', 1000.0)
b = a.owner
a.owner = 'Eva'
del a.owner