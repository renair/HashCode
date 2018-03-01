def time_to_arrive(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])


def get_max_points(start_pos, client_pos, finish_pos,\
                   curr_time, earl_start, latest_fin,\
                   num_steps, bonus):
    # How much time we have for the ride.
    max_steps_curr = latest_fin - earl_start
    # How much time we have till the end
    # of the simulation.
    max_steps_left = num_steps - curr_time
    # How many steps we need to get the client.
    time_to_client = time_to_arrive(start_pos, client_pos)
    # How many steps we need to get the destination.
    time_to_finish = time_to_arrive(client_pos, finish_pos)
    # How many scores we can get in case we arrive in time.
    default_scores = time_to_client + time_to_finish
    
    if (max_steps_curr <= 0 or max_steps_left < default_score):
        return 0
    
    return default_scores + bonus

