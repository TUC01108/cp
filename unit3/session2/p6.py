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
    # Step 1: Initialize an empty list to store the results
    ans = []
    # Step 2: Initialize an empty dictionary for next greater elements
    next_greater_map = {}
    # Step 3: Use a stack to find next greater elements
    stack = []
    for event in reversed(schedule2):
        # Pop elements from the stack until you find a greater element
        while stack and stack[-1] <= event:
            stack.pop()
        # If the stack is not empty, the top element is the next greater event
        if stack:
            next_greater_map[event] = stack[-1]
        else:
            # If the stack is empty, there is no greater event
            next_greater_map[event] = -1
        # Push the current event onto the stack
        stack.append(event)

    # Step 4: Populate the result list using the dictionary
    for event in schedule1:
        ans.append(next_greater_map[event])
    return ans
        

# Example Usage:

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4])) 

# Example Output:

# [-1, 3, -1]
# [3, -1]

# schedule2 [1,2,3,4]
# 4: -1
# push 4 on to the stack: stack[4]
# 3: 4
# stack has 4 which is more than 3 so next_greater_map[3] = 4
# push 3 onto the stack: stack = [4, 3]
# 2: 3
# stack has 3 which is greater than 2, next_greater_map[2] = 3
# push 2 onto the stack: stack = [4,3,2]
# 1: 2
# stack has 2 which is greater thatn 1, next_greater_map[1] = 2
# push 1 onto the stack: stack = [4,3,2,1]
# for event in schedule1:
# ans.append(next_greater_map[event])
# 3, -1