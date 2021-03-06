import tools as t

class Vehicle:
	def __init__(self):
		self.pos = (0,0)
		self.distance = 0
		self.distanceToStart = 0
		self.isAssigned = False
		self.completedRides = []
		self.idRide = -1

class Simulation:
	#vehicles  pos (-1;-1 if busy); distance; isAssigned
	#time

	def __init__(self, vehicles):
		self.time = 0
		self.vehicles = vehicles

	def simulate(self):
		#print("time" + str(self.time))
		for vehicle in self.vehicles:
			if vehicle.distanceToStart==0 and vehicle.isAssigned:
				vehicle.distance -= 1
				#print("IdRide:" + str(vehicle.idRide)+"distance"+str(vehicle.distance))
				if vehicle.distance == 0:
					self.removeRide(vehicle)
			else:
				vehicle.distanceToStart-=1

		self.time += 1
		return self.freeVehicles()

	def removeRide(self, vehicle):
		#print("ridefinish:" + str(vehicle.idRide) + "finished in"+str(vehicle.pos))
		i = self.vehicles.index(vehicle)
		if self.vehicles[i].idRide != -1:
			vehicle.completedRides.append(str(vehicle.idRide))
		self.vehicles[i].isAssigned = False

	#ride has all from input
	def addRide(self, ride, vehicle):
		#print("risestart:" + str(ride.id) + str(vehicle.pos))
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
