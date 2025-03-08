# At a cultural festival, you have a schedule of events where each event
#  has a unique popularity score. The schedule is represented by two 
# distinct 0-indexed integer arrays schedule1 and schedule2, where 
# schedule1 is a subset of schedule2.

# For each event in schedule1, find its position in schedule2 and 
# determine the next event in schedule2 with a higher popularity score. 
# If there is no such event, then the answer for that event is -1.

# Return an array ans of length schedule1.length such that ans[i] is the 
# next greater event's popularity score as described above.

def next_greater_event(schedule1, schedule2):
  
  pass

# Example Usage:

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 

# Example Output:

# [-1, 3, -1]
# [3, -1]
