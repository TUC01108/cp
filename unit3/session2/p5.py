# You are organizing a cultural festival and have two performance schedules, 
# schedule1 and schedule2, each represented by a string where each character 
# corresponds to a performance slot. Merge the schedules by adding performances
#  in alternating order, starting with schedule1. If one schedule is longer 
# than the other, append the additional performances onto the end of the 
# merged schedule.

# Return the merged performance schedule.

def merge_schedules(schedule1, schedule2):
    zipList = []
    for char1, char2 in zip(schedule1, schedule2):
        zipList.append(char1)
        zipList.append(char2)
    zipList.extend(schedule1[len(schedule2):])
    # print(schedule1[len(schedule2):])
    zipList.extend(schedule2[len(schedule1):])
    return ''.join(zipList)
    pass

# Example Usage:

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

# Example Output:

# apbqcr
# apbqrs
# apbqcd
