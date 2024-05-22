def trace(func):
	def call(*args, **kwargs):
		print('Calling', func.__name__)
		return func(*args, **kwargs)
	return call

@trace
def square(x):
	return x * x

a = square(3)
print(a)