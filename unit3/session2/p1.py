
def manage_stage_changes(changes):
    # take in a list of strings- changes

    # save performance in stack
    performance = []
    # save cancelled in stack
    cancelled = []
    # append() to performance
    for show in changes:
        if show.startswith("Schedule"):
            letter = show.split()[1]
            performance.append(letter)
        if performance and show == "Cancel":
            m = performance.pop()
            cancelled.append(m)
        elif show == "Reschedule" and cancelled:
            n = cancelled.pop()
            performance.append(n)
    return performance

        

    # if cancelled append() to cancelled
    # if rescheduled pop() from cancelled and append to performance
    # return performance stack

# Example Usage:

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Example Output:

# ["A", "C", "B", "D"]
# []
# ["Z"]
