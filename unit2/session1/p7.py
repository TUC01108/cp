# If you used a dictionary as part of your solution to 
# max_audience_performances() in the previous problem, try reimplementing 
# the function without using a dictionary. If you implemented 
# max_audience_performances() without using a dictionary, try solving the 
# problem with a dictionary.

# Once you've come up with your second solution, compare the two. Is one 
# solution better than the other? Why or why not?

from collections import Counter
def max_audience_performances(audiences):
    audience_count = {}
    for audience in audiences:
        if audience in audience_count:
            audience_count[audience] += 1
        else:
            audience_count[audience] = 1
    max_size = max(audiences)

    if audience_count[max_size] > 1:
        combined_audience_size = max_size * audience_count[max_size]
    else:
        combined_audience_size = max_size
    return combined_audience_size


    pass

# Example Usage:

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
