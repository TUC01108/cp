def count_less_than(race_times, threshold):
    advance_to_next_round = []
    for race_time in race_times:
        if race_time < threshold:
            advance_to_next_round.append(race_time)
    return len(advance_to_next_round)
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))
