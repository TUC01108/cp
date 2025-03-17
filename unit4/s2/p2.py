# You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. 
# You have a list of work sessions, each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

# Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to 
# find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space 
# complexity.

def find_smallest_gap(work_sessions):
    min = 0
    start_hold = None
    end_hold = None
    for session in work_sessions:
        start_hold = session[0]
        if end_hold:
            min = start_hold - end_hold
        end_hold = session[1]
    print(min)
  

# Example Usage:

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))

# Example Output:

# 60
# 30
# 15
