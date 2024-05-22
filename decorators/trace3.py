from functools import wraps

def trace(message):
	def decorate(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print(message.format(func=func))
			return func(*args, **kwargs)
		return wrapper
	return decorate

@trace('You called {func.__name__}')
def squares(x):
	return x * x

a = squares(3)
print(a)