class Simulation:
	vehicles   #pos (-1;-1 if busy); distance; isAssigned
	time

	def __init__(self,vehicles):
        self.time = 0
        self.vehicles = vehicles

	def simulate():
		for vehicle in vehicles:
			if (vehicle.distance-=1)==0:
				removeRide(vehicle)
			time+=1

	def removeRide(vehicle):
		i = vehicles.indexOf(vehicle)
		vehicles[i].pos = (-1,-1)

	#ride has all from input
	def addRide(ride, vehicle):
		if(ride.endTime>time):
			return
		v = vehicles[vehicle]
		v.distance=abs(ride.endX-v.pos.Y)+abs(ride.endY-v.pos.Y)