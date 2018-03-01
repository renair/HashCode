def time_to_arrive(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])

def get_ride_for_vehicle(car, time, rides):
	row, col = car
	
