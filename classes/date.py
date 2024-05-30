import time

class Date:
	datefmt = '{year}-{month:02d}-{day:02d}'
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def __str__(self):
		return self.datefmt.format(year=self.year,
							month=self.month,
							day = self.day)

	@classmethod
	def from_timestamp(cls, ts):
		tm = time.localtime(ts)
		return cls(tm.tm_year, tm.tm_mon, tm.tn_mday)

	@classmethod
	def today(cls):
		return cls.tm.from_timestamp(time.time())

class MDYDate(Date):
	datefmt = '{month}/{day}/{year}'

class DMYDate(Date):
	datefmt = '{day}/{month}/{year}'

a = Date(1967, 4, 9)
print(a)

b = MDYDate(1967, 4, 9)
print(b)

c = DMYDate(1967, 4, 9)
print(c)