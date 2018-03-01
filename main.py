import objects as obj
import obj_parser as pars
import simulation
import tools

#model, rides = pars.parse_file("a_example.in")
#model, rides = pars.parse_file("b_should_be_easy.in")
model, rides = pars.parse_file("c_no_hurry.in")
#model, rides = pars.parse_file("d_metropolis.in")
#model, rides = pars.parse_file("e_high_bonus.in")

vehicles = [simulation.Vehicle() for _ in range(model.vehicles)]

#Відсортувати список поїздок
sm = simulation.Simulation(vehicles)
#Цикл:
for v in vehicles:
	ride = tools.get_ride_for_vehicle(v, 0, rides, model.steps, model.per_time_bonus)
	rides.remove(ride)
	sm.addRide(ride, v)
	
while sm.time < model.steps or len(rides) != 0:
#Додати поїздки до симуляції
#Запустити симуляцію
	free_cars = sm.simulate()
	for v in free_cars:
		#print(len(free_cars))
		if len(rides) > 0:
			ride = tools.get_ride_for_vehicle(v, sm.time, rides, model.steps, model.per_time_bonus)
			rides.remove(ride)
			sm.addRide(ride, v)
#Взяти позиції автомобілів із симуляції

for v in vehicles:
	print(str(len(v.completedRides)) + " " + ' '.join(v.completedRides))