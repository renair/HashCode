def time_to_arrive(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])

def get_max_points(start_pos, ride, curr_time, total_steps, bonus):
	client_pos = ride.start
	finish_pos = ride.finish
	earl_start = ride.earliest
	latest_fin = ride.latest
	
    # How much time we have for the ride.
    max_steps_curr = latest_fin - earl_start
    # How much time we have till the end
    # of the simulation.
    max_steps_left = total_steps - curr_time
    # How many steps we need to get the client.
    time_to_client = time_to_arrive(start_pos, client_pos)
    # How many steps we need to get the destination.
    time_to_finish = time_to_arrive(client_pos, finish_pos)
    # How many scores we can get in case we arrive in time.
    default_scores = time_to_client + time_to_finish
    
	if (max_steps_curr <= 0 or max_steps_left < default_score):
        return 0
    
    return default_scores + bonus
	
def get_ride_for_vehicle(car, time, rides, total_steps, bonus):
	return max(rides, key = lambda r: get_max_points(car.pos, r, time, total_steps, bonus))
