def time_to_arrive(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])

def get_max_points(start_pos, client_pos, finish_pos,\
                   curr_time, earl_start, latest_fin,\
                   num_steps):
    # How much time we have for the ride.
    max_time = latest_fin - earl_start
    # How much time we have till the end
    # of the simulation.
    max_steps_left = num_steps - curr_time
    # How many scores we can get in case we arrive in time.
    default_scores = time_to_arrive(start_pos, finish_pos)
    
    if (max_time <= 0 or max_steps_left < default_score):
        return 0
    
    time_to_client = time_to_arrive(start_pos, client_pos)
    time_to_finish = time_to_arrive(client_pos, finish_pos)
    
    return 1
	
def get_ride_for_vehicle(car, time, rides, total_steps):
	return max(rides, key = lambda r: get_max_points(car, r.start, r.finish, time, r.earliest, r.latest, total_steps))