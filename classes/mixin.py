class Duck:
	def noise(self):
		return 'Quack'

	def waddle(self):
		return 'Waddle'

class Trombonist:
	def noise(self):
		return 'Blat!'

	def march(self):
		return 'Clomp'

class Cyclist:
	def noise(self):
		return 'On your left!'

	def pedal(self):
		return 'Padeling'

class LoudMixin:
	def noise(self):
		return super().noise().upper()

class AnnoyingMixin:
	def noise(self):
		return 3 * super().noise()

class LoudDuck(LoudMixin, Duck):
	pass

class AnnoyingTrombonist(AnnoyingMixin, Trombonist):
	pass

class AnnoyingLoudCyclist(AnnoyingMixin, LoudMixin, Cyclist):
	pass

d = LoudDuck()
print(LoudDuck.__mro__)
print(d.noise())

t = AnnoyingTrombonist()
print(AnnoyingTrombonist.__mro__)
print(t.noise())

c = AnnoyingLoudCyclist()
print(c.noise())