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

	def __init__(self,vehicles):
		self.time = 0
		self.vehicles = vehicles

	def simulate():
		for vehicle in self.vehicles:
			if vehicle.distanceToStart==0:
				if (vehicle.distance-=1)==0:
					self.removeRide(vehicle)
			else:
				vehicle.distanceToStart-=1
			self.time+=1
		return self.freeVehicles()

	def removeRide(vehicle):
		i = self.vehicles.indexOf(vehicle)
		self.vehicles[i].pos = (-1,-1)
		if self.vehicles[i].idRide != -1:
			self.vehicles[i].completedRides+=self.vehicles[i].idRide if self.vehicles[i].completedRides=="" else " "+self.vehicles[i].idRide
		self.vehicles[i].isAssigned = False

	#ride has all from input
	def addRide(ride, vehicle):
		if(ride.endTime>time):
			return
		v = Vehicle()
		v.distance=t.getDistance(vehicle.pos, ride.finish)
		v.distanceToStart=t.getDistance(vehicle.pos, ride.start)
		v.pos = ride.finish
		v.idRide = ride.id
		v.isAssigned = True
		vehicles.append(v)

	def freeVehicles():
		freeVehicles = []
		for vehicle in vehicles:
			if !vehicle.isAssigned:
				freeVehicles.add(vehicle)
		return freeVehicles
