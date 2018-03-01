import tools as t

class Vehicle:
	def __init__(self):
		self.pos = (0,0)
		self.distance = 0
		self.isAssigned = False
		self.completedRides = ""
		self.idRide = -1

class Simulation:
	#vehicles  pos (-1;-1 if busy); distance; isAssigned
	#time

	def __init__(self,vehicles):
		self.time = 0
		self.vehicles = vehicles

	def simulate():
		for vehicle in self.vehicles:
			if (vehicle.distance-=1)==0:
				self.removeRide(vehicle)
			self.time+=1
		return self.freeVehicles()

	def removeRide(vehicle):
		i = self.vehicles.indexOf(vehicle)
		self.vehicles[i].pos = (-1,-1)
		self.vehicles[i].completedRides+=self.vehicles[i].idRide if self.vehicles[i].completedRides=="" else " "+self.vehicles[i].idRide
		self.vehicles[i].isAssigned = False

	#ride has all from input
	def addRide(ride, vehicle):
		if(ride.endTime>time):
			return
		i = self.vehicles.indexOf(vehicle)
		self.vehicles[i].distance=t.getDistance(vehicle.pos, ride.finish)
		self.vehicles[i].pos = ride.finish
		self.vehicles[i].idRide = ride.id
		self.vehicles[i].isAssigned = True

	def freeVehicles():
		freeVehicles = []
		for vehicle in vehicles:
			if !vehicle.isAssigned:
				freeVehicles.add(vehicle)
		return freeVehicles
