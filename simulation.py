import tools as t

class Vehicle:
	def __init__(self):
		self.pos = (0,0)
		self.distance = 0
		self.distanceToStart = 0
		self.isAssigned = False
		self.completedRides = ""
		self.idRide = -1

class Simulation:
	#vehicles  pos (-1;-1 if busy); distance; isAssigned
	#time

	def __init__(self, vehicles):
		self.time = 0
		self.vehicles = vehicles

	def simulate(self):
		for vehicle in self.vehicles:
			if vehicle.distanceToStart==0:
				vehicle.distance -= 1
				if vehicle.distance == 0:
					self.removeRide(vehicle)
			else:
				vehicle.distanceToStart-=1
			self.time+=1
		return self.freeVehicles()

	def removeRide(self, vehicle):
		i = self.vehicles.index(vehicle)
		self.vehicles[i].pos = (-1,-1)
		if self.vehicles[i].idRide != -1:
			self.vehicles[i].completedRides += str(self.vehicles[i].idRide) + " " #self.vehicles[i].idRide if self.vehicles[i].completedRides=="" else " " + self.vehicles[i].idRide
		self.vehicles[i].isAssigned = False

	#ride has all from input
	def addRide(self, ride, vehicle):
		if(ride.latest < self.time):
			return
		##v = Vehicle()
		vehicle.distance=t.time_to_arrive(vehicle.pos, ride.finish)
		vehicle.distanceToStart=t.time_to_arrive(vehicle.pos, ride.start)
		vehicle.pos = ride.finish
		vehicle.idRide = ride.id
		vehicle.isAssigned = True
		#self.vehicles.append(v)

	def freeVehicles(self):
		freeVehicles = []
		for vehicle in self.vehicles:
			if not vehicle.isAssigned:
				freeVehicles.append(vehicle)
		return freeVehicles
