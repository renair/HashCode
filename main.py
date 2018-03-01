import objects as obj
import obj_parser as pars
import simulation
import tools

model, rides = pars.parse_file("a_example.in")


#Відсортувати список поїздок
sm = Simulation()
#Цикл:
for v in sm.vehicles:
	ride = get_ride_for_vehicle(v, 0, rides, model.steps, model.per_time_bonus)
	sm.addRide(ride, v)

while sm.time < model.steps or len(rides) == 0:
#Додати поїздки до симуляції
#Запустити симуляцію
	free_cars = sm.simulate()
	for v in free_cars:
		ride = get_ride_for_vehicle(v, sm.time, rides, model.steps, model.per_time_bonus)
		sm.addRide(ride, v)
#Взяти позиції автомобілів із симуляції