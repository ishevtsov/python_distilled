from functools import wraps

def trace(func):
	@wraps(func)
	def call(*args, **kwargs):
		print('Calling', func.__name__)
		return func(*args, **kwargs)
	return call

@trace
def squares(x):
	return x * x

a = squares(3)
print(a)