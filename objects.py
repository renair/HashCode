

class Model:
	def __init__(self):
		self.rows = 0
		self.cols = 0
		self.vehicles = 0
		self.rides = 0
		self.per_time_bonus = 0
		self.steps = 0

class Ride:
	def __init__(self):
		self.start = (0, 0)
		self.finish = (0, 0)
		self.earliest = 0
		self.latest = 0