class Time(object):

	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		slef.second = second

	def __str__(self):
		return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
		