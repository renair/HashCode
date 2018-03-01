import objects as obj

def parse_file(name):
	f = open(name, 'r')
	lines = f.readlines()
	model = obj.Model()
	a = (get_model(lines[0]), get_rides(lines[1:]))
	f.close()
	return a

def get_model(str):
	splited = str.split(' ')
	model = obj.Model()
	model.rows = int(splited[0])
	model.cols = int(splited[1])
	model.vehicles = int(splited[2])
	model.rides = int(splited[3])
	model.per_time_bonus = int(splited[4])
	model.steps = int(splited[5])
	return model

def get_rides(lines):
	res = []
	int  i = 0
	for l in lines:
		ride = obj.Ride()
		splited = l.split(' ')
		ride.id = i
		ride.start = (int(splited[0]), int(splited[1]))
		ride.finish = (int(splited[2]), int(splited[3]))
		ride.earliest = int(splited[4])
		ride.latest = int(splited[5])
		res.append(ride)
		i += 1
	return res
