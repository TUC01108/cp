# You are organizing a cultural festival and have a list of performances
#  represented by an integer array performances. Each performance is 
# classified as either an even type (e.g., dance, music) or an odd type
#  (e.g., drama, poetry).

# Your task is to rearrange the performances so that all the even-type 
# performances appear at the beginning of the array, followed by all the
#  odd-type performances.

# Return any array that satisfies this condition.

def sort_performances_by_type(performances):
    # split performances into 2 lists and then combine them into 1
    # list 1 will be all even numbers
    # list 2 will be all odd numbers
    # list 1 will be first in list 3 and list 2 will append to the end
    evenList = []
    oddList = []
    for performance in performances:
        if performance % 2 == 0:
            evenList.append(performance)
        else:
            oddList.append(performance)
    
    list3 = evenList + oddList

    return list3

# Example Usage:

print(sort_performances_by_type([3, 1, 2, 4]))  
print(sort_performances_by_type([0]))  

# Example Output:

# [4, 2, 1, 3]
# [0]
