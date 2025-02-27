# You are given an array audiences consisting of positive integers 
# representing the audience size for different performances at a music festival.

# Return the combined audience size of all performances in audiences with 
# the maximum audience size.

# The audience size of a performance is the number of people who attended 
# that performance.
from collections import Counter
def max_audience_performances(audiences):
    # find the performance with the maximum audience size
    count = Counter(audiences)
    # print(count)
    max_size = max(audiences)
    # print(count[max_size])
    if count[max_size] > 1:
        combined_audience_size = max_size * count[max_size]
    else:
        combined_audience_size = max_size 
    #print(max_size)
    return combined_audience_size
    pass

# Example Usage:

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
