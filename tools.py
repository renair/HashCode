def time_to_arrive(fr, to):
    return abs(to[0] - fr[0]) + abs(to[1] - fr[1])

print time_to_arrive((0, 0), (2, 2))
